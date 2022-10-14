import db_api

db = db_api.Database('db_api/database/shop.db')

# db.add_product(id=1, title='Драко', count=32, photo=r'db_api/database/photo/drako.jpg')
# db.add_product(id=2, title='Мартин', count=12, photo=r'db_api/database/photo/martin.jpg')
# db.add_product(id=3, title='Люцифер', count=43, photo=r'db_api/database/photo/lyci.jpg')
# db.add_product(id=4, title='Блойз', count=54, photo=r'db_api/database/photo/bloiz.jpg')

print(db.select_all_products())

print(db.get_product_count())