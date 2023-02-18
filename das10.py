# ----------------------------------7.For: циклы со счётчиком. Часть 1--------------------------------
# 1. Должники
# n = 0
# for i in range(1,11):
#     bank = int(input('Մուտքագրեք բանկի հաճախորդի համարը:  '))
#     if bank>0 and bank%2 == 0:
#         n += 1
# print(f'Բանկի վստահելի հաճախորդների ընդհանուր թիվը կազմում է {n}')



# 2. Посчитай чужую зарплату
# t_salary = 0
# for i in range(1,13):
#     m_salary = int(input('Մուտքագրեք ձեր ամսական աշխատավարձը:  '))
#     t_salary += m_salary
# print(f'Ձեր տարեկան միջին աշխատավարձը կազմում է {t_salary/12} դրամ')




# 3. Факториал
# number = int(input('Enter the number:  '))
# factorial = 1
# for i in range(1,number+1):
#     factorial *=i
# print(f'Factorial of the number {number} = {factorial}')



# 4. Успеваемость в классе
# n = int(input('Մուտքագրեք աշակերտների քանակը։  '))
# ger = 0
# harv = 0
# bav = 0 
# for i in range(1, n+1):
#     grade = int(input('Մուտքագրեք աշակերտի գնահատականը։  '))
#     if grade == 5:
#         ger +=1
#     elif grade == 4:
#         harv += 1
#     elif grade == 3:
#         bav += 1
# print(f'Գերազանցիկ աշակերտների քանակը հավասար է {ger}\nՀարվածային աշակերտների քանակը հավասար է {harv}\nԲավարար աշակերտների քանակը հավասար է {bav}')



# 5. Отрезок
# a = int(input('Մուտքագրեք առաջին թիվը:  '))
# b = int(input('Մուտքագրեք երկրորդ թիվը:  '))
# sum3 = 0
# count3 = 0
# for i in range(a, b+1):
#     if i%3 == 0:
#         sum3 += i
#         count3 +=1
# print(f'3—ի բաժանվող ընդհանուր թվերի միջին թվաբանականը հավասար է {sum3/count3}')        


# 6. Замечательные числа

# for i in range(10 , 100):
#     i = str(i)
#     if (int(i[0]) * int(i[1])) * 3 == int(i):
#         print(i)


# 7. Пропавшая карточка
# n = int(input('Enter the count of card: '))
# sum_of_card = 0
# for i in range(1, n + 1):
#     sum_of_card += i
# new_sum = 0
# for i in range(1, n):
#     card = int(input('Enter card number: '))
#     new_sum += card
# print(sum_of_card - new_sum)



# -----------------------------------------------8.For: циклы со счетчиком. Часть 2---------------------------------
# 1. Космическая еда
# month = 0
# reserv = 100
# for i in range(0 , 100, 4):
#     month += 1
#     month = int(input('Enter month:  '))
#     reserv -= 4
#     print(f'{month} ամիս հետո պաշարը կկազմի {reserv}կգ')



# 2. Долги
# debtor = int(input('Մուտքագրեք պարտապանների ընդհանուր քանակը:  '))
# t_dolg = 0
# for i in range(0 , debtor , 5):
#     dolg = int(input(f'Պարտապան No {i}\nՊարտքը կազմում է - '))
#     t_dolg += dolg
# print(f'Պարտքի ընդհանուր գումարը կազմում է - {t_dolg}')


# 3. Таймер для микроволновых печей
# ---------------


# 4. Среднее на отрезке
# a = int(input('Մուտքագրեք շարքի առաջին թիվը:  '))
# b = int(input('Մուտքագրեք շարքի առաջին թիվը:  '))
# c = int(input('Մուտքագրեք բաժանարարը:  '))
# print(f'{a}-ից մինչև {b} ընկած թվերի շարքում {c}-ին բաժանվում են հետևյալ թվերը')
# for i in range(a , b+1):
#     if i%c == 0:
#         print(i)


# 5. Функция 2
# ------------




# 6. Письмо
# a = float(input('Մուտքագրեք նամակի չափերը:  '))
# b = 0
# for i in range(1 , int((a+2)//1)):
#     if a>12:
#         a= a/2
#         b+=2
# print(f'Նամակը պետք է ծալվի {b} անգամ')



# 7. Стипендия
# educational_grant = int(input('Input educational_grant:  '))
# expenses = int(input('Input expenses:  '))
# from_par = 13000
# for i in range(2,11):
#     expenses += expenses*0.03
#     from_par += expenses
# print(f'Petq a vercnel {from_par- educational_grant*10} gumar')



# 8. Сумма ряда
# ----------------




# 9. Выражение
x = int(input('Enter number:  '))
res1 = 1
res2 = 1
a = 1
b = 2
count = 0
for i in range(1 , 7):
    res1*= (x-a)
    a = 2*a+1
    res2 *= (x-b)
    b = 2*b
print(res1, res2)
print(res1/res2)




