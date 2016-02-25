# -*- coding: utf-8 -*-
def func_3(s):
	try:
		num2 = int(input('Введите начало среза списка студентов\n'))
		num3 = int(input('Введите конец среза списка студентов\n'))
		if num3 <= len(s):
			print(s[num2 - 1:num3])
		else:
			print('Срез вне списка')
	except:
		print('некорректное значение')