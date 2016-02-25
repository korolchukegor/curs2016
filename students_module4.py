# -*- coding: utf-8 -*-
def func_4(s):
	col = 0
	for i in s:
		if i.find('р') > 0:
			col += 1
	print(col)
	return col