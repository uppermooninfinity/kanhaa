import os
import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# -----------------------------------------------------
# TELEGRAM API
# -----------------------------------------------------

API_ID = int(os.getenv("API_ID", "0"))
API_HASH = os.getenv("API_HASH", "")

BOT_TOKEN = os.getenv("BOT_TOKEN", "")
BOT_ID = int(os.getenv("BOT_ID", "0"))

OWNER_USERNAME = os.getenv("OWNER_USERNAME", "toxication_infinity")

BOT_USERNAME = os.getenv("BOT_USERNAME", "astral_xbot")
BOT_NAME = os.getenv("BOT_NAME", "🎧 Uᴘᴘᴇʀ ᴍᴏᴏɴ")

ASSUSERNAME = os.getenv("ASSUSERNAME", "mrs_radha")
SUPERBAN_ADMINS = list(map(int, os.getenv("SUPERBAN_ADMINS", "7651303468,8285730532,8566964639").split()))
SUPERBAN_LOG_GC = int(os.getenv("SUPERBAN_LOG_GC", -1003882647583))
SUPERBAN_CHANNEL = int(os.getenv("SUPERBAN_CHANNEL", -1003647170816))

# -----------------------------------------------------
# DATABASE
# -----------------------------------------------------

MONGO_DB_URI = os.getenv("MONGO_DB_URI", "")
API_KEY = os.getenv("API_KEY", "")

# -----------------------------------------------------
# LIMITS
# -----------------------------------------------------

DURATION_LIMIT_MIN = int(os.getenv("DURATION_LIMIT", "17000"))

# -----------------------------------------------------
# LOGGER
# -----------------------------------------------------

LOGGER_ID = int(os.getenv("LOGGER_ID", "0"))
CLONE_LOGGER = LOGGER_ID

# -----------------------------------------------------
# OWNER
# -----------------------------------------------------

OWNER_ID = int(os.getenv("OWNER_ID", "8143754205"))

# -----------------------------------------------------
# HEROKU
# -----------------------------------------------------

HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME", "")
HEROKU_API_KEY = os.getenv("HEROKU_API_KEY", "")

# -----------------------------------------------------
# GIT
# -----------------------------------------------------

SOURCE = os.getenv("SOURCE", "https://github.com//theteaminfinitybots/team-infinity-bots")

UPSTREAM_REPO = os.getenv(
    "UPSTREAM_REPO",
    "https://github.com/uppermooninfinity/kanhaa",
)

UPSTREAM_BRANCH = os.getenv("UPSTREAM_BRANCH", "main")

GIT_TOKEN = os.getenv("GIT_TOKEN", "")

# -----------------------------------------------------
# SUPPORT
# -----------------------------------------------------

SUPPORT_CHANNEL = os.getenv(
    "SUPPORT_CHANNEL", "https://t.me/dark_musictm"
)

SUPPORT_CHAT = os.getenv(
    "SUPPORT_CHAT", "https://t.me/snowy_hometown"
)

# -----------------------------------------------------
# ASSISTANT SETTINGS
# -----------------------------------------------------

AUTO_LEAVING_ASSISTANT = os.getenv(
    "AUTO_LEAVING_ASSISTANT", "False"
).lower() == "true"

AUTO_LEAVE_ASSISTANT_TIME = int(
    os.getenv("ASSISTANT_LEAVE_TIME", "9000")
)

SONG_DOWNLOAD_DURATION = int(
    os.getenv("SONG_DOWNLOAD_DURATION", "9999999")
)

SONG_DOWNLOAD_DURATION_LIMIT = int(
    os.getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999999")
)

# -----------------------------------------------------
# SPOTIFY
# -----------------------------------------------------

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID", "")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET", "")

# -----------------------------------------------------
# PLAYLIST
# -----------------------------------------------------

PLAYLIST_FETCH_LIMIT = int(
    os.getenv("PLAYLIST_FETCH_LIMIT", "25")
)

# -----------------------------------------------------
# FILE SIZE
# -----------------------------------------------------

TG_AUDIO_FILESIZE_LIMIT = int(
    os.getenv("TG_AUDIO_FILESIZE_LIMIT", "5242880000")
)

