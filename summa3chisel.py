import random

a = random.randint(100, 999)
print('случайное число =' ,a)
c = a % 10
a = a // 10
b = a % 10
n = a // 10
print(c + b + n)



