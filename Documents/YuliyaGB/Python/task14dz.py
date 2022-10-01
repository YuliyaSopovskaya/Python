# 1. Напишите программу, которая принимает на вход вещественное число и 
# 2. показывает сумму его цифр.

# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# num = int(input('Введите число: '))
# sum = 0

# while num > 0 and num < 0:
#   sum += num % 10
#   num //= 10

# print(sum)

def func(number):
    sum = 0

    number = number.replace(',', '.')

    for symbol in number:
        if symbol != '.':
            sum += int(symbol)

    return sum


if __name__ == "__main__":
    chislo = input('Input a number: ')
    summary = func(chislo)

    print(summary)