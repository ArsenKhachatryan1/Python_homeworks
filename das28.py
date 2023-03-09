
# -----------------Введение в ООП--------------------


# 1. Драка
import random
import time

# class War:

#     def __init__(self, name):
#         self.name = name
#         self.point = 100

#     def game(self, other):
#         while True:
#             choice = random.choice((self.name, other.name))
#             if choice == self.name:
#                 other.point -= 20
#                 time.sleep(2)
#                 print(f'---Win pc---\nuser points = {self.point}\npc points = {other.point}')
#             else:
#                 self.point -= 20
#                 time.sleep(2)
#                 print(f'---Win user---\nuser points = {self.point}\npc points = {other.point}')
#             if self.point == 0:
#                 print('End game WIN PC')
#                 break
#             elif other.point == 0:
#                 print('End game WIN USER')
#                 break
# unit1 = War('Vazgenchik')
# unit2 = War('Mrdo')
# unit1.game(unit2)


# 2. Студенты
# class Student:
#     def __init__(self, full_name, group_number, progress):
#         self.full_name = full_name
#         self.group_number = group_number
#         self.progress = progress
#         self.average = sum(progress) / len(progress)
 
#     def give_average(self):
#         return self.average
 
#     def __str__(self):
#         return f'{self.full_name} -> Group-{self.group_number} -> Average-{self.average}'
 
# def receiving_data():
#     name = input('Student name: ')
#     group = input('Group number: ')
#     grade = list(map (int, input('Grade through a space: ').split()))
#     return name, group, grade

# list_student = [Student(*receiving_data()) for _ in range(3)]
# list_student.sort(key = lambda x : x.give_average())

# print() 
# print('Sorted list of students')
# for i in list_student:
#     print(i)
 


# 3. Круг
import math
# class Circle:
#     def __init__(self, x=0, y=0, r=1):
#         self.x = x
#         self.y = y
#         self.r = r
#     def S(self):
#         return f'{math.pi * self.r ** 2}(m^2)'
#     def P(self):
#         return f'{math.pi * self.r * 2}(m)'
#     def max_r(self, k):
#         self.r *= k
#     def intercept(self, ayl_object):
#         if ((ayl_object.x - self.x) ** 2 + (ayl_object.y - self.y) ** 2) ** 0.5 <= (ayl_object.r + self.r):
#             return True
#         else:
#             return False
# krug1 = Circle()
# # krug1.max_r(5)
# krug2 = Circle(3, 4, 3)
# print(krug1.intercept(krug2))
# print(krug1.P())



# 4. Отцы, матери и дети

# class Child:
#     calm_states = {0:'hangist a ', 1:'lacum a '}
#     hungry_states = {0:'kusht a ', 1:'sovac a '}
#     def __init__(self, child_name, child_age):
#         self.name = child_name
#         self.age = child_age
#         self.calm_state = 0
#         self.hungry_state = 0
 
#     def child_info(self):
#         print(f'{self.name}y {self.age} tarekan a')
 
#     def print_state(self):
#         print(f'{self.name}y hima {Child.calm_states[self.calm_state]}')
#         print(f'{self.name}y hima {Child.hungry_states[self.hungry_state]}')
 
# class Parent:
 
#     def __init__(self, parent_name, parent_age, children, children_count):
#         self.name = parent_name
#         self.age = parent_age
#         self.children = []
#         self.children_count = 0
 
#     def parent_info(self):
#         print(f'Im anuny {self.name} a, es {self.age} tarekan em, es unem {self.children_count} erexa:')
#         for i_child in self.children:
#             i_child.child_info()
#         print()
 
#     def soothe_the_child(self, child):
#         if child.calm_state == 1:
#             print(f'{self.name}y hangstacnum a {child.name}in! ')
#             child.calm_state = 0
#         else:
#             print(f'{self.name}y urax a, vor {child.name}y hangist a! ')
 
#     def feed_the_child(self, child):
#         if child.hungry_state == 1:
#             print(f'{self.name}y kerakrum a {child.name}in! ')
#             child.hungry_state = 0
#         else:
#             print(f'{self.name} urax a, vor {child.name}y  kusht a! ')
 
# import random
 
# parentName = input('Inch a tsnoxi anuny? ')
# parentAge = int(input(f'{parentName}y qani tarekan e? '))
# parent = Parent(parentName, parentAge, children=[], children_count=0)