TG_VIDEO_FILESIZE_LIMIT = int(
    os.getenv("TG_VIDEO_FILESIZE_LIMIT", "5242880000")
)

# -----------------------------------------------------
# SESSION STRINGS
# -----------------------------------------------------

STRING1 = os.getenv("STRING_SESSION", "")
STRING2 = os.getenv("STRING_SESSION2", None)

# -----------------------------------------------------
# GLOBAL LISTS
# -----------------------------------------------------

BANNED_USERS = filters.user()

adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# -----------------------------------------------------
# STREAM IMAGES
# -----------------------------------------------------
SUPERBAN_VIDEO = "https://litter.catbox.moe/90xmzlql8un278km.mp4"
STREAMI_PICS = [
    "https://graph.org/file/c53dfca85e9e0b5bc9cd1-afa1339cd5d4e6522c.jpg",
    "https://graph.org/file/c53dfca85e9e0b5bc9cd1-afa1339cd5d4e6522c.jpg",
    "https://graph.org/file/c53dfca85e9e0b5bc9cd1-afa1339cd5d4e6522c.jpg",
    "https://graph.org/file/c53dfca85e9e0b5bc9cd1-afa1339cd5d4e6522c.jpg",
    "https://graph.org/file/c53dfca85e9e0b5bc9cd1-afa1339cd5d4e6522c.jpg",
    "https://graph.org/file/c53dfca85e9e0b5bc9cd1-afa1339cd5d4e6522c.jpg",
    "https://graph.org/file/c53dfca85e9e0b5bc9cd1-afa1339cd5d4e6522c.jpg",
    "https://graph.org/file/c53dfca85e9e0b5bc9cd1-afa1339cd5d4e6522c.jpg",
    "https://graph.org/file/c53dfca85e9e0b5bc9cd1-afa1339cd5d4e6522c.jpg",
    "https://files.catbox.moe/7icvpu.jpg",
    "https://files.catbox.moe/4hd77z.jpg",
    "https://files.catbox.moe/yn7wje.jpg",
    "https://files.catbox.moe/kifsir.jpg",
    "https://files.catbox.moe/zi21kc.jpg",
    "https://files.catbox.moe/z0gh23.jpg",
    "https://files.catbox.moe/f2s4ws.jpg",
    "https://files.catbox.moe/26nzoq.jpg",
    "https://files.catbox.moe/fu6jk3.jpg",
]

# -----------------------------------------------------
# IMAGE URLS
# -----------------------------------------------------

HELP_IMG_URL = os.getenv(
    "HELP_IMG_URL",
    "https://i.ibb.co/xPjc7tv/help-menu.jpg"
)

START_IMG_URL = os.getenv(
    "START_IMG_URL",
    "https://graph.org/file/c53dfca85e9e0b5bc9cd1-afa1339cd5d4e6522c.jpg"
)

PING_IMG_URL = os.getenv(
    "PING_IMG_URL",
    "https://files.catbox.moe/26nzoq.jpg"
)

PLAYLIST_IMG_URL = "https://files.catbox.moe/f2s4ws.jpg"
STATS_IMG_URL = "https://files.catbox.moe/z0gh23.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/2y5o3g.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/2y5o3g.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/d30d11c4365c025c25e3e.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/d30d11c4365c025c25e3e.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/2y5o3g.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/2y5o3g.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/2y5o3g.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/d30d11c4365c025c25e3e.jpg"

# -----------------------------------------------------
# TIME CONVERTER
# -----------------------------------------------------

def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60 ** i
        for i, x in enumerate(reversed(stringt.split(":")))
    )

DURATION_LIMIT = int(
    time_to_seconds(f"{DURATION_LIMIT_MIN}:00")
)

# -----------------------------------------------------
# URL VALIDATION
# -----------------------------------------------------

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] SUPPORT_CHANNEL must start with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] SUPPORT_CHAT must start with https://"
        )

# -----------------------------------------------------
# GREET EMOJIS
# -----------------------------------------------------

GREET = [
    "💞","🥂","🔍","🧪","🥂","⚡️","🔥","🦋","🎩",
    "🌈","🍷","🥂","🦋","🥃","🥤","🕊️","🦋",
    "🦋","🕊️","⚡️","🕊️","⚡️","⚡️","🥂","💌",
    "🥂","🥂","🧨"
]
