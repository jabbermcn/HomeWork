# Пользователь вводит 3 числа, сказать сколько из них положительных и сколько отрицательных

a = int(input('Enter the number a: '))
b = int(input('Enter the number b: '))
c = int(input('Enter the number c: '))
sum_positive = 0
sum_negative = 0
if a > 0:
    sum_positive += 1
if b > 0:
    sum_positive += 1
if c > 0:
    sum_positive += 1
if a < 0:
    sum_negative += 1
if b < 0:
    sum_negative += 1
if c < 0:
    sum_negative += 1
print(f'{sum_positive} positive numbers')
print(f'{sum_negative} negative numbers')
