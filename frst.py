#a = int(input('Введите a '))
#if not 1 < a < 20:
#    print('сегодня')
#else:
#    print("завтра")

#names = ['Aleks', 'Masha', 'Misha'] #создание списка
#for name in names:
#    print(name)

"""k = 1
while True:
    k += 1
    print(k)

    if k == 20:
        break"""

"""k = 1
while True:
    print(1)"""

"""
# -*- coding: utf-8 -*-
import os

lst = os.listdir('/Library/Frameworks/Python.framework/Versions/3.5/bin/')
for i in lst:
    print(i)
"""
#../../ - два раза выйти из директории
#import random
#help (random)



#import random
#print(random.randint(1,13))
#print(a)


f = open('/users/ekaterinakarachentseva/Documents/python lessons/ttt', 'w') #  открыли файл на чтение - ограниение оперативка
#print(f.read()) # читаем весь файл
#f=open('ttt', 'w')
f.write("""some text python
sfcvdf

python     python""")
f.close()
"""
f=open('ttt')
print(f.read())"""


#x,y = 4,5

#print(pow(3,4,5)) прочитать про divmod и pow

#print(0xff) - 16 ричная система

#print(int("1001",2)) - указывается двоичная система и переводится в десятиричную


#print(sum([1,2,3,4,5]))

#print(round(abs(3 - 7.4)))

"""y = complex(3,4)
print(y)"""
#print(0.1+0.1+0.1+0.1+0.1+0.1+0.1+0.1+0.1+0.1)
#print(3 ** 1000+0.1)- пример особенностей пайтона

#странное округление
#print(round(3.5),round(4.45, 1),round(2.75, 1))

"""from fractions import Fraction
f = Fraction(1,2)
f2 = Fraction(2,3)
print(f + f2)
"""
"""
from decimal import Decimal
print(Decimal('0.11'))
"""

'''
import math
print(math.pi, math.sqrt(9))
'''

#import random
#print(random.random())



# Строки


#s = 'это строка'
#m = '''многострочный
#
#текст'''
#print(s, m)
#print(type(s) is str) #проверяем, строка ли

#конец файла

