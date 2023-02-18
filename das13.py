# -----------------Базовые коллекции 1 - list (списки)----------------

# 1. Генерация списка
# num = int(input('Enter number:  '))
# list1 = []
# for i in range(1 , num):
#     if i%2 == 1:
#         list1.append(i)
# print(f'List of odd numbers from one to {num}: {list1}')


# 2. Турнир
# list_t = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
# list1 = []
# for i in list_t:
#     if list_t.index(i)%2 == 0:
#         list1.append(i)
# print(list1)



# 3. Клетки
# n = int(input('Количество клеток:  '))
# mylist = []
# for i in range(1 , n+1):
#     m = int(input(f'Эффективность {i} клетки: '))
#     if m < i:
#         mylist.append(m)
# print(f'Неподходящие значения: {mylist}')




# 4. Видеокарты
# list1 = [3090, 3070, 2060, 3090, 3090, 3070, 3090, 3090]
# print(f'Old list {list1}')
# m = max(list1)
# list1.remove(m)
# for i in list1:
#     if m == max(list1):
#         list1.remove(m)
# print(f'New list {list1}')



# 5. Кино
# films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов', 'Мементо', 'Отступники', 'Деревня']
# new_films = []
# n = int(input('Сколько фильмов хотите добавить?  '))
# for _ in range(n):
#     inp_films = input('Введите название фильма:  ')
#     if inp_films in films:
#         new_films.append(inp_films)
#     else:
#         print(f'Ошибка: фильма {inp_films} у нас нет :(')
# print(f'Ваш список любимых фильмов: {new_films}')



# 6. Анализ слова - 1 
# word = input('Введите слово:  ')
# word1 = []
# count = 0
# for i in word:
#     if i not in word1:
#         word1.append(i)
#         count += 1
#     else:
#         word1.remove(i)
#         count -= 1
# print(f'Количество уникальных букв: {count}')

# 6. Анализ слова - 2
# word = input('Введите слово:  ')
# count = 0
# for i in word:
#     if word.count(i) == 1:
#         count += 1
# print(f'Количество уникальных букв: {count}')



# 7. Контейнеры
# n = int(input('Количество контейнеров:  '))
# kont = []
# if n > 200:
#     print('Error')
# else:
#     for i in range(n):
#         weight = int(input('Введите вес контейнера: '))
#         kont.append(weight)
# kont.sort(reverse=True)
# new_weight = int(input('Введите вес нового контейнера: '))
# for i in kont:
#     if i < new_weight:
#         print(f'Номер, который получит новый контейнер: {kont.index(i)+1}')
#         break
#     elif new_weight <= kont[-1]:
#         print(f'Номер, который получит новый контейнер: {len(kont)+1}')
#         break



# 8. Бегущие цифры
# n = int(input('Enter count of num:  '))
# list1 = []
# for _ in range(n):
#     num = int(input('Enter number:  '))
#     list1.append(num)
# K = int(input('Enter K:  '))
# if K > len(list1):
#     while K > len(list1):
#         K = K-len(list1)
# list2 = []
# for i in list1:
#     if list1.index(i)+K >= len(list1):
#         a = list1.index(i)+K - len(list1)
#         list2.insert(a, i)
#     elif list1.index(i)+K <len(list1):
#         list2.append(i)
# print(f'Изначальный список: {list1}')
# print(f'Сдвинутый список:   {list2}')



# 9. Анализ слова 2
# word = input('Введите слово:  ').lower()
# if word == word[::-1]:
#     print('Слово является палиндромом')
# else:
#     print('Слово не является палиндромом')


# 10. Сортировка
# n = int(input('Введите кол-во чисел для сортировки:  '))
# list1 = []
# for i in range(n):
#     t = int(input('Введите число: '))
#     list1.append(t)
# print(f'Изначальный список: {list1}')
# list1.sort()
# print(f'Отсортированный список: {list1}')





# ---------------------------Методы для работы со списками--------------------

# 1. Страшный код
# list1 = [1, 5, 3]
# list2 = [1, 5, 1, 5]
# list3 = [1, 3, 1, 5, 3, 3]
# count5 = 0
# count3 = 0
# list1 = list1 + list2
# for i in list1.copy():
#     if i == 5:
#         count5 +=1
#         list1.remove(i)
# list1 = list1 + list3
# for i in list1:
#     if i == 3:
#         count3 +=1
# print(f'Кол-во цифр 5 при первом объединении: {count5}')
# print(f'Кол-во цифр 3 при втором объединении: {count3}')
# print(f'Итоговый список: {list1}')



# 2. Шеренга
# das1 = []
# das2 = []
# for i in range(160, 177, 2):
#     das1.append(i)
# for j in range(162, 181, 3):
#     das2.append(j)
# das3 = sorted(das1 + das2)
# print(f'Отсортированный список учеников: {das3}')


# 3. Детали
# shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300], ['педаль', 100], ['седло', 1500],
# ['рама', 12000], ['обод', 2000], ['шатун', 200], ['седло', 2700]]
# detal = input('Название детали: ')
# count = 0
# cena = 0
# for i in shop:
#     for j in i:
#         if j == detal:
#             count += 1
#             cena += i[1]
# print(f'Кол-во деталей - {count}')
# print(f'Общая стоимость - {cena}')


