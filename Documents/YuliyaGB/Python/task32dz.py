# Cоздайте программу для игры в крестики-нолики

import random
def check_x(pole):
    if pole[0][0] == 'X' and pole[1][1] == 'X' and pole[2][2] == 'X':
        print('x Выиграл')
        return True
    elif pole[2][0] == 'X' and pole[1][1] == 'X' and pole[0][2] == 'X':
        print('x Выиграл')
        return True
    elif pole[0][0] == 'X' and pole[0][1] == 'X' and pole[0][2] == 'X':
        print('x Выиграл')
        return True
    elif pole[0][0] == 'X' and pole[1][0] == 'X' and pole[2][0] == 'X':
        print('x Выиграл')
        return True
    elif pole[2][0] == 'X' and pole[2][1] == 'X' and pole[2][2] == 'X':
        print('x Выиграл')
        return True
    elif pole[0][2] == 'X' and pole[1][2] == 'X' and pole[2][2] == 'X':
        print('x Выиграл')
        return True
    else:
        return False

def check_0(pole):
    if pole[0][0] == 'O' and pole[1][1] == 'O' and pole[2][2] == 'O':
        print('0 Выиграл')
        return True
    elif pole[2][0] == 'O' and pole[1][1] == 'O' and pole[0][2] == 'O':
        print('0 Выиграл')
        return True
    elif pole[0][0] == 'O' and pole[0][1] == 'O' and pole[0][2] == 'O':
        print('0 Выиграл')
        return True
    elif pole[0][0] == 'O' and pole[1][0] == 'O' and pole[2][0] == 'O':
        print('0 Выиграл')
        return True
    elif pole[2][0] == 'O' and pole[2][1] == 'O' and pole[2][2] == 'O':
        print('0 Выиграл')
        return True
    elif pole[0][2] == 'O' and pole[1][2] == 'O' and pole[2][2] == 'O':
        print('0 Выиграл')
        return True
    else:
        return False

pole = [["_","_","_",],
        ["_","_","_",],
        ["_","_","_",]]
for i in pole:
    print(i)

while not check_x(pole) and not check_0(pole):
    a, b = int(input()), int(input())
    pole[a][b] = "X"
    for i in pole:
        print(i)
    print("Ходит бот")
    while True:
        c, d = random.randint(0,2), random.randint(0,2)
        if pole [c][d] != "X":
            break
    pole[c][d] = "О"
    for i in pole:
        print(i)