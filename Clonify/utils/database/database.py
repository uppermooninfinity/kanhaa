import random
from typing import Dict, List, Union

from Clonify import userbot
from Clonify.core.mongo import mongodb

# ---------------- DATABASE ---------------- #

authdb = mongodb.adminauth
authuserdb = mongodb.authuser
autoenddb = mongodb.autoend
assdb = mongodb.assistants
blacklist_chatdb = mongodb.blacklistChat
blockeddb = mongodb.blockedusers
chatsdb = mongodb.chats
channeldb = mongodb.cplaymode
countdb = mongodb.upcount
gbansdb = mongodb.gban
langdb = mongodb.language
onoffdb = mongodb.onoffper
playmodedb = mongodb.playmode
playtypedb = mongodb.playtypedb
skipdb = mongodb.skipmode
sudoersdb = mongodb.sudoers
usersdb = mongodb.tgusersdb
privatedb = mongodb.privatechats
suggdb = mongodb.suggestion
cleandb = mongodb.cleanmode
queriesdb = mongodb.queries
userdb = mongodb.userstats
videodb = mongodb.vipvideocalls

# CLONE DATABASE
chatsdbc = mongodb.chatsc
usersdbc = mongodb.tgusersdbc


# ---------------- MEMORY CACHE ---------------- #

active = []
activevideo = []
assistantdict = {}
skipmode = {}
playmode = {}
playtype = {}
pause = {}
mute = {}
loop = {}
count = {}
channelconnect = {}
langm = {}
maintenance = []
nonadmin = {}
privatechats = {}
suggestion = {}
cleanmode = []


# ---------------- QUERY COUNT ---------------- #

async def get_queries():
    data = await queriesdb.find_one({"chat_id": 98324})
    if not data:
        return 0
    return data.get("mode", 0)


async def set_queries(mode: int):
    data = await queriesdb.find_one({"chat_id": 98324})

    if data:
        mode = data.get("mode", 0) + mode

    await queriesdb.update_one(
        {"chat_id": 98324},
        {"$set": {"mode": mode}},
        upsert=True,
    )


# ---------------- ASSISTANT ---------------- #

async def get_client(num: int):
    if num == 1:
        return userbot.one
    if num == 2:
        return userbot.two
    if num == 3:
        return userbot.three
    if num == 4:
        return userbot.four
    if num == 5:
        return userbot.five


async def set_assistant(chat_id: int):

    from Clonify.core.userbot import assistants

    ran = random.choice(assistants)

    assistantdict[chat_id] = ran

    await assdb.update_one(
        {"chat_id": chat_id},
        {"$set": {"assistant": ran}},
        upsert=True,
    )

    return await get_client(ran)


async def get_assistant(chat_id: int):

    from Clonify.core.userbot import assistants

    assistant = assistantdict.get(chat_id)

    if assistant:
        return await get_client(assistant)

    data = await assdb.find_one({"chat_id": chat_id})

    if not data:
        return await set_assistant(chat_id)

    num = data.get("assistant")

    if num not in assistants:
        return await set_assistant(chat_id)

    assistantdict[chat_id] = num

    return await get_client(num)


# ---------------- SKIP MODE ---------------- #

async def is_skipmode(chat_id: int):

    mode = skipmode.get(chat_id)

    if mode is None:

        data = await skipdb.find_one({"chat_id": chat_id})

        if not data:
            skipmode[chat_id] = True
            return True

        skipmode[chat_id] = False
        return False

    return mode


async def skip_on(chat_id: int):

    skipmode[chat_id] = True

    await skipdb.delete_one({"chat_id": chat_id})


async def skip_off(chat_id: int):

    skipmode[chat_id] = False

    await skipdb.update_one(
        {"chat_id": chat_id},
        {"$set": {"chat_id": chat_id}},
        upsert=True,
    )


# ---------------- LANGUAGE ---------------- #

async def get_lang(chat_id: int):

    mode = langm.get(chat_id)

    if mode:
        return mode

    data = await langdb.find_one({"chat_id": chat_id})

    if not data:
        langm[chat_id] = "en"
        return "en"

    langm[chat_id] = data.get("lang", "en")

    return langm[chat_id]


async def set_lang(chat_id: int, lang: str):

    langm[chat_id] = lang

    await langdb.update_one(
        {"chat_id": chat_id},
        {"$set": {"lang": lang}},
        upsert=True,
    )


# ---------------- MUSIC STATE ---------------- #

async def is_music_playing(chat_id: int):
    return pause.get(chat_id, False)


async def music_on(chat_id: int):
    pause[chat_id] = True


async def music_off(chat_id: int):
    pause[chat_id] = False


# ---------------- MUTE ---------------- #

async def is_muted(chat_id: int):
    return mute.get(chat_id, False)


async def mute_on(chat_id: int):
    mute[chat_id] = True


async def mute_off(chat_id: int):
    mute[chat_id] = False


# ---------------- ACTIVE CHATS ---------------- #

async def get_active_chats():
    return active


async def add_active_chat(chat_id: int):
    if chat_id not in active:
        active.append(chat_id)


async def remove_active_chat(chat_id: int):
    if chat_id in active:
        active.remove(chat_id)


# ---------------- CLONE USERS ---------------- #

async def add_served_user_clone(user_id: int, bot_id: int):

    data = await usersdbc.find_one(
        {"user_id": user_id, "bot_id": bot_id}
    )

    if not data:
        await usersdbc.insert_one(
            {"user_id": user_id, "bot_id": bot_id}
        )


async def get_served_users_clone(bot_id: int):

    return [
        user async for user in usersdbc.find({"bot_id": bot_id})
    ]


async def add_served_chat_clone(chat_id: int, bot_id: int):

    data = await chatsdbc.find_one(
        {"chat_id": chat_id, "bot_id": bot_id}
    )

    if not data:
        await chatsdbc.insert_one(
            {"chat_id": chat_id, "bot_id": bot_id}
        )


async def get_served_chats_clone(bot_id: int):

    return [
        chat async for chat in chatsdbc.find({"bot_id": bot_id})
    ]


# ---------------- START PANEL DATABASE ---------------- #

startpicdb = mongodb.startpic
startvideodb = mongodb.startvideo
starttextdb = mongodb.starttext
startbuttondb = mongodb.startbuttons


async def set_start_pic(user_id: int, pic: str):

    await startpicdb.update_one(
        {"user_id": user_id},
        {"$set": {"pic": pic}},
        upsert=True,
    )


async def get_start_pic(user_id: int):

    data = await startpicdb.find_one({"user_id": user_id})

    if not data:
        return None

    return data["pic"]


async def set_start_video(user_id: int, video: str):

    await startvideodb.update_one(
        {"user_id": user_id},
        {"$set": {"video": video}},
        upsert=True,
    )


async def get_start_video(user_id: int):

    data = await startvideodb.find_one({"user_id": user_id})

    if not data:
        return None

    return data["video"]


async def set_start_text(user_id: int, text: str):

    await starttextdb.update_one(
        {"user_id": user_id},
        {"$set": {"text": text}},
        upsert=True,
    )


async def get_start_text(user_id: int):

    data = await starttextdb.find_one({"user_id": user_id})

    if not data:
        return None

    return data["text"]


async def set_start_buttons(user_id: int, buttons: list):

    await startbuttondb.update_one(
        {"user_id": user_id},
        {"$set": {"buttons": buttons}},
        upsert=True,
    )


async def get_start_buttons(user_id: int):

    data = await startbuttondb.find_one({"user_id": user_id})

    if not data:
        return None

    return data["buttons"]
