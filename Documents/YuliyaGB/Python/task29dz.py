# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и
# записать в файл многочлен степени k.
# Пример:
# k=2 => 2*x^2 + 4*x + 5 = 0 или x^2 + 5 = 0 или 10*x^2 = 0

from random import randint
import random
my_f = open("result.txt", "w")
#with open("result.txt", "w+", encoding='utf-8') as my_f:
k = int(input("Введите число:   "))
lst = [random.randint(0,100) for i in range(k + 1)]
print(lst)
x = ""
for i in range(k + 1):
    if i < k:
        x += str(lst[i]) + "*x^" + str(k-i)  +  " + " 
    else:
        x += str(lst[i])
print(x)

my_f.write(f'{x}  \n')
my_f.close()

# from random import randint

# def func(k):    
#     file = open("result.txt", "w")
#     #list = []
#     a = int(0)
#     for i in range(-k, -1):
#         a = randint(0, 101)
#         if a != 0:
#             file.write(str(a))
#             file.write('*x^')
#             file.write(str(-i))
#             file.write('+')
# #print (a, '*x^', -i ,'+', end='')
#     a = randint(0, 101)
#     if a != 0:
#             file.write(str(a))
#             file.write('*x+')
#     a = randint(0, 101)
#     if a != 0:
#             file.write(str(a))
#     file.write('=0')


#     file.close()

# chislo = int(input("Введите коэф k:"))

# func(chislo)
