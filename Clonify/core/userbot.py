from pyrogram import Client
import config
from ..logging import LOGGER

assistants = []
assistantids = []


class Userbot:
    def __init__(self):

        self.one = Client(
            name="PROAss1",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING1),
            no_updates=True,
        )

    async def start(self):
        LOGGER(__name__).info("Starting Assistants...")

        if not config.STRING1:
            LOGGER(__name__).warning("STRING_SESSION not provided.")
            return

        try:
            await self.one.start()
        except Exception as e:
            LOGGER(__name__).error(f"Assistant failed to start: {e}")
            return

        # Auto join support chats
        try:
            await self.one.join_chat("dark_musictm")
            await self.one.join_chat("snowy_hometown")
        except Exception:
            pass

        assistants.append(1)

        try:
            await self.one.send_message(
                config.LOGGER_ID,
                "✅ Assistant Started Successfully"
            )
        except Exception as e:
            LOGGER(__name__).error(
                "Assistant cannot access log group. "
                "Add assistant to log group and make admin."
            )
            LOGGER(__name__).error(e)

        # Assistant
