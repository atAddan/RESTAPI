import requests

# get запрос на вывод всех продуктов, меняем 0 на id продукта и получаем выбранный продукт
res = requests.get("http://127.0.0.1:3000/api/products/0")

# delete запрос на удаление выбранного продукта, меняем 1 на id продукта и удаляем выбранный продукт 
#res = requests.delete("http://127.0.0.1:3000/api/products/1")

# post запрос на добавление одной записи, 4 - новый id для добавления, так же указывается цена и название добавляемого продукта
#res = requests.post("http://127.0.0.1:3000/api/products/4", json={'name':'Микроволновка', 'price': 38})

# put запрос на изменение одной записи, 2 - id для изменения, так же указывается цена и название добавляемого продукта
#res = requests.put("http://127.0.0.1:3000/api/products/2", json={'name':'Чайник', 'price': 4})

print(res.json())