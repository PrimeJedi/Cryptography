#n=5 a=1 b=6
S = [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
     [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
     [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
     [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]]


def bits_to(stack):                                         #перевод текста в двоичный код
    bits = ""
    for i in range(0, len(stack)):
        bits += bin(stack[i])[2:].zfill(8)
    return bits


def add_stack(stack_to_bits,encrypted_block):   #добавляем недостающие биты в блок
    for i in range(len(stack_to_bits) % 6, 0, -1):
        encrypted_block += stack_to_bits[len(stack_to_bits) - i]
    return encrypted_block


def encryp(message):                          #Шифрование
    with open(message, 'rb') as file:
        stack = bytearray(file.read())        # Считываем файл в стэк
        stack_to_bits = list(bits_to(stack))  # Побитово записываем его в стэк
        encrypted_block = ''

        for i in range(0, len(stack_to_bits)//6):   #разбиваем циклом файл на блоки по 6 бит
            a = stack_to_bits[i * 6]                #считываем 1 бит в блоке
            b = stack_to_bits[i * 6 + 5]            #считываем 6 бит в блоке
            line_number = a + b                     #определяем номер строки берём 1 бит и 6 бит

            a = [1, 2, 3, 4]                                                 #это биты которые остались
            column_number = ""
            for j in a:                                                      #объединяем оставшиеся биты
                column_number += stack_to_bits[i * 6 + j]                    #определяем номер столбца

            intersection = S[int(line_number, 2)][int(column_number, 2)]     #число на пересечении номера строки и номера столбца в 10 системе исчисления
            intersection_to_bit = str(bin(intersection)[2:])                 #преобразуем число в двоичную строку

            if len(intersection_to_bit) == 1: intersection_to_bit = "000" + intersection_to_bit  #добавляем нули
            if len(intersection_to_bit) == 2:intersection_to_bit = "00" + intersection_to_bit
            if len(intersection_to_bit) == 3: intersection_to_bit = "0" + intersection_to_bit

            encrypted_block = encrypted_block + str(line_number) + intersection_to_bit   #зашифрованный блок

        adding_bits_to_the_stack = add_stack(stack_to_bits, encrypted_block)  #добавляем недостающие биты в блок

        intermediate_variable = []
        for i in range(0, len(adding_bits_to_the_stack) // 8):               #перекодировка оставшихся битов
            text_to_byte = ""
            for j in range(0, 8):
                text_to_byte += adding_bits_to_the_stack[8 * i + j]
            intermediate_variable_2 = int(text_to_byte, 2)
            intermediate_variable.append(intermediate_variable_2)
        stack = intermediate_variable                                                       # записываем всё в стек

        stack = bytearray(stack)

    with open(message, 'wb') as file:
        file.write(stack)
    print("Зашифрованно\n")


def decryp(message):                            #Дешифровка
    with open(message, 'rb') as file:
        stack = bytearray(file.read())          # Считываем файл в стэк
        stack_to_bits = list(bits_to(stack))    # Побитово записываем его в стэк
        encrypted_block = ''

        for i in range(0, len(stack_to_bits)//6):                       #разбиваем циклом файл на блоки по 6 бит
            a = stack_to_bits[i * 6 ]
            b = stack_to_bits[i * 6 + 1]
            line_number = a + b                                         #определяем номер строки
            reclaimed_element = ""

            for j in range(2, 6): reclaimed_element += stack_to_bits[i * 6 + j]       #восстанавливаем элемент

            search_column = S[int(line_number, 2)].index(int(reclaimed_element, 2))   #ищем столбец в S
            search_column = str(bin(search_column)[2:])

            if len(search_column) == 1: search_column = "000" + search_column         #добавляем нули
            if len(search_column) == 2: search_column = "00" + search_column
            if len(search_column) == 3: search_column = "0" + search_column

            line_number = str(line_number)
            encrypted_block = encrypted_block + line_number [0] + search_column + line_number[1]

        adding_bits_to_the_stack = add_stack(stack_to_bits, encrypted_block)

        intermediate_variable = []
        for i in range(0, len(adding_bits_to_the_stack) // 8):  # перекодировка оставшихся битов
            text_to_byte = ""
            for j in range(0, 8):
                text_to_byte += adding_bits_to_the_stack[8 * i + j]
            intermediate_variable_2 = int(text_to_byte, 2)
            intermediate_variable.append(intermediate_variable_2)
        stack = intermediate_variable  # записываем всё в стек

        stack = bytearray(stack)

    with open(message, 'wb') as file:
        file.write(stack)  # записываем данные из стека в файл

    print("Дешифрованно\n")


file_name = input("Введите имя файла: ")

while True:         #Меню программы
    print('1. Шифрование.')
    print('2. Дешифрование.')
    print('0. Выход из программы.')
    chose = input("Выберите пункт меню -> ")

    if chose == '1':
        encryp(file_name)
    elif chose == '2':
        decryp(file_name)
    elif chose == '0':
        break
    else:
        print("Такой команды в меню нет :(")
