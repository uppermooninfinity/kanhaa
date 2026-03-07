from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Clonify import app
from Clonify.core.mongo import mongodb
from config import OWNER_ID

startdb = mongodb.clonestart


# START COMMAND
@app.on_message(filters.command("start"))
async def start_cmd(client, message):

    bot = await client.get_me()
    bot_id = bot.id

    data = await startdb.find_one({"bot_id": bot_id})

    if not data:
        return await message.reply("Bot Started Successfully")

    text = data.get("text")
    photo = data.get("photo")
    video = data.get("video")
    gif = data.get("gif")
    buttons = data.get("buttons")

    keyboard = None

    if buttons:
        btn = []
        for b in buttons:
            btn.append([InlineKeyboardButton(b["name"], url=b["url"])])
        keyboard = InlineKeyboardMarkup(btn)

    if photo:
        await message.reply_photo(photo, caption=text, reply_markup=keyboard)

    elif video:
        await message.reply_video(video, caption=text, reply_markup=keyboard)

    elif gif:
        await message.reply_animation(gif, caption=text, reply_markup=keyboard)

    else:
        await message.reply(text, reply_markup=keyboard)


# SET START TEXT
@app.on_message(filters.command("setstarttext") & filters.private)
async def set_start_text(client, message):

    if message.from_user.id != OWNER_ID:
        return await message.reply("Only bot owner can use this")

    bot = await client.get_me()
    bot_id = bot.id

    if len(message.command) < 2:
        return await message.reply("Use: /setstarttext your text")

    text = message.text.split(None, 1)[1]

    await startdb.update_one(
        {"bot_id": bot_id},
        {"$set": {"text": text}},
        upsert=True
    )

    await message.reply("✅ Start text saved")


# SET PHOTO
@app.on_message(filters.command("setstartpic") & filters.private)
async def set_start_pic(client, message):

    if message.from_user.id != OWNER_ID:
        return

    bot = await client.get_me()
    bot_id = bot.id

    if not message.reply_to_message or not message.reply_to_message.photo:
        return await message.reply("Reply to a photo")

    file_id = message.reply_to_message.photo.file_id

    await startdb.update_one(
        {"bot_id": bot_id},
        {"$set": {"photo": file_id}},
        upsert=True
    )

    await message.reply("✅ Start photo saved")


# SET VIDEO
@app.on_message(filters.command("setstartvideo") & filters.private)
async def set_start_video(client, message):

    if message.from_user.id != OWNER_ID:
        return

    bot = await client.get_me()
    bot_id = bot.id

    if not message.reply_to_message or not message.reply_to_message.video:
        return await message.reply("Reply to a video")

    file_id = message.reply_to_message.video.file_id

    await startdb.update_one(
        {"bot_id": bot_id},
        {"$set": {"video": file_id}},
        upsert=True
    )

    await message.reply("✅ Start video saved")


# SET GIF
@app.on_message(filters.command("setstartgif") & filters.private)
async def set_start_gif(client, message):

    if message.from_user.id != OWNER_ID:
        return

    bot = await client.get_me()
    bot_id = bot.id

    if not message.reply_to_message or not message.reply_to_message.animation:
        return await message.reply("Reply to a GIF")

    file_id = message.reply_to_message.animation.file_id

    await startdb.update_one(
        {"bot_id": bot_id},
        {"$set": {"gif": file_id}},
        upsert=True
    )

    await message.reply("✅ Start GIF saved")


# SET BUTTONS
@app.on_message(filters.command("setstartbuttons") & filters.private)
async def set_buttons(client, message):

    if message.from_user.id != OWNER_ID:
        return

    bot = await client.get_me()
    bot_id = bot.id

    if len(message.command) < 3:
        return await message.reply(
            "Use:\n/setstartbuttons ButtonName https://link.com"
        )

    name = message.command[1]
    url = message.command[2]

    data = await startdb.find_one({"bot_id": bot_id})

    buttons = []

    if data and data.get("buttons"):
        buttons = data.get("buttons")

    buttons.append({"name": name, "url": url})

    await startdb.update_one(
        {"bot_id": bot_id},
        {"$set": {"buttons": buttons}},
        upsert=True
    )

    await message.reply("✅ Button added")


# PREVIEW
@app.on_message(filters.command("previewstart") & filters.private)
async def preview_start(client, message):

    bot = await client.get_me()
    bot_id = bot.id

    data = await startdb.find_one({"bot_id": bot_id})

    if not data:
        return await message.reply("No start settings")

    text = data.get("text")
    photo = data.get("photo")
    video = data.get("video")
    gif = data.get("gif")

    if photo:
        await message.reply_photo(photo, caption=text)

    elif video:
        await message.reply_video(video, caption=text)

    elif gif:
        await message.reply_animation(gif, caption=text)

    else:
        await message.reply(text)


# RESET
@app.on_message(filters.command("resetstart") & filters.private)
async def reset_start(client, message):

    if message.from_user.id != OWNER_ID:
        return

    bot = await client.get_me()
    bot_id = bot.id

    await startdb.delete_one({"bot_id": bot_id})

    await message.reply("✅ Start reset")