# children_count = int(input(f'Qani erexa uni {parentName}y?  '))
# for i in range(children_count):
#     child_Name = input('Erexu anuny? ')
#     child_Age = int(input(f'Сколько {child_Name} лет? '))
#     child = Child(child_Name, child_Age)
#     parent.children.append(child)
# parent.children_count += children_count
 
# parent.parent_info()
 
# for i_child in parent.children:
#     i_child.calm_state = random.randint(0, 1)
#     i_child.hungry_state = random.randint(0, 1)
#     i_child.print_state()
#     parent.soothe_the_child(i_child)
#     parent.feed_the_child(i_child)




# 6. Магия

# class Water:
#     def __str__(self):
#         return 'Water'

#     def __add__(self, other):
#         if isinstance(other, Air):
#             return Storm()
#         elif isinstance(other, Fire):
#             return Vapor()
#         elif isinstance(other, Earth):
#             return Dirt()
#         else:
#             None

# class Air:
#     def __str__(self):
#         return 'Air'

#     def __add__(self, other):
#         if isinstance(other, Water):
#             return Storm()
#         elif isinstance(other, Fire):
#             return Lightning()
#         elif isinstance(other, Earth):
#             return Dust()
#         else:
#             None

# class Fire:
#     def __str__(self):
#         return 'Fire'

#     def __add__(self, other):
#         if isinstance(other, Water):
#             return Vapor()
#         elif isinstance(other, Air):
#             return Lightning()
#         elif isinstance(other, Earth):
#             return Lava()
#         else:
#             None

# class Earth:
#     def __str__(self):
#         return 'Earth'

#     def __add__(self, other):
#         if isinstance(other, Water):
#             return Dirt()
#         elif isinstance(other, Air):
#             return Dust()
#         elif isinstance(other, Fire):
#             return Lava()
#         else:
#             None

# class Storm:
#     def __str__(self):
#         return 'Storm'

# class Vapor:
#     def __str__(self):
#         return 'Vapor'

# class Dirt:
#     def __str__(self):
#         return 'Dirt'

# class Lightning:
#     def __str__(self):
#         return 'Lightning'

# class Dust:
#     def __str__(self):
#         return 'Dust'

# class Lava:
#     def __str__(self):
#         return 'Lava'

# def main():
#     water = Water()
#     air = Air()
#     earth = Earth()
#     fire = Fire()

#     print(f'Es xarnum em {water} u {earth}... \n\t'
#     f'Stanum em: {water + earth}')
#     print()
#     print(f'Es xarnum em {water} u {air}... \n\t'
#     f'Stanum em: {water + air}')
#     print()
#     print(f'Es xarnum em {fire} u {air}... \n\t'
#     f'Stanum em: {fire + air}')
#     print()
    
#     print(f'Es xarnum em {earth} u {air}... \n\t'
#     f'Stanum em: {earth + air}')
#     print()
    
# if __name__ == '__main__':
#     main()



#7. Совместное проживание
# from random import randint, choice
 
# class House:
#         food = 50
#         money = 0
 
# class Person:
    
#     def __init__(self, name):
#         self.name = name
#         self.satiety = 50
 
#     def eat(self):
#         self.satiety += 1
#         House.food -= 1
#         return f'ест, сытость {self.satiety} еда {House.food}'
 
#     def work(self):
#         self.satiety -= 1
#         House.money += 1
#         return f'работает, сытость {self.satiety} деньги {House.money}'
 
#     def play(self):
#         self.satiety -= 1
#         return f'играет, сытость {self.satiety}'
        
#     def repast(self):
#         House.food += 1
#         House.money -= 1
#         return f'идет в магазин, еда {House.food} деньги {House.money}'
 
# person_1 = Person('Вася')
# person_2 = Person('Федя')
 
# for i in range(365):
#     number_cubes = randint(1,6)
#     person = choice([person_1, person_2]) 
#     if person.satiety < 0:
#         print(f'К сожалению, {person.name} помер с голоду ')
#         break
#     if person.satiety < 20 and House.food >= 10:
#         text = person.eat()
#     elif House.food < 10:
#         text = person.repast()
#     elif House.money < 50:
#         text = person.work()
#     elif number_cubes == 1:
#         text = person.work()
#     elif number_cubes == 2:
#         text = person.eat()
#     else:
#         text = person.play()
#     print(person.name, text)
        
# print('выжили' if i == 364 else 'все плохо')





        
    
