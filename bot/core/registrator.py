from pyrogram import Client
from bot.config import settings
from bot.utils import logger


async def register_sessions() -> None:
    API_ID = settings.API_ID
    API_HASH = settings.API_HASH

    if not API_ID or not API_HASH:
        raise ValueError("API_ID and API_HASH are not found in the .env file. Please check the configuration.")

    session_name = input('\nEnter the session name (press Enter to exit): ').strip()

    if not session_name:
        print("Session registration process canceled.")
        return

    if not session_name.isalnum():
        print("Session name can only contain letters and numbers.")
        return

    session = Client(
        name=session_name,
        api_id=API_ID,
        api_hash=API_HASH,
        workdir="sessions/"
    )

    try:
        async with session:
            user_data = await session.get_me()
        logger.success(f"Session successfully added @{user_data.username} | {user_data.first_name} {user_data.last_name}")
    except Exception as e:
        logger.error(f"Failed to add session: {e}")
