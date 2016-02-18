# -*- coding: utf-8 -*-
s = []
i = 0
stud = int(input('Введите количество студентов:'))

for i in range(stud):
    s.append(input('Введите имя и вамилию студента:'))
print(s)
#Пункт 2
#s = ['Егор Корольчук','Андрей Андреев','Данила Савицкий','Денис Цыганов','Дмитрий Синицкий','Настя Захарина','Александр Бутаков','Юрий Рябов','Павел Логинов','Ишхан Никогосян','Андрей Лекарев','Виталий Маковкин','Антон Кожанов','Кирилл Сухарев','Vensder Fainas','Жека Fm','Daniil Ershov','In Effect','Алексей Иванов','Денис Нестеренко', 'Андрей Фадеев']
print('Введите индекс студента')
num = int(input())
print(s[num - 1])
#Пункт 3
num2 = int(input('Введите начало среза списка студентов'))
num3 = int(input('Введите конец среза списка студентов'))
print(s[num2 - 1:num3])
#Пункт 4
col = 0
for i in s:
        if i.find('р') > 0:
                col += 1
print(col)
#Пункт 5
"""fullname = 0
names = []
names2 = []
s1 = set()
group = []
names1 = []
i = 0
for fullname in s:
    Name = fullname[:fullname.find(' ')] #Выделяем имена
    names.append(Name) #Список имен
    for Name in names:
        while Name != names[i:i + 1]:
        i += 1
        print(Name)


for Name in names:    
    if names.count(Name) >= 2:
        if Name in names:
            s1.add(Name)
            s2 = list(s1)
for Name in s2:
    for fullname in s:
        if Name in fullname:
            group.append(fullname)

print(group)"""
#Выводит список студентов, имена которых совпадают



