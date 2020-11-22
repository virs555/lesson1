phones = ['iPhone Xs', 'Samsung 10s', 'Xiaomi Mi8', 'iPhone Xs'] #Список 21 стр

product = {
    'name': 'iPhone Xs',
    'stock': 5,
    'price': 65000.0
}

product['stock']=10 # Меняем значение
product['memory']=64 # Добавляем новую пару


print(product)
print(len(product))
print(product['memory']) # Выводим отдельный элемент (только существующий)
print(product.get('name', 'iPhone 3g')) # Выводим отдельный элемент
print(product.get('Discount', 0)) # Выводим несуществующий элемент None или указываем значение по умолчанию
del product['stock'] #Удаляем элемент (только существующий)
print(product)

product['recomend'] = phones # Добавляем список в словарь
print(product)

print(product['recomend']) #Получаем список из словаря
print(product['recomend'][1]) #Получаем элемент списка из словаря
product['recomend'].append('iPhone 12')
print(product)

#Cписок словарей

stock = [
    {'name': 'iPhone Xs Plus', 'stock': 24, 'price': 65432.1, 
     'recomended': ['Samsung Galaxy S10', 'iPhone Xs']},
    {'name': 'Samsung Galaxy S10', 'stock': 8, 'price': 50000.0, 'discount': 5000},
    {'name': 'Xiaomi Mi8', 'stock': 42, 'price': 38000.5}
]

print(stock)

print(stock[0]['name']) # Выводим элемент
stock[0]['price'] = stock[0]['price']+10000 # Прибавляем к цене 0-го элемента
print(stock)
stock[0]['price']+=10000 # Прибавляем к цене 0-го элемента (простая запись)
print(stock)
print(stock[0]['recomended'][0]) # Обращение к элементам