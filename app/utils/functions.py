from pathlib import Path

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
    base = Path(__file__).resolve().parents[1] / "data" / "images"
    images = {
        "en": base / "smm-banner-eng.png",
        "ru": base / "smm-banner-ru.png",
    }
    return str(images.get(language, images["en"]))