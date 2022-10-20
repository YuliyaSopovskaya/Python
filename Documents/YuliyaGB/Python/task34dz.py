# Напишите программу, удаляющую из текста все слова, содержащие "абв"

with open('text.txt') as data:
    txt = data.readline()
    print(txt)

    words = txt.split(' ')

    new = " ".join(filter(lambda s: s.find('рып')<0, words))

    print(new)