# 2. Напишите программу, которая на вход принимает 5 чисел и 
#  находит максимальное из них.    
#     Примеры:    
#     - 1, 4, 8, 7, 5 -> 8
#     - 78, 55, 36, 90, 2 -> 90

# a, b, c, d, f = int(input()), int(input()), int(input()), int(input()), int(input())

# max= a 
# if (b>max):
#     max=b
# if (c>max):
#     max=c
# if (d>max):
#     max=d
# if (f>max):
#     max=f  
# print(max)



some_list = []
for i in 1,2,3,4,5:
    some_list.append(int(input()))
    print(some_list)
    max = some_list[0]
for i in some_list:
    if max < i: max = i
print(max)
