# 63  Среднее значение
# num = int(input('Enter a number:  '))
# sum = num
# count = 0
# if num ==0:
#     print('Error')
# else:
#     while num != 0:
#         num = int(input('Enter a number:  '))
#         sum += num
#         count+=1
    
#     print(f'Sum of the numbers = {sum}')
#     print(f'Count of the numbers = {count}')
#     print(f'Average of the numbers = {int(sum/count)}')


# 64  Таблица со скидками
# prices = 4.95, 7.5, 88.54, 12.45
# for i in prices:
#     print(f'${i} - 60% = ${round(i - (i * 0.6), 2)}')


# 65  Таблица соотношения температур
# for i in range(0, 101, 10):
#     print(f'{i}(C) ---> {i * 9/5 + 32}(F)')


# 66  Никаких центов
# price = (input('Enter the price:  '))
# sum_ = 0
# while price != '':
#     sum_ += float(price)
#     price = (input('Enter the price:  '))
# print(f'Total of price = {sum_}')
# if sum_ % 5 < 2.5:
#     sum_ -= sum_ % 5
# else:
#     sum_ += (5 - sum_ % 5)
# print(f'Your payment = {sum_}')


#  67  Найти периметр многоугольника
# first_X = x0 = int(input('Enter X:  '))
# first_Y = y0 = int(input('Enter Y:  '))
# perimetr = 0

# while True:
#     x1 = input('Enter X:  ')
#     if x1 == '':
#         break
#     else:
#         x1 = int(x1)
#         y1 = int(input('Enter Y:  '))
#         perimetr += ((x1 - x0)**2 + (y1 - y0)**2)**0.5
#         x0 = x1
#         y0 = y1
# perimetr += ((x0 - first_X)**2 + (y0 - first_Y)**2)**0.5
# print(f'Perimetr = {perimetr}')




# 68  Средняя оценка
# grade = input('Enter num:  ')
# total = 0
# count = 0
# while grade != '':
#     if grade == 'A+':
#         result = '4.0'
#     elif grade == 'A':
#         result = '4.0'
#     elif grade == 'A-':
#         result = '3.7'
#     elif grade == 'B+':
#         result = '3.3'
#     elif grade == 'B':
#         result = '3.0'
#     elif grade == 'B-':
#         result = '2.7'
#     elif grade == 'C+':
#         result = '2.3'
#     elif grade == 'C':
#         result = '2.0'
#     elif grade == 'C-':
#         result = '1.7'
#     elif grade == 'D+':
#         result = '1.3'
#     elif grade == 'D':
#         result = '1.0'
#     elif grade == 'F':
#         result = '0'
#     else:
#         result = 'Error'
#     grade = input('Enter num:  ')
#     total = total + float(result)
#     count += 1
# print(f'Total grade = {total}')
# print(f'The average grade = {round(total/count , 2)}')


# 69  Билеты в зоопарк
# age = (input('Your age:  '))
# total = 0
# while age != '':
#     age = int(age)
#     if age <= 2:
#         price = 0
#     elif 2<age<=12:
#         price = 14
#     elif age>=65:
#         price = 18
#     elif 12<age<65:
#         price = 23
#     age = (input('Your age:  '))
#     total += price
# print(f'Total amount for payment = {float(round(total , 2))} $')



# 70  Биты четности
# count = 0
# while True:
#     summ_of_1 = 0
#     bit = input('Enter 8 bit: ')
#     if bit == '':
#         break
#     else:
#         if len(bit) != 8:
#             count += 1
#             if count == 1:
#                 print('Enter 8 BIT ARA!!!!')
#             elif count == 2:
#                 print('Du ches jogum vor pti 8 bit gres hesa kanjatem demqit')
#             elif count == 3:
#                 print('Hajox')
#                 break
#         else:
#             count = 0
#             for i in bit:
#                 if i == '1':
#                     summ_of_1 += 1
#             if summ_of_1 % 2 == 0:
#                 print('Zuyg bit')
#             else:
#                 print('Kent bit')  



# 71  Приблизительное число π
# pi = 3
# n1 = 2
# n2 = 3
# n3 = 4
# i = 0
# while i < 15:
#     if i % 2 == 0:
#         pi += (4 / (n1 * n2 * n3))
#     else:
#         pi -= (4 / (n1 * n2 * n3))
#     n1, n2 ,n3 = n3, n3 + 1, n3 + 2
#     i += 1
# print(pi)



# 72/1  Игра Fizz-Buzz
# num = int(input('Enter a number:  '))
# count = 1
# while num < 100:
#     num = int(input('Enter a number:  '))
#     count+=1
#     if num%3==0 and num%5==0:
        
#         result = 'Fizz-Buzz'
#         print(result)
#     elif num%5 ==0:
#         result = 'BUZZ'
#         print(result)
#     elif num%3==0:
#         result = 'Fizz'
#         print(result)
#     else:
#         print(count)
    


