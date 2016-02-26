# -*- coding: utf-8 -*-
from itertools import groupby
def func_5(s):
	fullname = 0
	names = []
	s1 = set()
	unicnames = []
	grouplist = []
	for fullname in s:
		Name, Surname = fullname.split()
		names.append(Name)
	for Name in names:
		if names.count(Name) >= 2:
			s1.add(Name)
			s2 = list(s1)
	for Name in s2:
		for fullname in s:
			if Name in fullname:
				grouplist.append(fullname.split())
	for key, group in groupby(grouplist, lambda x: x[0]):
		print("Группа", key, ":\n")
		for grouplist in group:
			print(key, grouplist[1])
		print("\n")
   