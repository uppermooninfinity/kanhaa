from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient

import config
from ..logging import LOGGER

# -----------------------------------------------------

if not config.MONGO_DB_URI:
    LOGGER(__name__).error("No MONGO_DB_URI found in environment!")
    raise SystemExit("MongoDB URI is missing")

# -----------------------------------------------------

try:
    _mongo_async_ = AsyncIOMotorClient(config.MONGO_DB_URI)
    _mongo_sync_ = MongoClient(config.MONGO_DB_URI)

    # Database name
    mongodb = _mongo_async_.Anon
    pymongodb = _mongo_sync_.Anon

    LOGGER(__name__).info("MongoDB Connected Successfully")

except Exception as e:
    LOGGER(__name__).error(f"MongoDB Connection Failed: {e}")
    raise SystemExit
