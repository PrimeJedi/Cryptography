register_value = int(input("Задайте 8-ми битное значение регистра: "))
characteristic_function, register_size = [1, 1, 1, 0, 0, 0, 1, 0, 1], 8


def right_shift(value):
    '''
        Функция right_shift, которая сдвигает значение регистра на один бит вправо с помощью заданной характеристической функции
    '''
    new_bit = sum([bit_value(value, n) * characteristic_function[n] for n in range(len(characteristic_function))]) % 2
    return (value >> 1) | (new_bit << (register_size - 1))


def bit_value(value, position):
    '''
        Функция bit_value, которая получает значение бита по заданной позиции из заданного значения
    '''
    return (value >> position) & 1


length_period, generated_sequence = 0, []   #генерируем последовательность значений, используя заданный размер и начальное значение регистра
while True:
    generated_sequence.append(register_value % 256)
    register_value = right_shift(register_value)
    length_period += 1
    if register_value == int('11011011', 2):
        break

period_in_bits = length_period * 8


def results_and_show(message):
    binary_sequence = [bin(value)[2:].zfill(8) for value in message]                  #бинарная последовательность
    print('Сгенерированная последовательность в двоичном представлении -> cгенерированная последовательность в десятичном представлении')
    for i in range(length_period):
        if i % 9 == 0:
            print(binary_sequence[i], " - > ", message[i])
        else:
            print(binary_sequence[i], " - > ", message[i], end=",   ")

    even_count = sum([1 for value in message if value % 2 == 0])         #подсчёт нечётных чисел
    odd_count = sum([1 for value in message if value % 2 == 1])          #подсчёт чётных чисел
    print('\nКоличество нечётных элементов:', even_count, ' Количество чётных элементов:', odd_count)
    zero_count = sum([binary_value.count('0') for binary_value in binary_sequence]) #подсчёт нулей
    one_count = sum([binary_value.count('1') for binary_value in binary_sequence])  #подсчёт единиц
    print('Количество нулей:', zero_count, ' Количество единиц:', one_count)


results_and_show(generated_sequence)
print('Период последовательности в битах:', period_in_bits)
print('Характеристическая функция:', characteristic_function)
