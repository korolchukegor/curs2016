#-*- coding: utf-8 -*- 
import pickle
try: #Проверяем, пустой ли файл
	f = open('data.pickle', 'rb')
	data_new = pickle.load(f) #Если не пустой, то загружаем содержимое
	print(data_new)
except IOError:  #Если пустой, то создаём и заполняем новый
	data = {}
	a = int(input('Введите длину списка: '))
	for i in range(a):
		data[input('Введите ключ: ')] = input('Введите значение: ')
	f = open('data.pickle', 'wb')
	pickle.dump(data, f)

	print(data)

