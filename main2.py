key = [2, 1, 4, 3, 6, 5]


def encrip(message):    #Шифрование
    i = 0
    transposition = [0, 0, 0, 0, 0, 0]
    file = open(message, 'rb')  #Открываем файл
    stack = bytearray(file.read())  #Побитово записываем его в стэк
    score = []
    if (len(stack) % len(key)) != 0:
        while len(stack) % len(key) != 0:   # Добавляем в конец строки символ
            stack.append(0)
            i += 1
    for i in range(0, len(stack), len(key)):  #Перебираем все байты не включая ключ
        for j in range(0, len(key), 1):
            transposition[key[j] - 1] = stack[i + j]  #Производим перестановку байтов
        for j in range(0, len(key)):
            score.append(transposition[j])  #Складываем все блоки

    fill_stack = bytearray(score)   #Записываем побайтово в стэк
    file = open(message, 'wb')
    file.write(fill_stack)      #Записываем в файл
    print("Done\n")
    file.close()


def decrip(message):    #Дешифрование
    file = open(message, 'rb')
    stack = bytearray(file.read())
    score = []
    transposition = [0, 0, 0, 0, 0, 0]

    for i in range(0, len(stack), len(key)):
        for j in range(0, len(key), 1):
            transposition[j] = stack[i + key[j]-1]  #Обратная перестановка
        for j in range(0, len(key)):
            score.append(transposition[j])

    fill_stack = bytearray(score)
    file = open(message, 'wb')
    file.write(fill_stack)
    print("Done\n")
    file.close()


file_name = input("Введите имя файла: ")


while True:         #Меню программы
    print('1. Шифрование.')
    print('2. Дешифрование.')
    print('0. Выход из программы.')
    chose = input("Выберите пункт меню -> ")

    if chose == '1':
        encrip(file_name)
    elif chose == '2':
        decrip(file_name)
    elif chose == '0':
        break
    else:
        print("Такой команды в меню нет :(")
