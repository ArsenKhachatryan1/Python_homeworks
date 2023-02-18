# Упражнение 85. Вычисляем длину гипотенузы
# from math import sqrt
# def myfunc():
#     a = int(input('Enter side 1:  '))
#     b = int(input('Enter side 2:  '))
#     c = sqrt((a**2+b**2))
#     return c
# print(myfunc())



# Упражнение 86. Плата за такси
# def func_taxi(km):
#     himn_tarif = 4
#     poxvox_tarif = 0.25/0.14
#     gin = km * poxvox_tarif +himn_tarif
#     return round(gin, 2)
# dist = float(input('Input distance:  '))
# print(func_taxi(dist))



# Упражнение 87. Расчет стоимости доставки
# def dostavka(qanak:int):
#     price =10.95
#     if qanak <= 0:
#         price = 0
#         return price
#     else:
#         for i in range(qanak-1):
#             price += 2.95
#         return round(price, 2)
# a = int(input('Enter quantity:  '))
# print(dostavka(a))



# Упражнение 89. Переводим целые числа в числительные
# def chisl(num):
#     Ordinal = ['First', 'Second', 'Third', 'Fourth', 'Fifth', 'Sixth', 'Seventh', 'Eighth', 'Ninth', 'Tenth', 'Eleventh', 'Twelfth']
#     if num< 1 or num > 12:
#         quit()
#     for i in range(1,13):
#         i = Ordinal[num-1]
        # return i
# for i in range(1,13):
#     print(i , chisl(i))



# Упражнение 90. Двенадцать дней Рождества
# for i in range(1,13):
#     song = f'On the {chisl(i)} day of Christmas\nmy true love sent to me:\nA partridge in a pear tree.'
#     print(song)
#     print('And a partridge in a pear tree.')
#     print()


# Упражнение 91. Григорианский календарь в порядковый
# def func_day(day:int, month:int, year:int):
#     list1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if year%4 == 0:
#         list1[1]=29
#     day_ind = day
#     for i in range(month-1):
#         day_ind += list1[i]
#     return day_ind
# day = int(input('Enter day: '))
# month = int(input('Enter month:  '))
# year = int(input('Enter year:  '))
# print(func_day(day, month, year))




