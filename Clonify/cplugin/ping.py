import time
from datetime import datetime

import psutil
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from config import PING_IMG_URL
from Clonify.utils import get_readable_time
from Clonify.utils.database.clonedb import (
    get_owner_id_from_db,
    get_cloned_support_chat,
    get_cloned_support_channel,
)
from Clonify.plugins.utils import StartTime


@Client.on_message(filters.command("ping"))
async def ping_clone(client: Client, message: Message):

    bot = await client.get_me()

    # owner id
    C_BOT_OWNER_ID = get_owner_id_from_db(bot.id)

    # support chat
    C_BOT_SUPPORT_CHAT = await get_cloned_support_chat(bot.id)

    if C_BOT_SUPPORT_CHAT:
        C_SUPPORT_CHAT = f"https://t.me/{C_BOT_SUPPORT_CHAT}"
    else:
        C_SUPPORT_CHAT = "https://t.me/telegram"

    # ping message
    msg = await message.reply_photo(
        photo=PING_IMG_URL,
        caption=f"{bot.mention} is pinging..."
    )

    # system stats
    uptime_sec = int(time.time() - StartTime)
    uptime = get_readable_time(uptime_sec)

    cpu = psutil.cpu_percent(interval=0.5)
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent

    start = datetime.now()
    end = datetime.now()
    resp = (end - start).microseconds / 1000

    # edit message
    await msg.edit_text(
        f"""🏓 **Pong:** `{resp} ms`

**{bot.mention} System Stats**

• **Uptime:** {uptime}  
• **CPU:** {cpu}%  
• **RAM:** {mem}%  
• **Disk:** {disk}%""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Support",
                        url=C_SUPPORT_CHAT
                    )
                ]
            ]
        ),
    )
