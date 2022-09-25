# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# для всех значений предикат.

def inputNumb(x):
    xyz = ["x", "y", "z"]
    a = []
    for i in range(x):
        a.append(input(f"Введите значение {xyz[i]}: "))
    return a

def predicate(x):
    left = not (x[0] or x[1] or x[2])
    right = not x[0] and not x[1] and not x[2]
    result = left == right
    return result

statement = inputNumb(3)

if predicate(statement) == True:
    print(f"Утверждение истинно")
else:
    print(f"Утверждение ложно")