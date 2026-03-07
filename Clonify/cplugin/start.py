import time
import random
import asyncio

from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from youtubesearchpython.__future__ import VideosSearch

from Clonify import app
from Clonify.misc import _boot_

from Clonify.utils.database import (
    add_served_chat_clone,
    add_served_user_clone,
)

from Clonify.utils.decorators.language import LanguageStart
from Clonify.utils.formatters import get_readable_time
from Clonify.utils.inline import help_pannel

from config import BANNED_USERS, STREAMI_PICS
from strings import get_string

from Clonify.utils.database.clonedb import (
    get_owner_id_from_db,
    get_cloned_support_chat,
    get_cloned_support_channel,
)

from Clonify.cplugin.setinfo import get_logging_status, get_log_channel
from Clonify.core.mongo import mongodb


startdb = mongodb.clonestart


# =========================
# PRIVATE START
# =========================


@Client.on_message(filters.command(["start"]) & filters.private & ~BANNED_USERS)
@LanguageStart
async def start_pm(client, message: Message, _):

    bot = await client.get_me()
    bot_id = bot.id

    await add_served_user_clone(message.from_user.id, bot_id)

    # Loading animation
    msg = await message.reply_text("⚡")
    for i in ["ʟᴏᴀᴅɪɴɢ", "ʟᴏᴀᴅɪɴɢ.", "ʟᴏᴀᴅɪɴɢ..", "ʟᴏᴀᴅɪɴɢ..."]:
        await msg.edit_text(f"<b>{i}</b>")
        await asyncio.sleep(0.2)
    await msg.delete()

    # Owner
    OWNER = get_owner_id_from_db(bot_id)

    # Support Chat
    SUPPORT_CHAT = await get_cloned_support_chat(bot_id)
    SUPPORT_CHAT = f"https://t.me/{SUPPORT_CHAT}"

    # Support Channel
    SUPPORT_CHANNEL = await get_cloned_support_channel(bot_id)
    SUPPORT_CHANNEL = f"https://t.me/{SUPPORT_CHANNEL}"

    # START ARGUMENTS
    if len(message.text.split()) > 1:

        name = message.text.split(None, 1)[1]

        if name.startswith("help"):

            keyboard = help_pannel(_)

            return await message.reply_photo(
                random.choice(STREAMI_PICS),
                caption=_["help_1"].format(SUPPORT_CHAT),
                reply_markup=keyboard,
            )

        if name.startswith("info"):

            m = await message.reply_text("🔎")

            query = name.replace("info_", "", 1)
            query = f"https://www.youtube.com/watch?v={query}"

            results = VideosSearch(query, limit=1)

            for result in (await results.next())["result"]:

                title = result["title"]
                duration = result["duration"]
                views = result["viewCount"]["short"]
                thumbnail = result["thumbnails"][0]["url"].split("?")[0]
                channellink = result["channel"]["link"]
                channel = result["channel"]["name"]
                link = result["link"]
                published = result["publishedTime"]

            text = _["start_6"].format(
                title,
                duration,
                views,
                published,
                channellink,
                channel,
                bot.mention,
            )

            key = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Watch", url=link),
                        InlineKeyboardButton("Support", url=SUPPORT_CHAT),
                    ]
                ]
            )

            await m.delete()

            return await client.send_photo(
                message.chat.id,
                thumbnail,
                caption=text,
                reply_markup=key,
            )

    # =====================
    # MAIN START PANEL
    # =====================

    buttons = [
        [
            InlineKeyboardButton(
                "➕ Add Me To Group",
                url=f"https://t.me/{bot.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton("Owner", user_id=OWNER),
            InlineKeyboardButton("Channel", url=SUPPORT_CHANNEL),
        ],
        [
            InlineKeyboardButton("Settings", callback_data="settings_back_helper"),
        ],
    ]

    data = await startdb.find_one({"bot_id": bot_id})

    if data:

        text = data.get("text")
        photo = data.get("photo")
        video = data.get("video")

        if photo:

            await message.reply_photo(
                photo,
                caption=text,
                reply_markup=InlineKeyboardMarkup(buttons),
            )

        elif video:

            await message.reply_video(
                video,
                caption=text,
                reply_markup=InlineKeyboardMarkup(buttons),
            )

        else:

            await message.reply_text(
                text,
                reply_markup=InlineKeyboardMarkup(buttons),
            )

    else:

        await message.reply_photo(
            random.choice(STREAMI_PICS),
            caption=_["c_start_2"].format(
                message.from_user.mention,
                bot.mention,
                app.name,
                f"https://t.me/{app.username}",
                app.name,
                f"https://t.me/{app.username}",
                SUPPORT_CHANNEL,
                SUPPORT_CHAT,
            ),
            reply_markup=InlineKeyboardMarkup(buttons),
        )

    # =====================
    # LOGGING
    # =====================

    LOG_STATUS = get_logging_status(bot_id)
    LOGGER_ID = get_log_channel(bot_id)

    if LOG_STATUS:

        if str(LOGGER_ID) == "-100":
            LOGGER_ID = OWNER

        try:

            await client.send_message(
                chat_id=int(LOGGER_ID),
                text=f"✦ {message.from_user.mention} started the bot\n\n"
                f"User ID: `{message.from_user.id}`\n"
                f"Username: @{message.from_user.username}",
            )

        except Exception as e:
            print(f"[LOG ERROR] {e}")


# =========================
# GROUP START
# =========================


@Client.on_message(filters.command(["start"]) & filters.group & ~BANNED_USERS)
@LanguageStart
async def start_group(client, message: Message, _):

    bot = await client.get_me()
    bot_id = bot.id

    SUPPORT_CHAT = await get_cloned_support_chat(bot_id)
    SUPPORT_CHAT = f"https://t.me/{SUPPORT_CHAT}"

    buttons = [
        [
            InlineKeyboardButton(
                "➕ Add Me",
                url=f"https://t.me/{bot.username}?startgroup=true",
            ),
            InlineKeyboardButton("Support", url=SUPPORT_CHAT),
        ]
    ]

    uptime = int(time.time() - _boot_)

    await message.reply_photo(
        random.choice(STREAMI_PICS),
        caption=_["start_1"].format(bot.mention, get_readable_time(uptime)),
        reply_markup=InlineKeyboardMarkup(buttons),
    )

    await add_served_chat_clone(message.chat.id, bot_id)
