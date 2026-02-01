import logging
from aiogram import Router
from aiogram.types import Update
from aiogram.exceptions import TelegramBadRequest

from app.core.config import settings

error_router = Router()
logger = logging.getLogger(__name__)


@error_router.errors()
async def errors_handler(update: Update, exception: Exception):
    """
    Handler for all errors.
    """
    logger.error("Cause exception: %s", exception, exc_info=True)

    if isinstance(exception, TelegramBadRequest):
        logger.error("TelegramBadRequest: %s", exception)
        return

    # Send error notification to developers
    if settings.DEVS:
        for dev_id in settings.DEVS:
            try:
                await update.bot.send_message(
                    chat_id=dev_id,
                    text=f"An unhandled error occurred:\n\n`{exception}`\n\nUpdate: `{update.model_dump_json(indent=2)}`",
                    parse_mode="Markdown"
                )
            except Exception as e:
                logger.error("Failed to send error notification to developer %s: %s", dev_id, e)

    logger.error("Update: %s \n%s", update.model_dump_json(indent=2), exception, exc_info=True)
