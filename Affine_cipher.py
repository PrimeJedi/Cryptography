# m = 256 ,k = (9,16) а = 9, b = 16,

def affinity_character_encrip(message):
    translat = message
    result = (9 * translat + 16) % 256
    return result


def affinity_encrip(message):
    fill_stack = bytearray()
    i = 0

    file = open(message, 'rb')
    stack = bytearray(file.read())  #Записываем в стэк содержимое файла
    stack_e = tuple(stack)  #Применяем кортеж

    while i != len(stack_e):
        fill_stack.append(affinity_character_encrip(stack_e[i]))  #Шифрование
        i += 1
    file = open(message, 'wb')  #Открываем файл для записи в него
    for i in range(len(fill_stack)):
        file.write(bytes([fill_stack[i]]))  #Из стека записываем в файл
    print("Готово\n")
    file.close()


def affinity_character_deсrip(message):
    translat = message
    result = 57*(translat - 16) % 256
    return result


def affinity_decrip(message):
    fill_stack = bytearray()
    i = 0

    file = open(message, 'rb')
    stack = bytearray(file.read())  #Записываем в стэк содержимое файла
    stack_e = tuple(stack)  #Применяем кортеж

    while i != len(stack_e):
        stack_f = affinity_character_deсrip(stack_e[i])  #Дешифрование
        fill_stack.append(stack_f)
        i += 1
    file = open(message, 'wb')  #Открываем файл для записи в него
    for i in range(len(fill_stack)):
        file.write(bytes([fill_stack[i]]))  #Из стека записываем в файл
    print("Готово\n")
    file.close()


file_name = input("Введите имя файла: ")

while True:
    print("[1] - Шифрование.")
    print("[2] - Дешифрование.")
    print("[0] - Выход.")
    menu_item = input("Выберите что вы хотите сделать ->")

    if menu_item == "1":
        affinity_encrip(file_name)
    elif menu_item == "2":
        affinity_decrip(file_name)
    elif menu_item == "0":
        break
    else:
        print("Такое команды нет:( давай попробуем ещё раз\n")
