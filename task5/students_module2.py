# -*- coding: utf-8 -*-
def func_2(s):
	num = int(input('Введите индекс студента'))
	try:
		s1 = s[num - 1]
		print(s1)
	except IndexError:
		print('Индекс не подходит')
		func_2(s)
