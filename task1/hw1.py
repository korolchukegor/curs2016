# -*- coding: utf-8 -*-
import os
source = '/Users/egorkorolchuk/Documents/python/test'
lst = os.listdir(source)
linect = 0                                      #количество упоминаний слова в строках
s = []                                          #список, куда будут добавляться файлы с упоминанием слова
for i in lst:                                   #перебираю файлы в папке
    if i != '.DS_Store' and i != '.idea':       #исключаю файлы в unicode
        f = open(i)
        for line in f:                          #читаю файлы построчно
                linpyth = line.count('python')  #проверяю строки на количество слов "python"
                if linpyth > 0:                 #если в строке есть слово, то +1 к счетчику
                        linect += 1
        if linect != 0:                         #если в строках есть python, то добавить название в файла в список s
                s.append(i)
result = open('result.txt', 'w')
result.write('''Список всех файлов, где есть слово "Python":\n''' + str(s) + '''\nСлово "Python" упоминается '''+ str(linect) + ''' раз!''')






