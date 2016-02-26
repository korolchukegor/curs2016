#-*- coding: utf-8 -*- 
import pickle
try: #Проверяем, пустой ли файл
	f = open('data.pickle', 'rb')
	data = pickle.load(f) #Если не пустой, то загружаем содержимое
	f.close()
	print(data)
except IOError:  #Если пустой, то создаём и заполняем новый
	data = {}
	a = int(input('Введите количество треков на диске: '))
	for i in range(a):
		data[input('Введите название группы: ')] = input('Введите название композиции: ')
	f = open('data.pickle', 'wb')
	pickle.dump(data, f)
	f.close()
	print(data)

#Фильтрация
find = input('Введите название группы для поиска:')
print(find)
print(data.get(find))
