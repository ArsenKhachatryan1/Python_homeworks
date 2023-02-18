



# Упражнение 173. Сумма значений
# total = 0
# def myfunc():
#     n = input('Enter number:  ')
#     if n == '':
#         return 0
#     else:
#         return int(n) + myfunc()
# print(myfunc())



# Упражнение 174. Наибольший общий делитель
# num1 = int(input('Enter number 1:  '))
# num2 = int(input('Enter number 2:  '))
# def myfunc(num1, num2):
#     if num2 == 0:
#         return num1
#     else:
#         num1 = num1 % num2
#         return  myfunc(num2, num1)
# print(myfunc(num1,num2))
# print()





# Упражнение 175. Рекурсивный перевод числа из десятичного в двоичное
# n = int(input('Enter number:  '))
# def dec_to_bin(n, s=''):
#     if n == 1:
#         return f'{n}{s[::-1]}'
#     else:
#         return dec_to_bin(n // 2, s + str(n % 2))
# print(dec_to_bin(n))



# Упражнение 176. Фонетический алфавит НАТО
# list1 =['Alpha', 'Bravo', 'Charlie', 'Delta', 'Echo', 'Foxtrot', 'Golf', 'Hotel', 'India', 'Juliet', 'Kilo', 'Lima', 'Mike', 'November', 'Oscar', 'Papa', 'Quebec', 'Romeo', 'Sierra', 'Tango', 'Uniform', 'Victor', 'Whiskey', 'Xray', 'Yankee', 'Zulu']
# word = input('Enter word:  ').upper()
# def myfunc(word):
#     for i in list1:
#         for j in word:
#             if j == i[0]:
#                 print(i, end=' ')
# myfunc(word)


# Упражнение 181. Возможный размен
def func(amount, coin_count):
    if amount == 0 or coin_count == 0:
        return amount == coin_count
    return func(amount - 25, coin_count - 1) or func(amount - 10, coin_count - 1) or func(amount - 5, coin_count - 1) or func(amount - 1, coin_count - 1)
print(func(101, 5))


# # Упражнение 184. Выравниваем список
# def func(mylist:list[int, list]) -> list[int]:
#     if mylist == []:
#         return []
#     elif isinstance(mylist[0], int):
#         return [mylist[0]] + func(mylist[1:])
#     elif isinstance(mylist[0], list):
#         return func(mylist[0]) + func(mylist[1:])
# print(func([1, [2, 3], [4, [5, [6, 7]]], [[[8],9], [10]]]))


