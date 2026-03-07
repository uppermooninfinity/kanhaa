from pyrogram import Client, filters
from Clonify import app
from Clonify.utils.database import set_start_pic

@app.on_message(filters.command("setstartpic") & filters.private)
async def set_startpic(client, message):
    if not message.reply_to_message:
        return await message.reply("Reply to a photo")

    photo = message.reply_to_message.photo.file_id
    user_id = message.from_user.id

    await set_start_pic(user_id, photo)

    await message.reply("Start photo saved.")
