import random

# Упражнение 146. Карточка лото

print()
b = list(range(1, 16))
i = list(range(16, 31))
n = list(range(31, 46))
g = list(range(46, 61))
o = list(range(61, 76))
random.shuffle(b)
random.shuffle(i)
random.shuffle(n)
random.shuffle(g)
random.shuffle(o)

loto_dict = {}
loto_dict.setdefault('B' , b[:5])
loto_dict.setdefault('I', i[:5])
loto_dict.setdefault('N', n[:5])
loto_dict.setdefault('G', g[:5])
loto_dict.setdefault('O', o[:5])

for i in loto_dict:
    print(i, end='  ')
    for j in loto_dict[i]:
        print(f'{j:>5}\t', end='    ', )
    print()
    print()

print()
print("Ահա Ձեր լոտոյի տոմսը։\nԽաղը սկսելու համար սեղմեք 'Enter' կոճակը")
input()
Tcount = 0
Bcount = 0
Icount = 0
Ncount = 0
Gcount = 0
Ocount = 0

park = list(range(1,76))

for i in park:
    while True:
        if Bcount == 5:
            break
        elif Icount == 5:
            break
        elif Ncount == 5:
            break
        elif Gcount == 5:
            break
        elif Ocount == 5:
            break
        elif loto_dict['B'][0] ==loto_dict['I'][0] == loto_dict['N'][0] ==loto_dict['G'][0] ==loto_dict['O'][0]:
            break
        elif loto_dict['B'][1] ==loto_dict['I'][1] == loto_dict['N'][1] ==loto_dict['G'][1] ==loto_dict['O'][1]:
            break
        elif loto_dict['B'][2] ==loto_dict['I'][2] == loto_dict['N'][2] ==loto_dict['G'][2] ==loto_dict['O'][2]:
            break
        elif loto_dict['B'][3] ==loto_dict['I'][3] == loto_dict['N'][3] ==loto_dict['G'][3] ==loto_dict['O'][3]:
            break
        elif loto_dict['B'][4] ==loto_dict['I'][4] == loto_dict['N'][4] ==loto_dict['G'][4] ==loto_dict['O'][4]:
            break
        elif loto_dict['B'][0] ==loto_dict['I'][1] == loto_dict['N'][2] ==loto_dict['G'][3] ==loto_dict['O'][4]:
            break
        elif loto_dict['B'][4] ==loto_dict['I'][3] == loto_dict['N'][2] ==loto_dict['G'][1] ==loto_dict['O'][0]:
            break
               
        num = random.choice(park)
        print(f'Դուրս եկավ համար։ {num}')
        print()
        Tcount += 1
            
        for i in loto_dict.values():
            for j in i:
                if num == j:
                    i[i.index(j)] =  '●'
                if num == j and num <16:
                    Bcount += 1
                elif num == j and 16<=num<31:
                    Icount += 1 

                elif num == j and 31<=num<46:
                    Ncount += 1
                elif num == j and 46<=num<61:
                    Gcount +=1
                elif num == j and 61<=num<76:
                    Ocount += 1


        #   ------------------- lotoyi printi hamar----------
        for i in loto_dict:
            print(i, end='  ')
            for j in loto_dict[i]:
                print(f'{j:>5}\t', end='    ', )
            print()
            print()

        park.remove(num)
        input()

print(f'Դուք հաղթեցիք!!!\nԸնդհանուր քայլերի քանակը կազմեց։ {Tcount}')





