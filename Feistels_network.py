def bits_to(stack):                                         #перевод текста в двоичный код
    bits = ""
    for i in range(0, len(stack)):
        bits += bin(stack[i])[2:].zfill(8)
    return bits


def add_stack(stack_to_bits,encrypted_block):               #добавляем недостающие биты
    for i in range(len(stack_to_bits) % 16, 0, -1):
        encrypted_block += stack_to_bits[len(stack_to_bits) - i]
    return encrypted_block


def obtaining_the_key():                # у нас будет постоянный ключ который равен 10 как и номер варианта
    key = list("{0:08b}".format(5))     # преобразуем ключ
    for i in range(0, len(key)):
        key[i] = int(key[i])
    return key                          # на выходе получаем список длинной 8 из единиц и нулей
                                        # каждый раунд шифрования разделяет наш шифруемый блок на 2 блока L_i-1 и R_i-1 c соответсвующими индексами
                                        #     0 - 7 и 8 - 15
def round_of_encryption(bits, key):     # тут реализуем функцию f=(x<<2)+(x<<6)+k
    round_result = []
    for i in range(0, 8):                           # переносим значение из R_i-1 в L_i
        round_result.append(int(bits[i + 8]))
    for i in range(0, 8):                           # В R_i оставляем нули
        round_result.append(0)

    for i in range(0, 8):
        left_index = i + 10                       # получаем левый индекс элементов в R(i-1) x<<2
        if left_index <= 15:                      # получаем элемент по индексу который получен в результате смещения x<<2
            item_by_left_index = bits[left_index]
        else:
            left_index = left_index - 8
            item_by_left_index = bits[left_index]

        right_index = i + 8 + 6                             # получаем правый индекс элементов в R(i-1) x<<6
        if right_index <= 15:                             # получаем элемент по индексу который получен в результате смещения x<<6
            item_by_right_index = bits[right_index]
        else:
            right_index = right_index - 8
            item_by_right_index = bits[right_index]

        round_result[i + 8] = int(bits[i], 2) ^ int(item_by_left_index, 2) ^ int(item_by_right_index, 2) ^ key[i]  #Побитовый ксор
        # получаем R_i

        for i in range(0, len(round_result)):
            round_result[i] = str(round_result[i])

    return round_result
                                                # каждый раунд дешифрования  разделяем наш зашифрованный блок на два блока L_i и R_i c соответсвующими индексами
                                                # 0 -7 и 8 - 15
def round_of_decryption(bits, key):             # тут реализуем обратную функцию f=(x>>2)+(x>>6)+k
    round_result = []
    for i in range(0, 8):                       # ячейка с конечным результатов просто заполняем её нулями
        round_result.append(0)
    for i in range(0, 8):                       # переносим значение из L_i в R_i-1
        round_result.append(int(bits[i]))

    for i in range(0, 8):
        left_index = i + 2                      # получаем левый индекс элементов в R(i) x>>2
        if left_index <= 7:                   # получаем элемент по индексу который получен в результате смещения x>>2
            item_by_left_index = bits[left_index]
        else:
            left_index = left_index - 8
            item_by_left_index = bits[left_index]

        item_by_right_index = 0
        right_index = i + 6                     # получаем правый индекс элементов в R(i) x>>6
        if right_index <= 7:                  # получаем элемент по индексу который получен в результате смещения x>>6
            item_by_right_index = bits[right_index]
        else:
            right_index = right_index - 8
            item_by_right_index = bits[right_index]

        round_result[i] = int(bits[i + 8], 2) ^ int(item_by_left_index, 2) ^ int(item_by_right_index, 2) ^ key[i] #побитовый ксор
        # получаем L_i-1

    for i in range(0, len(round_result)):
        round_result[i] = str(round_result[i])
    return round_result


def encryp(message):  # ШИФРОВАНИЕ
    with open(message, 'rb') as file:
        stack = bytearray(file.read())        # Считываем файл в стэк
        stack_to_bits = list(bits_to(stack))  # Побитово записываем его в стэк

        identical_keys = obtaining_the_key()  # Генерируем ключ шифрования
        result = []
        for i in range(0, len(stack_to_bits) // 16):
            r_o_e = []
            for j in range(0, 16):
                r_o_e.append(stack_to_bits[16 * i + j])
            r_o_e = round_of_encryption(r_o_e, identical_keys)        # 1-ый раунд
            r_o_e = round_of_encryption(r_o_e, identical_keys)        # 2-ой раунд
            r_o_e = round_of_encryption(r_o_e, identical_keys)        # 3-ий раунд

            result += r_o_e

        adding_bits_to_the_stack = add_stack(stack_to_bits, result) # добавляем недостающие биты в блок

        intermediate_variable = []
        for i in range(0, len(adding_bits_to_the_stack) // 8):  # перекодировка оставшихся битов
            text_to_byte = ""
            for j in range(0, 8):
                text_to_byte += adding_bits_to_the_stack[8 * i + j]
            intermediate_variable_2 = int(text_to_byte, 2)
            intermediate_variable.append(intermediate_variable_2)
        stack = intermediate_variable                           # записываем всё в стек
        stack = bytearray(stack)

    with open(message, 'wb') as file:                           # открываем файл
        file.write(stack)                                       # записываем всё в файл.
    print("Зашифрованно")


def decryp(path):
    with open(path, 'rb') as file:
        stack = bytearray(file.read())        # Считываем файл в стэк
        stack_to_bits = list(bits_to(stack))  # Побитово записываем его в стэк

        identical_keys = obtaining_the_key()  # Генерируем ключ расшифрования

        result = []
        for i in range(0, len(stack_to_bits) // 16):
            r_o_d = []
            for j in range(0, 16):
                r_o_d.append(stack_to_bits[16 * i + j])
            r_o_d = round_of_decryption(r_o_d, identical_keys)  # 1-ый раунд
            r_o_d = round_of_decryption(r_o_d, identical_keys)  # 2-ой раунд
            r_o_d = round_of_decryption(r_o_d, identical_keys)  # 3-ий раунд
            result += r_o_d

        adding_bits_to_the_stack = add_stack(stack_to_bits, result)

        intermediate_variable = []
        for i in range(0, len(adding_bits_to_the_stack) // 8):  # перекодировка оставшихся битов
            text_to_byte = ""
            for j in range(0, 8):
                text_to_byte += adding_bits_to_the_stack[8 * i + j]
            intermediate_variable_2 = int(text_to_byte, 2)
            intermediate_variable.append(intermediate_variable_2)
        stack = intermediate_variable  # записываем всё в стек
        stack = bytearray(stack)

    with open(path, 'wb') as file:
        file.write(stack)
    print("Дешифрованно")


file_name = input("Введите имя файла: ")


print("[1]Шифрование")
print("[2]Дешифровка")
menu = int(input("Введите пункт меню: "))
if menu == 1:
    encryp(file_name)

if menu == 2:
    decryp(file_name)
