# 1. Напишите программу, которая принимает на вход число N 
# и выдаёт последовательность из N членов, 
# подчиняющихся закону f(i) = 3^i*(-1)^i, где i - индекс элемента последовательности.
# Пример:
# - Для N = 5: 1, -3, 9, -27, 81

n = int(input("enter n ="))
some_list = []
for i in range (0, n):
    some_list.append((-3)**i)
print(some_list)