
# -------------OOP Exercises------------

# 2.Николаю требуется проверить

# class TriangleChecker:

#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c

#     def is_triangle(self):
#         try:
#             if ((float(self.a) + float(self.b) > float(self.c)) and (float(self.a) + float(self.c) > float(self.b))
#              and (float(self.c) + float(self.b) > float(self.a))):
#                 return '- Ура, можно построить треугольник!'
#             elif float(self.a) < 0 or float(self.b) < 0 or float(self.c) < 0:
#                 return '– С отрицательными числами ничего не выйдет!'
#             else:
#                 return '– Жаль, но из этого треугольник не сделать.'
#         except ValueError:
#             return '– Нужно вводить только числа!' 

# a = input('Enter first side:  ')
# b = input('Enter second side:  ')
# c = input('Enter third side:  ')
# erankyun = TriangleChecker(a, b, c)
# print(erankyun.is_triangle())




# 4. Николай – оригинальный человек.
# class Nikola:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def anun(self):
#         if self.name == 'Nikolay':
#             return f'Ya {self.name}, mne {self.age} let'
#         return  f'Ya ne {self.name}, a Nikolay, mne {self.age} let'
 
# name = input('Enter your name: ')
# age = int(input('Enter your age: '))
# mard = Nikola(name, age)

# print(mard.anun())

        

# --------------------------------codewars------------------
# High score table

# class HighScoreTable:

#     def __init__(self, lenght, table=[]):
#         self.length = lenght
#         self.table = table

#     def scores(self):
#         self.table = sorted(self.table, reverse=True)
#         return self.table[0:self.length]
    
#     def update(self, score):
#         self.table.append(score)

#     def reset(self):
#         return self.table.clear()

# highScoreTable = HighScoreTable(3)
# highScoreTable.update(10)
# highScoreTable.update(4)
# highScoreTable.update(7)
# highScoreTable.update(18)
# highScoreTable.reset()
# highScoreTable.update(14)
# print(highScoreTable.scores())



# Thinkful - Object Drills: Quarks

# class Quark:
    
#     def __init__(self, col, fl) -> None:
#         self.col = col
#         self.fl = fl

#     def color(self):
#         return f'Color is {self.col}'
    
#     def flavor(self):
#         return f'Flavor is {self.fl}'
    
#     def baryon_number(self):
#         return f'Baryon_number = {1/3}'
    
#     def interact(self, other):

#         self.col , other.col = other.col , self.col
    
# q1 = Quark('green', 'up')
# q2 = Quark("blue", "strange")
# # q1.interact(q2)

# print(q1.baryon_number())
# print(q1.color())
# print(q1.flavor())
# print()
# print(q2.baryon_number())
# print(q2.color())
# print(q2.flavor())




# Building blocks

# class Block:

#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c

#     def get_width(self):
#         return f'The width of the Block = {self.a}'
    
#     def get_length(self):
#         return f'The length of the Block = {self.b}'
    
#     def get_height(self):
#         return f'The height of the Block = {self.c}'
    
#     def get_volume(self):
#         return f'The volume of the Block = {self.a*self.b*self.c}'
    
#     def get_surface_area(self):
#         return f'The surface area of the Block = {2*(self.a*self.b+self.a*self.c+self.b*self.c)}'
    

# block = Block(2,4,6)

# print(block.get_height())
# print(block.get_length())
# print(block.get_width())
# print(block.get_volume())
# print(block.get_surface_area())




# PaginationHelper

class PaginationHelper:

    def __init__(self, text=list(), item=int):
        self.text = text
        self.item = item
        
    def page_count(self):
        self.i_count = 0
        for _ in self.text:
            self.i_count += 1
        self.p_count = (self.i_count/self.item).__ceil__()
        return f'Total page count = {self.p_count}'
    
    def item_count(self):
        return f'Total item count = {self.i_count}'
    
    def page_item_count(self, a):
        self.a = a
        if self.a < self.p_count:
            return f'Item count in page {self.a} = {self.item}'
        elif self.a == self.p_count:
            return f'Item count in page {self.a} = {self.i_count - (self.p_count-1)*self.item}'
        else:
            return f'Item count in page {self.a} = -1! since the page is invalid'
        
    def page_index(self, b):
        self.b = b+1
        if 0 < self.b <= self.i_count:
            return f'Index {self.b} item is in page -> {(self.b/self.item).__ceil__()}'
        elif self.b <= 0:
            return 'Negative indexes are invalid'
        else:
            return 'The index out of range'

helper =  PaginationHelper(['a','b','c','d','e','f'], 2)

print(helper.page_count())
print(helper.item_count())
print(helper.page_item_count(3))
print(helper.page_index(6))