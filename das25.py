
# Декораторы: базовый уровень
# 1. Как дела?

# import functools
# import time

# def vasya_decor(func):
#     @functools.wraps(wrapped=func)
#     def wraps_decor(*args):
#         print('Как дела? Хорошо. А у меня не очень! Ладно, держи свою функцию.')
#         func(*args)
#     return wraps_decor

# time.sleep(2)
# @vasya_decor
# def test():
#     '''TEST FUNC'''
#     print('Hello')
# test()
# print(test.__doc__)




# --------------------------------------------

# import math

# person = [3, 3, 3, 5, 5, 2, 1, 6, 6]
# house_price = 70

# mylist = person.copy()
# newlist = []
# mydict = {}

# count = 1
# for i in range(0, max(person)):
#     price = house_price / len(person)
#     while count in person:
#         person.remove(count)
#     count += 1
#     newlist.append(price)


# mylist = list(set(mylist))
# mylist.sort()
# for i in mylist:
#     mydict[i] = 0
# for i in mydict:
#     mydict[i] = math.ceil(sum(newlist[0:i]))
# print(mydict)



