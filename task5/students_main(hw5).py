# -*- coding: utf-8 -*-
import students_module1, students_module2, students_module3, students_module4, students_module5
s = ['Егор Корольчук','Андрей Андреев','Данила Савицкий','Денис Цыганов','Дмитрий Синицкий','Настя Захарина','Александр Бутаков','Юрий Рябов','Павел Логинов','Ишхан Никогосян','Андрей Лекарев','Виталий Маковкин','Антон Кожанов','Кирилл Сухарев','Vensder Fainas','Жека Fm','Daniil Ershov','In Effect','Алексей Иванов','Денис Нестеренко', 'Андрей Фадеев']
ask = int(input('Введите номер пункта задания:\n'))
if ask == 1:
	students_module1.func_1()

elif ask == 2:
	students_module2.func_2(s)
elif ask == 3:
	students_module3.func_3(s)
elif ask == 4:
	students_module4.func_4(s)
elif ask == 5:
	students_module5.func_5(s)
else:
	print('У задачи было только 5 пунктов')
