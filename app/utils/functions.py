def get_start_message(language: str | None, first_name: str) -> str:
    messages = {
        "en": (
            f"<b>🚀 Welcome to SMMLY, {first_name}!</b>\n\n"
            "Boost your social media in seconds: followers, views, likes, and more.\n\n"
            "<b>Automation. Speed. Reliability.</b>\n\n"
            "🔹 Telegram | Instagram | YouTube | TikTok and etc.\n"
            "🔹 24/7 Support\n"
            "🔹 Bonuses for activity\n\n"
            "<b>👉 Start now — press '🚀 Launch App'!</b>"
        ),
        "ru": (
            f"<b>🚀 Добро пожаловать в SMMLY, {first_name}!</b>\n\n"
            "Прокачай свои соцсети за секунды — подписчики, просмотры, лайки и многое другое.\n\n"
            "<b>Автоматизация. Скорость. Надёжность.</b>\n\n"
            "🔹 Telegram | Instagram | YouTube | TikTok и т.д.\n"
            "🔹 Поддержка 24/7\n"
            "🔹 Бонусы за активность\n\n"
            "<b>👉 Начни прямо сейчас — нажми «🚀 Запустить»!</b>"
        )
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
        "en": "http://telegraph.controller.bot/files/1733486741/AgACAgIAAxkBAAIKYGmAgyM6b2Sa_WjWXm-5vElSqb8DAAIFD2sb4BgBSFv87hDUR-ffAQADAgADeQADOAQ",
        "ru": "http://telegraph.controller.bot/files/1733486741/BQACAgIAAxkBAAIKXGmAgwvi11lo-GzVfVVm4CosKRpwAAL6jQAC4BgBSHh_Z7QYAq4TOAQ"
    }
    return images.get(language, images["en"])