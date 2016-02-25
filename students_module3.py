# -*- coding: utf-8 -*-
def func_3(s):
	num2 = int(input('Введите начало среза списка студентов\n'))
	num3 = int(input('Введите конец среза списка студентов\n'))
	print(s[num2 - 1:num3])
	return s[num2 - 1:num3]