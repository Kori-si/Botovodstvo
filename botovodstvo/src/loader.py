import sqlite3
from pathlib import Path

from aiogram import Bot, Dispatcher

from config import TOKEN
from db_api import Database

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
db_path = 'db_api/database/shop.db'
db = Database(db_path=db_path)
try:
    db.create_table_users()
except sqlite3.OperationalError as e:
    print(e)
except Exception as e:
    print(e)