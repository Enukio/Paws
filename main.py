import asyncio
import logging
from contextlib import suppress

from bot.utils.launcher import process
from bot.config.config import settings

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)

def validate_settings():
    """
    Validate critical settings and log warnings if they are not set.
    """
    if not settings.API_ID or not settings.API_HASH:
        logger.warning("API_ID and API_HASH are not properly set. Please check your .env file.")

async def main():
    validate_settings()
    await process()

if __name__ == '__main__':
    with suppress(KeyboardInterrupt):
        asyncio.run(main())
