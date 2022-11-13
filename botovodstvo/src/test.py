import db_api

db = db_api.Database('db_api/database/shop.db')

db.add_product(id=1, title='Драко', count=32, photo_path=r'db_api/database/photo/drako.jpg')
db.add_product(id=2, title='Мартин', count=12, photo_path=r'db_api/database/photo/martin.jpg')
db.add_product(id=3, title='Люцифер', count=43, photo_path=r'db_api/database/photo/lyci.jpg')
db.add_product(id=4, title='Блойз', count=54, photo_path=r'db_api/database/photo/bloiz.jpg')

print(db.select_all_products())
print(db.select_all_basket())

print(db.get_product_count())
user_basket = ''
current_product_id = '2'
current_count = 10
user_basket = [product_data.split(':') for product_data in user_basket.split()]
print(user_basket)
for i in range(len(user_basket)):
    product_id, product_count = user_basket[i]
    if current_product_id == product_id:
        user_basket[i][1] = str(int(product_count) + current_count)
        break
else:
    user_basket += [[current_product_id, str(current_count)]]
print(user_basket)
user_basket = ' '.join([':'.join(dbl) for dbl in user_basket])

print(user_basket)