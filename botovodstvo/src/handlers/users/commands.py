from aiogram.types import ReplyKeyboardMarkup, InputFile, InputMediaPhoto

from loader import dp
from loader import db, bot
from aiogram import types
from keyboards import commands_default_keyboard, get_product_inline_keyboard, navigation_products_callback


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
    print("1234")
    if message.contact.user_id == message.from_user.id:
        await message.answer(text='Регистрация прошла успешно!')
        db.add_user(message.from_user.id, message.contact.phone_number)
    else:
        await message.answer(text='Увы(')

@dp.message_handler(text=['Список товаров'])
@dp.message_handler(commands=['products'])
async def answer_menu_command(message: types.Message):
    first_products_info = db.select_product_info(id=1)
    first_products_info = first_products_info[0]
    _, title, count, photo_path = first_products_info
    products_text = f"Название товара: {title}" \
                    f"\nКоличество товара: {count}"
    photo = InputFile(path_or_bytesio=photo_path)
    await message.answer_photo(photo=photo,
                               caption=products_text,
                               reply_markup=get_product_inline_keyboard())

@dp.callback_query_handlers(navigation_products_callback.filter(for_data='products'))
async def see_new_product(call: types.CallbackQuery):
    print(call.data)
    current_product_id = int(call.data.split(':')[-1])
    first_products_info = db.select_product_info(id=current_product_id)
    first_products_info = first_products_info[0]
    _, title, count, photo_path = first_products_info
    products_text = f'Название товара: {title}' \
                    f'\nКоличество товара: {count}'

    photo = InputFile(path_or_bytesio=photo_path)
    await bot.edit_message_media(media=InputMediaPhoto(media=photo,
                                                       caption=products_text),
                                 chat_id=call.message.chat.id,
                                 message_id=call.message.message_id,
                                 reply_markup=get_product_inline_keyboard(id=current_product_id))



