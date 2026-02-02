import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

from app.core.config import settings
from app.core.logging_config import setup_logging

from app.utils.set_bot_commands import set_default_commands


bot = Bot(
    token=settings.BOT_TOKEN.get_secret_value(),
    default=DefaultBotProperties(
        parse_mode=ParseMode.HTML
    )
)
dp = Dispatcher()


async def start_bot(bot: Bot) -> None:
    try:
        for dev in settings.DEVS:
            await bot.send_message(
                dev,
                'Bot started!'
            )
        bot_info = await bot.me()
        logging.info(f"Bot - @{bot_info.username} - {bot_info.id} - started!")
    except Exception as e:
        logging.error(f"Error starting bot: {e}", exc_info=True)


async def close_bot(bot: Bot) -> None:
    await bot.session.close()
    logging.info("Bot session closed.")


def setup_handlers(dp: Dispatcher):
    from app.handlers.users import commands, stars_payment
    dp.include_routers(
        commands.router,
        stars_payment.router
    )


def setup_middlewares(dp: Dispatcher, bot: Bot) -> None:
    """MIDDLEWARE"""
    from app.middlewares.throttling import ThrottlingMiddleware

    # Classic internal middleware for spam protection. Basic times between requests are 0.5 seconds.
    dp.message.middleware(ThrottlingMiddleware(slow_mode_delay=0.5))


async def main() -> None:
    try:
        setup_logging()
        setup_handlers(dp)
        setup_middlewares(dp, bot)
        dp.startup.register(start_bot)
        dp.shutdown.register(close_bot)
        await dp.start_polling(bot)
        await set_default_commands(bot)
    except Exception as ex:
        logging.error(f"Unhandled exception in main: {ex}", exc_info=True)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.info('Bot stopped!')
