from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Clonify import app
from Clonify.core.clone import get_owner_id_from_db
from Clonify.core.mongo import mongodb

startdb = mongodb.clonestart

# SAVE TEXT
@app.on_message(filters.command("setstarttext") & filters.private)
async def set_start_text(client, message):

    bot_id = client.me.id
    owner = get_owner_id_from_db(bot_id)

    if message.from_user.id != owner:
        return await message.reply("Only bot owner can use this")

    text = message.text.split(None,1)[1]

    await startdb.update_one(
        {"bot_id": bot_id},
        {"$set": {"text": text}},
        upsert=True
    )

    await message.reply("✅ Start text saved")


# SAVE PHOTO
@app.on_message(filters.command("setstartpic") & filters.private)
async def set_start_pic(client, message):

    bot_id = client.me.id
    owner = get_owner_id_from_db(bot_id)

    if message.from_user.id != owner:
        return

    if not message.reply_to_message.photo:
        return await message.reply("Reply to a photo")

    file_id = message.reply_to_message.photo.file_id

    await startdb.update_one(
        {"bot_id": bot_id},
        {"$set": {"photo": file_id}},
        upsert=True
    )

    await message.reply("✅ Start photo saved")


# SAVE VIDEO
@app.on_message(filters.command("setstartvideo") & filters.private)
async def set_start_video(client, message):

    bot_id = client.me.id
    owner = get_owner_id_from_db(bot_id)

    if message.from_user.id != owner:
        return

    if not message.reply_to_message.video:
        return await message.reply("Reply to a video")

    file_id = message.reply_to_message.video.file_id

    await startdb.update_one(
        {"bot_id": bot_id},
        {"$set": {"video": file_id}},
        upsert=True
    )

    await message.reply("✅ Start video saved")


# PREVIEW
@app.on_message(filters.command("previewstart") & filters.private)
async def preview_start(client, message):

    bot_id = client.me.id
    data = await startdb.find_one({"bot_id": bot_id})

    if not data:
        return await message.reply("No start settings")

    text = data.get("text")
    photo = data.get("photo")
    video = data.get("video")

    if photo:
        await message.reply_photo(photo, caption=text)

    elif video:
        await message.reply_video(video, caption=text)

    else:
        await message.reply(text)


# RESET
@app.on_message(filters.command("resetstart") & filters.private)
async def reset_start(client, message):

    bot_id = client.me.id
    owner = get_owner_id_from_db(bot_id)

    if message.from_user.id != owner:
        return

    await startdb.delete_one({"bot_id": bot_id})

    await message.reply("✅ Start reset")
