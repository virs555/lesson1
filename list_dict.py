phones = ['iPhone Xs', 'Samsung 10s', 'Xiaomi Mi8', 'iPhone Xs'] #Список

print(phones)

phones_count = len(phones)
print(phones_count)

phones.append('iPhone 6') # append добавляет элемент в конец списка
print(phones)

print(phones.count('iPhone Xs')) # count считает кол-во указанных элементов в списке

print(phones.count('iPhone 9'))

print(phones[0]) # вызов элемента списка

print(phones[1:3]) # срез списка

print(phones[-1]) # Вывод последнего элемента списка

print(phones[:2]) # вывод элементов от начала до 2

print(phones.index('Samsung 10s')) # Узнаем индекс элемента

phones.sort() # сортировка списка, только однотипные
print(phones)

print('iPhone Xs' in phones) # проверка совпадения

del phones [-1] #Удаление элемента по индексу
print(phones)

phones.remove('iPhone Xs') #Удаление элемента по названию, первое вхождение
print(phones)