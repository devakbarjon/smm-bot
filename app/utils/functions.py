def get_start_message(language: str | None, first_name: str) -> str:
    messages = {
        "en": f"Hello, {first_name}! Welcome to our SMM service bot. Use the menu below to navigate.",
        "ru": f"Привет, {first_name}! Добро пожаловать в наш бот SMM сервиса. Используйте меню ниже для навигации."
    }
    return messages.get(language, messages["en"])


def get_help_message(language: str) -> str:
    messages = {
        "en": (
            "If you have any questions or need assistance, feel free to reach out to our support team: @"
        ),
        "ru": (
            "Если у вас есть вопросы или вам нужна помощь, не стесняйтесь обращаться в нашу службу поддержки: @"
        ),
    }
    return messages.get(language, messages["en"])


def get_start_image(language: str | None) -> str:
    images = {
        "en": "http://telegraph.controller.bot/files/1733486741/AgACAgIAAxkBAAIKSWl_qzb1kAbVmX3bBqIJDg6airwYAAJRDWsbAAHLAAFIKUQ5u-QcR9UBAAMCAAN5AAM4BA",
        "ru": "http://telegraph.controller.bot/files/1733486741/AgACAgIAAxkBAAIKTWl_rHPMCqBt1s8S50OlO-ek_kj3AAJiDWsbAAHLAAFIAxDgGgvlOJ8BAAMCAAN4AAM4BA"
    }
    return images.get(language, images["en"])