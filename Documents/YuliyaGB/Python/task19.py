# 2. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

def func(lst):
    for item in lst:
        if isinstance(item, int) or isinstance(item, float): #проверяет есть или нет в списке это 
            return "Yes"

    return "No"

if __name__ == "__main__":
    print(func(["1982", "gfghfhg", "hjgjhg", 51, "18375"]))