# -*- coding: utf-8 -*-
s = []
def func_1():
	i = 0
	global s
	stud = int(input('Введите количество студентов:'))
	for i in range(stud):
		s.append(input('Введите имя и вамилию студента:'))
	print(s)
	return s