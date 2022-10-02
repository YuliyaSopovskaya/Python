
# 1. Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.

from time import time


def func(t):
    return int(str(t).split('.')[1]) % 1000


if __name__ == "__main__":
    print(func(time()))