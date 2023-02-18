# Упражнение 77. Таблица умножения
# print('       1    2    3    4    5    6    7    8    9   10')
# for i in range(1 ,11):
#     print(f'{i:>3}', end=' ' )
#     for j in range(1 , 11):
#         j = i*j
#         print(f'{j:>4}', end=' ')
#     print()



# # ***************************************

# Parz Tver
# n = int(input('Enter number: '))
# for i in range(1 , n+1):
#     # print(i)
#     for j in range(2 , i//2+1):
#         if i%j ==0:
#             break
#     else:
#         print(i)



# ----------------------------


# -----------------------------------------10.Вложенные циклы------------
# Задача 10. Яма
# n = int(input('Enter a number: '))
# if 1<n<10:
#     number = 2
#     a = ''
#     for i in range(n, 0, -1):
#         a+=str(i)
#     b =''
#     for j in a:
#         b+=j
#         print(b+(2*n-number)*'.'+b[::-1])
#         number+=2
# else:
#     print('Input is not a correct number')       






# --------------------------------------------
# a = 1 ,2 ,3, 4 , 5
# count = 0
# for i in a:
#     for j in a:
#         for l in a:
#             count +=1
#             print(i,j,l)
# print(count)


# ----------------------------------------
# boy = int(input('Enter boys:  '))
# girl = int(input('Enter girs:  '))
# a = boy*'B'+girl*'G'
# # a = 'BGBGBGG'
# # b = girl*'G'
# print(a, 'es a')
# for i in a:
# # for i in range(0, len(a)-1,):
#     # print(a[i], i)
#     print(i)

#     i=a
#     # i+=1
#     # b=a
# print(i)
    
# print()


# boys = int(input('Введите кол-во мальчиков: '))
# girls = int(input('Введите кол-во девочек: '))
# answer = ''
# if (boys > 2 * girls) or (girls > 2 * boys):
#     print('Нет решения.')
# elif boys >= girls:
#     k = boys - girls                     # k = 2
#     for bgb in range(k):                                 
#         answer += 'BGB'                      #BGBBGB
#     for bg in range(girls - k):               
#         answer += 'BG'
# else:
#     k = girls - boys
#     for gbg in range(k):
#         answer += 'GBG'
#     for gb in range(boys - k):
#         answer += 'GB'
# print(answer)