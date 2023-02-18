
# Упражнение 180. Редакционное расстояние
def myfunc(s, t):
    if len(s) == 0:
        return len(t)
    elif len(t) == 0:
        return len(s)
    else:
        cost = 0
    if s[-1] != t[-1]:
        cost = 1
    d1 = myfunc(s[0 : len(s) - 1], t) + 1
    d2 = myfunc(s, t[0 : len(t) - 1]) + 1
    d3 = myfunc(s[0 : len(s) - 1] , t[0 : len(t) - 1]) + cost
    return min(d1, d2, d3)
s1 = input('Enter word 1:  ')
t1 = input('Enter word 2:  ')
print(myfunc(s1, t1))




