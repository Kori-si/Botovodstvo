import sqlite3
from pathlib import Path

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import TOKEN
from db_api import Database

bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot)
db_path = Path('db_api/database/shop.db')
db = Database(db_path=db_path)
try:
    db.create_table_users()
except sqlite3.OperationalError as e:
    print(e)
except Exception as e:
    print(e)

try:
    db.create_table_products()
except sqlite3.OperationalError as e:
    print(e)
except Exception as e:
    print(e)

try:
    db.create_table_basket()
except sqlite3.OperationalError as e:
    print(e)
except Exception as e:
    print(e)