# 63
# num = int(input('Enter a number:  '))
# sum = num
# count = 0
# if num ==0:
#     print('Error')
# else:
#     while num != 0:
#         num = int(input('Enter a number:  '))
#         sum += num
#         count+=1
    
#     print(f'Sum of the numbers = {sum}')
#     print(f'Count of the numbers = {count}')
#     print(f'Average of the numbers = {int(sum/count)}')


# 64
prices = 4.95, 7.5, 88.54, 12.45
for i in prices:
    print(f'${i} - 60% = ${round(i - (i * 0.6), 2)}')


# 65
# for i in range(0, 101, 10):
#     print(f'{i}(C) ---> {i * 9/5 + 32}(F)')


# 66
# price = (input('Enter the price:  '))
# sum = 0
# while price != '':
#     sum = sum + float(price)
#     price = (input('Enter the price:  '))
# print(f'Total of price = {sum}')
# if sum%5<2.5:
#     sum = sum - sum%5
# else:
#     sum = sum + (5-sum%5)
# print(f'Your payment = {sum}')


#  67 ????????????



# 68
# grade = input('Enter num:  ')
# total = 0
# count = 0
# while grade != '':
#     if grade == 'A+':
#         result = '4.0'
#     elif grade == 'A':
#         result = '4.0'
#     elif grade == 'A-':
#         result = '3.7'
#     elif grade == 'B+':
#         result = '3.3'
#     elif grade == 'B':
#         result = '3.0'
#     elif grade == 'B-':
#         result = '2.7'
#     elif grade == 'C+':
#         result = '2.3'
#     elif grade == 'C':
#         result = '2.0'
#     elif grade == 'C-':
#         result = '1.7'
#     elif grade == 'D+':
#         result = '1.3'
#     elif grade == 'D':
#         result = '1.0'
#     elif grade == 'F':
#         result = '0'
#     else:
#         result = 'Error'
#     grade = input('Enter num:  ')
#     total = total + float(result)
#     count += 1
# print(f'Total grade = {total}')
# print(f'The average grade = {round(total/count , 2)}')


# 69
# age = (input('Your age:  '))
# total = 0
# while age != '':
#     age = int(age)
#     if age <= 2:
#         price = 0
#     elif 2<age<=12:
#         price = 14
#     elif age>=65:
#         price = 18
#     elif 12<age<65:
#         price = 23
#     age = (input('Your age:  '))
#     total += price
# print(f'Total amount for payment = {float(round(total , 2))} $')



# 70  ???????????




# 71
# pi = 3
# n1 = 2
# n2 = 3
# n3 = 4
# i = 0
# while i < 15:
#     if i % 2 == 0:
#         pi += (4 / (n1 * n2 * n3))
#     else:
#         pi -= (4 / (n1 * n2 * n3))
#     n1, n2 ,n3 = n3, n3 + 1, n3 + 2
#     i += 1
# print(pi)



# 72
# num = int(input('Enter a number:  '))
# count = 1
# while num < 100:
#     num = int(input('Enter a number:  '))
#     count+=1
#     if num%3==0 and num%5==0:
        
#         result = 'Fizz-Buzz'
#         print(result)
#     elif num%5 ==0:
#         result = 'BUZZ'
#         print(result)
#     elif num%3==0:
#         result = 'Fizz'
#         print(result)
#     else:
#         print(count)
    


# 75
# name = input('Enter the name:  ')
# if name == name[::-1]:
#     print('Palindrom')
# else:
#     print('Not palindrom')




# 79
# num1 = int(input('Enter number 1:  '))
# num2 = int(input('Enter number 2:  '))
# if 0<num1<num2:
#     x = num1
#     while num1%x!=0 or num2%x!=0:
#         x-=1
#     print(x)
# elif 0<num2<num1:
#     x = num2
#     while num1%x!=0 or num2%x!=0:
#         x-=1
#     print(x)
# elif num1<0 or num2<0:
#     print('Error')
# else:
#     print(num1)

       

# 81
# a = input('Enter a number:  ')
# a= a[::-1]
# c = 0
# d = 0
# for i in range(0,len(a)):
#     b =int((2**c)*(a[i]))
#     c+=1
#     d+=b
#     print(b)
    

#  Կիսատ-պռատ




