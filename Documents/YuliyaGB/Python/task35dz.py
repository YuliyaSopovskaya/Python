# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# Пример:
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

import os

def nlist(data: list) -> list:
    t = {x : data.count(x) for x in data}
    return [k for k in t.keys() if t[k] == 1]


os.system('s')

tests = ((
    [1, 2, 3, 5, 1, 5, 3, 10],
    [1, 8, 7, 5, 5, 5, 5, 5],
    [6, 9, 3, 3, 3, 3] ))

print('список')
for t in tests:
    print(f'{t} -> {nlist(t)}')
