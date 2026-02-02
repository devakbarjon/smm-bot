from itertools import zip_longest
from typing import List, Union

from aiogram.types import InlineKeyboardMarkup, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder


def inline_builder(
        text: Union[str, List[str]],
        callback_data: Union[str, List[str]],
        sizes: Union[int, List[int]] = 1,
) -> InlineKeyboardMarkup:
    """
    Builds an inline keyboard using given text and callback data.

    :param text: Text for each button (single string or list of strings).
    :param callback_data: Callback data for each button (single string or list of strings).
    :param sizes: Number of buttons per row (single integer or list of integers, default is 1).
    :return: InlineKeyboardMarkup object.
    """
    builder = InlineKeyboardBuilder()

    if isinstance(text, str):
        text = [text]
    if isinstance(callback_data, str):
        callback_data = [callback_data]
    if isinstance(sizes, int):
        sizes = [sizes]

    if len(text) != len(callback_data):
        raise ValueError("Length of text and callback_data must be the same.")

    for txt, cb in zip_longest(text, callback_data):
        if txt is not None and cb is not None:
            builder.button(text=txt, callback_data=cb)
        else:
            raise ValueError("Mismatch in lengths of text and callback_data lists.")

    builder.adjust(*sizes)
    return builder.as_markup()


async def main_buttons(language: str) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    app_link = "https://smmly.pro/"
    support_link = "https://t.me/smmly_support"
    
    
    if language == 'ru':
        builder.button(
            text="🚀 Запустить",
            web_app=WebAppInfo(url=app_link)
        )

        builder.button(
            text="💭 Написать в поддержку",
            url=support_link
        )

    else:
        builder.button(
            text="🚀 Launch App",
            web_app=WebAppInfo(url=app_link)
        )

        builder.button(
            text="💭 Contact Support",
            url=support_link
        )
    
    builder.adjust(1)

    return builder.as_markup()