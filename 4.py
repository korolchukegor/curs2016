#Функции
def newfunc():
    def add(x, y):
	    return x + y #складываем и возвращаем значение
    return add
#print(add(20, 5))
print(newfunc()) #любые объекты

def func():
	pass #Задание пустого блока кода
print(func())

import sys, os

def sumfunc(lst):
	summa = 0
	for a in lst:
		summa += a
	return summa

lst = {2, 4, 6, 9 , 2, 4}
ret = sumfunc(lst)
print(ret)

def some_file_work(text):
    f = open('rrr', 'a')
    s = "{}\n".format(text) #Вставляем значение переменной text вместо{}
    f.write(s)
    f.close()


some_file_work("hello")
some_file_work('my name')
some_file_work('is')

def func(a, b, c = 2):
	return a + b + c

#ret = func(10, 4)
ret = func(a = 2, b = 4, c = 3)
print(ret)

def func(*args): #можно вставлять аргументы
	return args

func()
func(1, 2, 3)

def debug(*args): #tuple
    print('args len:', len(args))
    for a in args:
    	print(a)
    return args
debug(1, 3, 5)
print(debug(1,3,5))

def func(x, y, c = 2, *args, **kwargs):
	if kwargs['password'] == 'sdfgsdf':
	    print(kwargs['name'], x, y)
	    #print(kwargs['age'])
	return kwargs


func(10, 20, name = 'Ivan', password = 'sdfgsdf')

'''Функция рисования. Первый аргумент - длина линии, вторым - длина линии. '''

def func(dlina, shirina, znak):
	line = (znak * dlina + "\n") * shirina
	print(line)
    

func(20, 3, 'z')

#lambda

add = lambda x, y: x + y
print(add(10, 20))
print((lambda x, y: x + y)(10, 20)) #Можно и так


lst = [
	['Ivan', 'Novikov'],
	['Will', 'Smith'],
	['Michael', 'Jackson']
]
lst.sort(key = lambda lst2: lst2[1])
print(lst)
# def sort(key=lambda lst2: lst2[1]):
#	for lst2 in lst:
#		a = key(lst2)

print((lambda name, surname: len(name) / len(surname))(lst[0][0], lst[0][1]), lst[0][0], lst[0][1])

koef = lambda lst: [len(a[0]) / len(a[1]) for a in lst]
print(koef(lst))

a, b = ['hello', 'buy'] # распаковка
print(a, b)
# git clone https://egorkorolchuk@github.com/korolchukegor/curs2016.git #-получаем репозиторийв первый раз
# git status # Проверка состояния репозтитория
# git commit -a - m "Комментарий к коммиту"#
# git push # заливаем коммит
# git add -i #