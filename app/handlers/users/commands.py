from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile

from app.filters.chat_filters import TypeFilter
from app.keyboards.users.inline import main_buttons
from app.utils.functions import get_help_message, get_start_message, get_start_image

router = Router()


@router.message(CommandStart(), TypeFilter('private'))
async def cmd_start(message: Message):
    language = message.from_user.language_code
    first_name = message.from_user.first_name

    start_message = get_start_message(language, first_name)
    buttons = await main_buttons(language)

    await message.answer_photo(
        photo=FSInputFile(get_start_image(language)),
        caption=start_message,
        reply_markup=buttons
    )


@router.message(Command("help"), TypeFilter("private"))
async def cmd_help(message: Message):
    language = message.from_user.language_code
    
    await message.answer(
        text=get_help_message(language)
    )