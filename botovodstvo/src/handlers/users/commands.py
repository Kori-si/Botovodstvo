from aiogram.types import ReplyKeyboardMarkup

from loader import dp
from aiogram import types
from keyboards import commands_default_keyboard


@dp.message_handler(text=['Привет', 'Начать'])
@dp.message_handler(commands='start')
async def answer_start_command(message: types.Message):
    await message.answer(text=f"Hi!"
                              f"\n Like",
                         reply_markup=commands_default_keyboard)

@dp.message_handler(commands='menu')
async def answer_start_command(message: types.Message):
    await message.answer(text=f"Главное меню",
                         reply_markup=commands_default_keyboard)

@dp.message_handler(text=['О нас'])
@dp.message_handler(commands=['info'])
async def process_hi6_command(message: types.Message):
    await message.reply("Мы интернет магазин")

@dp.message_handler(text=['Скрыть меню'])
@dp.message_handler(commands=['menu'])
async def answer_info_command(message: types.Message):
    await message.answer(text='Чтобы вернуть меню, воспользуйтесь командой /menu',
                         reply_markup=ReplyKeyboardMarkup)

@dp.message_handler(content_types=['contact'])
async def answer_contact_command(message: types.Message):
    if message.contact.user_id == message.from_user.id:
        await message.answer(text='Регистрация прошла успешно!')
    else:
        await message.answer(text='Увы(')

@dp.message_handler(content_types=['location'])
async def answer_location_command(message: types.Message):
    if message.location.user_id == message.from_user.id:
        await message.answer(text='опа!')
    else:
        await message.answer(text='хуй')