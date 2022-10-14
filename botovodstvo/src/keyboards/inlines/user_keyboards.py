from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inlines.callback_data import navigation_products_callback
from loader import db

def get_product_inline_keyboard(id: int = 1) -> InlineKeyboardMarkup:
    product_inline_keyoard = InlineKeyboardMarkup()
    left_id = id - 1
    right_id = id + 1
    if id == 1:
        btm = InlineKeyboardButton(text='>>>',
                                   callback_data=navigation_products_callback.new(
                                       for_data='products',
                                       id=right_id)
                                   )
        product_inline_keyoard.add(btm)
    elif id == db.get_product_count():
        btm = InlineKeyboardButton(text='<<<',
                                   callback_data=navigation_products_callback.new(
                                       for_data='products',
                                       id=left_id)
                                   )
    else:
        btm_left = InlineKeyboardButton(text='<<<',
                                        callback_data=navigation_products_callback.new(
                                            for_data='products',
                                            id=left_id)
                                       )
        btm_right = InlineKeyboardButton(text='>>>',
                                         callback_data=navigation_products_callback.new(
                                            for_data='products',
                                            id=right_id)
                                        )
        product_inline_keyoard.row(btm_left, btm_right)
    return product_inline_keyoard