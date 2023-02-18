# --------------------------------------------------------Dictionaries ------------------------

# 1.Write a Python program to sort a dictionary by value.
# mydict = {'D': 56, 'E': 12, 'F': 69, 'C': 45, 'B': 23, 'A': 67}
# dictvalues = sorted(mydict.values())
# print(dictvalues)


# 2. Write a Python program to add a key to a dictionary.
# mydict = {'name':'Aram', 'year': 1994}
# mydict['job'] = 'Geologist'
# print(mydict)


# 3. Write a Python program to check whether agiven key already exists in a dictionary
# 4. Write a Python program to merge two Python dictionaries.

# dict1 = {'a': 50, 'b': 700}
# dict2 = {'c': 400, 'd': 600}
# dict1.update(dict2)
# print(dict1)
# a = input('Enter key: ')
# if a in dict1:
#     print('Yes')
# else:
#     print('No')


# 5. Write a Python program to multiply all the values in a dictionary.
# a = 1
# mydict = {'a': 1,'b': 2,'c': 12, 'd' : 11}
# for i in mydict.values():
#     a *= i
# print(a)


# 6. Create a Python program to find the highest 3 values in a dictionary.
# mydict = {'D': 56, 'E': 12, 'F': 69, 'C': 45, 'B': 23, 'A': 67}
# myvalues = sorted(mydict.values(), reverse= True)[:3]
# print(myvalues)






# ---------------------------------------------Dictionaries, Exercises------------------------ 
# 1. New Dictionary
# students = ['Armen', 'Aram', 'Ani', 'Garnik', 'Tigran', 'Lilit', 'Anna', 'Artur', 'Vachik', 'Vardan']
# grades = 3, 7, 10, 8, 4, 5, 6, 8, 9, 7
# mydict = {}
# for i, j in zip(students, grades):
#     mydict[i] = j
# print(mydict)



# 2. Arithmetic average
# mydict = {'Armen': 3, 'Aram': 7, 'Ani': 10, 'Garnik': 8, 'Tigran': 4,
#          'Lilit': 5, 'Anna': 6, 'Artur': 8, 'Vachik': 9, 'Vardan': 7}
# count_st = 0
# grade_st = 0
# for i in mydict.values():
#     count_st += 1
#     grade_st += i
# print(f'The arithmetic average:  {grade_st/count_st}')


# 3-4-5 Good and bad students
# mydict = {'Armen': 3, 'Aram': 7, 'Ani': 10, 'Garnik': 8, 'Tigran': 4,
#          'Lilit': 5, 'Anna': 6, 'Artur': 8, 'Vachik': 4, 'Vardan': 7}
# good_st = {}
# bad_st ={}
# for i in mydict:
#     if mydict[i] >= 5:
#         good_st.setdefault(i, mydict[i])
#     else:
#         bad_st.setdefault(i, mydict[i])
# print(f'Good students:\n{good_st}')
# print(f'Bad students:\n{bad_st}')


# 6. Name
# mydict = {'Armen': 3, 'Aram': 7, 'Ani': 10, 'Garnik': 8, 'Tigran': 4,
#          'Lilit': 5, 'Anna': 6, 'Artur': 8, 'Vachik': 4, 'Vardan': 7}

# name = input('Enter name:  ')
# if name in mydict:
#     print(name, mydict[name])
# else:
#     print('Name is not in dictionary')



# 7. New_dict
# s = 'a,2,b,5,c,8,a,4,e,11'
# list1 = s.split(',')
# newdict = {}
# a = 0
# while a <= len(list1)-2:
#     newdict.setdefault(list1[a], list1[a+1])
#     a+=2
# print(newdict)


# 8. Dict from a string
# word = 'exercises'
# mydict = {}
# for i in word:
#     mydict.setdefault(i, word.count(i))
# print(mydict)


# 9. Remove all duplicate items in list
# old_list = [{'key1':'value1'},{},{},{'key1':'value1'},{'key2':'value2'}]
# new_list = []
# for i in old_list:
#     if i in new_list:
#         pass
#     else:
#         new_list.append(i)
# print(new_list)




