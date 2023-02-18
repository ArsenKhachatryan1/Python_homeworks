# ----------------------------------------------------Tuple Data Types---------------------------------------

# 1.
# mylist = [1 , 8 , 43 , -97 , 7 , (12 , 13 ,14), 32 , 0]
# print(mylist)
# mycount = 0
# for i in mylist:
#     if type(i) != tuple:
#         mycount +=1
#     else:
#         break
# print(mycount)


# 2.
# mytuple1 = ('Gold', 'Copper' , 'Molly' , 'Silver' , 'Lead' , 'Zink')
# mytuple2 = tuple(reversed(mytuple1))
# print(mytuple2)


# 4.
# mytuple1 = ('Gold', 'Copper' , 'Molly' , 'Silver' , 'Lead' , 'Zink')
# string = ', '.join(mytuple1)
# print(string)
# print(type(string))


# 5.
# tuple1 = (4, 8, 94, 45, 27)
# sum1 = 0
# for i in tuple1:
#     sum1+=i
# print(sum1)


# 6.
# mytuple1 = (2, 58, 31, 40, 'Gold', 23, 11)
# for i in mytuple1:
#     if type(i) == str:
#         print(i)



# ---------------------------------------------------List Data Types---------------------------------------------


# 1 , 2
# numbers =[34, 56 , -456, 7.56, - 2.34]
# sum1 = 0
# mtp = 1
# for i in numbers:
#     sum1 += i
#     mtp *= i
# print(sum1)
# print(mtp)


# 3.
# mylist = ['py', 'programming', 'python', 'result', 'hello']
# mylist.sort(key=len)
# print(mylist[-1])

# mylist = [4, 1, -8, 55.2, 41.75, 6, 9, 7, 10]
# mylist.sort( reverse=True)
# print(mylist)


# 4.
# list1 = [5, 7, 11]
# list2 = [4, 17, 6, 22, 45]
# count1 = 0
# for i in list2:
#     if i in list1:
#         count1+=1
# # print(count1) 
# if count1 == 0:
#     print('False')
# else:
#     print('True')

            


#-----------------------------------------------Exercises-----------------------------------

# 1. New List
# list1 = [1, 3.14, ('A', 'B', 'C'), 'Africa', [3, 9, 27]]
# for i in list1:
#     print(type(i))


# 2. Mac
# my_list=['Hp', 'Asus', 'Dell', 'Mac', 'Lenovo']
# print('Mac' in my_list)


# 3. Password-1
# password = input('Enter password:  ')
# sp_ch1 = ('!', '@', '#', '$', '%', '&', '*')
# num1 = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
# sp_ch2 = 0
# num2 = 0
# if len(password)<=8:                  
#     print('Short Password')
# else:
#     for i in password:
#         if i in sp_ch1:
#             sp_ch2 +=1
#         elif str(i) in num1:
#             num2 +=1
#     if sp_ch2>=2 and num2 >= 2:
#         print('Strong password')
#     else:
#         print('Weak password')

#  3. Password-2
# chars = '!@#$%^&*()-_=+ ,<.>/?'
# while True: 
#     char_count = 0
#     number_count = 0
#     password = input('Enter password: ')
#     if len(password) < 8:
#         print('Your password is not strong  :( !!!!')
#     else:
#         if password[0].isupper():
#             for i in password:
#                 if i.isdigit():
#                     number_count += 1
#                 elif i in chars:
#                     char_count += 1
#         else:
#             print('Your password is not strong  :( !!!!')

#         if char_count >= 2 and number_count >= 2:
#             print(f'{password}\n\t--->Yout password is strong :)<---')
#             break
#         else:
#             print('Your password is not strong  :( !!!!')
            

# 4. Link Finder
# link = input('Enter a link: ')
# for i in link:
#     if i == '=':
#         id = link.index('=')
#         print(f'Link ID is --> {link[id+1:]}')
#         break
#     elif '=' not in link:
#         print('No link ID')
#         break



# 5. Sign in
# text = input('Enter text:  ').lower()
# print(text)
# if text == text[::-1]:
#     print('Open')
# else:
#     print('Trash')



# 6. String-to-List                  
# string = input('Enter text:  ')
# my_list = string.split(' ')
# print(my_list)


# 7. Even Numbers
# num = input('Enter numbers:  ')
# num = num.split(' ')
# for i in num:
#     if int(i) %2 == 0:
#         print(i, end=' ')


# 8. Odd-1
# list1 = [1, 45, 364, 95, 3, 484, 65, 51351]
# list2 = []
# for i in list1:
#     if i%2 == 1:
#         list2.append(i)
# print(list2)

# 8. Odd-2
# list_ = [1, 45, 364, 95, 3, 484, 4, 65, 51351]
# for i in list_.copy():
#     if i % 2 == 0:
#         list_.remove(i)
# print(list_)



import random
# 9. Secret Santa-1
# anun = ['Aram', 'Ani', 'Lilit', 'Armen', 'Hayk']
# anun2 = []
# anun3 = []
# while len(anun2) != len(anun):
#     a = random.choice(anun)
#     b = random.choice(anun)
#     if a!=b:
#         if a not in anun2 and b not in anun3:
#             anun2.append(a)
#             anun3.append(b)
#         else:
#             anun2 = []
#             anun3 = []  
# for i, j in zip(anun2, anun3):
#     print(f'{i} --- {j}')

# 9. Secret Santa-2    
# anun = ['Aram', 'Ani', 'Lilit', 'Armen', 'Hayk']
# new_name = []
# names = []
# while len(anun) != 0:
#     x = random.choice(anun)
#     new_name.append(x)
#     anun.remove(x)
# for i in range(0, len(new_name) - 1):
#     names.append(f'{new_name[i]} --- {new_name[i + 1]}')
# names.append(f'{new_name[-1]} --- {new_name[0]}')
# while len(names) != 0:
#     x = random.choice(names)
#     print(x)
#     names.remove(x)


# 9. Secret Santa-3
# anun = ['Aram', 'Ani', 'Lilit', 'Armen', 'Hayk']
# names = []
# random.shuffle(anun)
# for i in range(0, len(anun) - 1):
#     names.append(f'{anun[i]} --- {anun[i + 1]}')
# names.append(f'{anun[-1]} --- {anun[0]}')
# random.shuffle(names)
# for i in names:
#     print(i)




# 10. Duplicate
# list1 = [1, 45, 364, 95, 3, 484, 3, 1, 65, 513]
# list2 = []
# for i in list1:
#     if i in list2:
#         pass
#     else:
#         list2.append(i)
# print(list2)













