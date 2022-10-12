# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

lst = list(map(int, input("Введите числа через пробел:\n").split()))
print(f"Исходный список: {lst}")
new_lst = []
[new_lst.append(i) for i in lst if i not in new_lst]
print(f"Список из неповторяющихся элементов: {new_lst}")


# from random import randrange

# def count_of_numbers(count: int):
#     if count < 0:
#         print("отрицательное число элементов!")
#         return[]
#     list_numbers = []
#     for i in range(count):
#         list_numbers.append(randrange(count))
#     return list_numbers

# def non_repeat_elements(list_numbers):
#     return set(list_numbers)

# all_list = count_of_numbers(int(input("Размер списка: ")))
# print(all_list)
# print(non_repeat_elements(all_list))