# Задачи:
# 1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого
#     Примеры:
#     - 5, 25 -> да
#     - 4, 16 -> да
#     - 25, 5 -> да
#     - 8,9 -> нет

a = int(input("Введите a"))
b = int(input("Введите b"))

if a == b**2 or b ==a**2:
    print ('True')
else:
    print('False')