# 72/2  Игра Fizz-Buzz
# user_count = 12
# for i in range(1, 101):
#     if user_count == 1:
#         print('GAME OVER')
#         break
#     else:
#         print(i)
#         user = input('Enter Fizz/Buzz/Fizz-Buzz/ : ')
#         if (i % 3 and i % 5 == 0) and user == 'Fizz-Buzz':
#             print('GOOD', user_count)
#         elif i % 3 == 0 and user == 'Fizz':
#             print('GOOD', user_count)
#         elif i % 5 == 0 and user == 'Buzz':
#             print('GOOD', user_count)
#         elif (i % 3 != 0 or i % 5 != 0) and user == '':
#             print('GOOD', user_count)
#         else:
#             print('VATA SHAT VATA!!')
#             user_count -= 1
#             print(user_count)
# else:
#     print('Mnac', user_count)



# 73 Код Цезаря xary kisat
# text = input('Enter your text:  ')
# lag = int(input('Enter lag:  '))
# if lag>25:
#     print('Entered Wrong lag: ')
# else:
#     text_new = ''
#     for i in text:
#         if i.isalpha():
#             if 97<=ord(i)<=122:
#                 if ord(i)+lag>122:
#                     text2 = ord(i)-23
#                     text_new = text_new + chr(text2)
#                 else: 
#                     text2 = ord(i) + lag
#                     text_new = text_new + chr(text2)
#             elif 65<=ord(i)<=90:
#                 if ord(i)+lag>90:
#                     text2 = ord(i)-23
#                     text_new = text_new + chr(text2)
#                 else: 
#                     text2 = ord(i) + lag
#                     text_new = text_new + chr(text2)    
#         else:
#             text_new = text_new + i
#     print(text_new, end = '')



# 74  Квадратный корень
# num =int(input('Enter mnumber:  '))

# armat =num/2
# while armat*armat-num>10**-12:
#     armat = (num/armat+armat)/2
# print(armat)




# 75  Палиндром или нет?
# text = input('Enter the text:  ').lower()
# text = text.replace(' ', '')
# if text == text[::-1]:
#     print('Palindrom')
# else:
#     print('Not palindrom')


# Упражнение 77. Таблица умножения
print('       1    2    3    4    5    6    7    8    9   10')
for i in range(1 ,11):
    print(f'{i:>3}', end=' ' )
    for j in range(1 , 11):
        j = i*j
        print(f'{j:>4}', end=' ')
    print()





# 78. Гипотеза Коллатца
# num = int(input('Enter number:  '))
# while num !=1:
#     if num%2 == 0:
#         line = num/2
#         num = line
#     elif num%2 == 1:
#         line = num*3 + 1
#         num = line
#     print(int(line), end =', ')
    



# 79  Наибольший общий делитель
# num1 = int(input('Enter number 1:  '))
# num2 = int(input('Enter number 2:  '))
# if 0<num1<num2:
#     x = num1
#     while num1%x!=0 or num2%x!=0:
#         x-=1
#     print(x)
# elif 0<num2<num1:
#     x = num2
#     while num1%x!=0 or num2%x!=0:
#         x-=1
#     print(x)
# elif num1<0 or num2<0:
#     print('Error')
# else:
#     print(num1)


# 80  Простые множители
# num = int(input('Enter number:  '))
# factor = 2
# while factor <= num:
#     if num%factor == 0:
#         print(factor)
#         num = int(num/factor)
#     else:
#         factor +=1
        
     

       
# 81_1  Двоичное число в десятичное
# a = input('Enter a number:  ')
# e= a[::-1]
# c = 0
# d = 0
# for i in range(0,len(a)):
#     b =(2**c)*int((e[i]))
#     c+=1
#     d+=b
# print(f'{a}₂ = {d}')

    
# 81-2  Двоичное число в десятичное
# a = input('Enter a number:  ')
# c = len(a)-1
# d = 0
# if ('0' in a and '1' in a) or '1' in a:
#     for i in range(0,len(a)):
#         b =(2**c)*int((a[i]))
#         c-=1
#         d+=b
#     print(f'{a}₂ = {d}')
    
# else:
#     print('Error')



# 82 Десятичное число в двоичное
# num_10 = int(input('Enter number:  '))
# num_2 = ''
# # num = num_2[::-1]
# while num_10 != 0:
#     num_2 += str(num_10%2)
#     num_10 = num_10//2
# print((num_2)[::-1])




# 83  Максимальное число в последовательности
# from random import randrange

# a = (randrange(1,100))
# b = a
# c = 0
# count = 0
# while c !=10:
#     c+=1
#     a = (randrange(1,100))
#     if b < a:
#         b = a
#         count +=1
#         print('Max is changed')
#     print(a,)
# print(f'Total changes = {count}')
# print(f'Max number in range = {b}')




# 84. Подбрасываем монетку
# import random

# for i in range(10):
#     s = ''
#     while True:
#         x = random.choice('OP')
#         s += x
#         if len(s) < 3:
#             continue
#         else:
#             if s[-1] == s[-2] == s[-3]:
#                 print(s, len(s))
#                 break
#             else:
#                 continue




