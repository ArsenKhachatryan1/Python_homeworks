
# Упражнение 149. Отображаем начало файла
# def head(filename):
#     try:
#         with open(filename, 'r') as file:
#             for i in range(10):
#                 print(file.readline())
#     except FileNotFoundError:
#         print('No such file')

# head(input('Enter filename: '))


# Упражнение 150. Отображаем конец файла
# def tail(filename):
#     try:
#         with open(filename, 'r') as file:
#             a = []
#             for i in file.readlines():
#                 a.append(i)
#             for i in a[-10:]:
#                 print(i)
#     except FileNotFoundError:
#         print('No such file found')
# tail(input('Enter filename: '))



# Упражнение 151. Сцепляем файлы
# list1 = []
# filename1 = input('Enter filename1: ')
# filename2 = input('Enter filename2: ')
# try:
#     with open(filename2, 'r') as file2:
#         for i in file2.readlines():
#             list1.append(i)
# except FileNotFoundError:
#     print('No such file found')

# try:
#     with open(filename1, 'a') as file1:
#         file1.write('\n')
#         for i in list1:
#             file1.write(i)
# except FileNotFoundError:
#     print('No such file found')
# with open(filename1, 'r') as file:
#     print(file.readlines())




# Упражнение 152. Нумеруем строки в файле
# filename1 = input('Enter filename1: ')
# filename2 = input('Enter filename2: ')
# num = 1
# list1 =[]
# with open(filename1, 'r') as file:
#     line = file.readline()
#     while line != '':
#         list1.append(f'{num}: {line}')
#         num +=1
#         line = file.readline()

# with open(filename2, 'w') as file:
#     for i in list1:
#         file.write(i)




# Упражнение 153. Самое длинное слово в файле
with open('113.txt', 'r') as file:
    list1 = file.readlines()
list1.sort(key=len, reverse= True)
list2 = []
for i in list1:
    i = i.replace('\n', '')
    list2.append(i)
list3 = [] 
list3.append(list2[0])
a = 1
for i in list2:
    if len(list2[a]) >= len(list3[0]):
        list3.append(list2[a])
        a +=1
print(list3)



