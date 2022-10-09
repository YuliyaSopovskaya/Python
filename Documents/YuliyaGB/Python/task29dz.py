# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и
# записать в файл многочлен степени k.
# Пример:
# k=2 => 2*x^2 + 4*x + 5 = 0 или x^2 + 5 = 0 или 10*x^2 = 0

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
