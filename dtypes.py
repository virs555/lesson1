a = 3
b = 4
c = a>b
print(c)

a = 'Привет'
b = "мир"
c = 2
c = '{}, {}{}!'.format(a,b,c)
print(c)

user = 'Python'
d = 'Привет, {name}!'.format(name=user)
print(d)

user2 = 'Python3'
e = f'Привет, {user2}!'
print(e)

a = 'Привет'.upper()
print(a)
b = 'МИР'.lower()
print(b)
c = 'python'.capitalize()
print(c)

a = '   Привет  '
b = a.strip() #Отрезает пробелы в начале и в конце
print(a)
print(b)

a = 'Прив3т т3б3'
print(a)
b = a.replace ('3', 'е')
print(b)
c = 'Прив3т т3б3'.replace('3', 'e')
print(c)

a = 'Привет приветЫ'.lower().replace('ы', '').capitalize() # 3 действия подряд
print(a)


a = 'learn.python.ru'
b = a.split('.')
print(b)
print(len(b))

a = 'learn python    ru'
b = a.split()
print(b)
print(len(b))

a = None
b = 0
print (a is None)
print (b is not None)

a = 2.0
b = '2.0'
c = 2
d = False
e = None
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

#name = input('Введите Ваше имя: ')
#print(f'Привет, {name}!')
#age = int(input('Сколько вам лет? '))
#age = 2020 - age
#print (f'Вы родились в {age} году')

print(bool('Пр'))
print(bool('0'))
print(bool(0))
print(str(None))