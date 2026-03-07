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


# ---------------- CHANNEL PLAY MODE ---------------- #

async def get_cmode(chat_id: int):

    mode = channelconnect.get(chat_id)

    if mode is not None:
        return mode

    data = await channeldb.find_one({"chat_id": chat_id})

    if not data:
        channelconnect[chat_id] = False
        return False

    channelconnect[chat_id] = data.get("mode", False)
    return channelconnect[chat_id]


async def set_cmode(chat_id: int, mode: bool):

    channelconnect[chat_id] = mode

    await channeldb.update_one(
        {"chat_id": chat_id},
        {"$set": {"mode": mode}},
        upsert=True,
    )


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
# ---------------- AUTH USER NAMES ---------------- #

async def get_authuser_names():
    """
    Returns a list of usernames from the authuser database
    """
    users = await authuserdb.find({}).to_list(length=None)
    return [user.get("username") for user in users if "username" in user]