# 4. Вечеринка
# guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
# print(f'Сейчас на вечеринке {len(guests)} человек: {guests}')
# a = input('Гость пришёл или ушёл?  ')
# while True:
#     if a == 'Пора спать':
#         print('Вечеринка закончилась, все легли спать.')
#         break
#     elif a == 'Пришёл':
#         name = input('Имя гостя: ')
#         if len(guests) == 6:
#             print(f'Прости, {name}, но мест нет')
#             print(f'Сейчас на вечеринке {len(guests)} человек: {guests}')
#         else:
#             guests.append(name)
#             print(f'Привет, {name}')
#             print(f'Сейчас на вечеринке {len(guests)} человек: {guests}')
#     elif a == 'Ушёл':
#         name = input('Имя гостя: ')
#         guests.remove(name)
#         print(f'Привет, {name}')
#         print(f'Сейчас на вечеринке {len(guests)} человек: {guests}')
#     a = input('Гость пришёл или ушёл?  ')


# 5. Песни
# songs = [['World in My Eyes', 4.86],
#         ['Sweetest Perfection', 4.43],
#         ['Personal Jesus', 4.56],
#         ['Halo', 4.9],
#         ['Waiting for the Night', 6.07],
#         ['Enjoy the Silence', 4.20],
#         ['Policy of Truth', 4.76],
#         ['Blue Dress', 4.29],
#         ['Clean', 5.83]]
# k = 1
# song_time = 0
# song_num = int(input('Сколько песен выбрать: '))
# for _ in range(song_num):
#     song_name = input(f'Название {k} песни: ')
#     k += 1
#     for i in songs:
#         for j in i:
#             if j == song_name:
#                 song_time += i[1]
# print(f'Общее время звучания песен: {song_time} минут')

    
# 6. Уникальные элементы                    ---- ???? ----
# list1 = []
# for i in range(3):
#     num = int(input(f'Введите {i+1} число для первого списка:  '))
#     list1.append(num)
# list2 = []
# for i in range(7):
#     num = int(input(f'Введите {i+1} число для второго списка:  '))
#     list2.append(num)
# print(list1)
# print(list2)
# list1 = list1 + list2
# print(list(set(list1)))


# 7. Ролики
# n = int(input('Кол-во коньков: '))
# list_k = []
# for i in range(n):
#     size_k = int(input(f'Размер {i+1} пары: '))
#     list_k.append(size_k)

# m = int(input('Кол-во людей: '))
# list_l = []
# for i in range(m):
#     size_l = int(input(f'Размер ноги {i+1} человека: '))
#     list_l.append(size_l)

# count = 0
# a = 0
# for i in list_k:
#     if i >= list_l[a]:
#         count += 1
#         a += 1
# print(count)


# 8. Считалка
# n = int(input('Մուտքագրեք խաղացողների ընդհանուր թիվը:  '))
# list1 = []
# for i in range(1, n+1):
#     list1.append(i)
# K = int(input('Մուտքագրեք դուրս եկող համարը:  '))
# A = K
# # print(list1)
# while len(list1) != 1:
#     # print('K-skz = ', K)
#     for i in list1.copy():
#         if K > len(list1):
#             while K > len(list1):
#                 K = K-len(list1)   
#         print(f'Ընդհանուր խաղացողները։ {list1}')
#         print(f'Դուրս ա գալիս {list1[K-1]} համարի մարդը')
#         list1.remove(list1[K-1])
#         K = A + (K - 1)
#         break
#     print()
# print(f'Մնաց հետևյալ համարը։ {list1}')


# 9. Друзья



# 10. Симметричная последовательность  
# list1 = []  
# list2 = []
# n = int(input('Количество элементов:  '))
# for _ in range(n):
#     num = int(input('Введите натуральные числа от 1 до 9:  '))
#     list1.append(num)
# print(f'Входные данные: {list1}')
# a = 0
# count = 0
# if list1 == list1[::-1]:
#     print(f'Нужно приписать чисел: {count}')
# else:
#     for i in list1.copy():
#         list1.insert(len(list1)-a, i)
#         a += 1
#         list2.append(i)
#         count += 1
#         if list1 == list1[::-1]:
#             break
#     print(f'Нужно приписать чисел: {count}')
#     print(f'Сами числа: {list2[::-1]}')




# Упражнение 133. Содержит ли список подмножество элементов?
larger = [1, 2, 33, 4, 756]
smaller = []
inlist = 0

a = 0
b = len(smaller)
for i in range(len(larger)-b+1):
    i = larger[a:a+b]
    a +=1
    if smaller == i:
        inlist +=1
if inlist > 0:
    print('Small list is sublist')
else:
    print('Small list is NOT sublist')





# Упражнение 134. Все подсписки заданного списка
# larger = [1, 2, 33]
# larger_str = ''
# for i in larger:
#     larger_str += str(i)
# print(larger_str)
# sm = []
# for i in larger_str:
#     sm.append(list(i))
# print(sm)





