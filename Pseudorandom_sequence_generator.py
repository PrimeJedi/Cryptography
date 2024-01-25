# (a = 81,c = 25,m = 197,x(0) = 16)

def linear_congruent_oscillator(a, c, m, x0):
    length_period = 0
    string = ''
    array = []

    x = x0
    binary_number = bin(x)[2:]

    length_period += len(binary_number)
    string += binary_number

    print("Последовательность ПСЧ в 10-ом представлении:")

    array.append(x)   #первый элемент в 10-ом представлении
    print(x, end=' ')

    while True:
        x = (a * x + c) % m
        if x == x0:
            break
        array.append(x) #все остальные элементы в 10-ом представлении
        print(x, end=' ')

        binary_number = bin(x)[2:]
        length_period += len(binary_number)
        string += binary_number

        count_odd_number = 0
        count_even_number = 0

        for i in range(1, (len(string) // 8 + 1)):  #количество чётных нечётных элементов
            if string[i * 8 - 1] == '1':
                count_odd_number += 1
            else:
                count_even_number += 1

    print("\n\nПоследовательность ПСЧ в 2-ом представлении: ")
    for i in range(len(array)):                           #все элементы в 2-ом представлении
        string += bin(array[i])[2:]
        print(bin(array[i])[2:], end=' ')

    print("\n\nДлинна периода в битах ->", length_period)
    print("Количество чётных чисел ->", count_even_number, ", количество нечётных чисел ->", count_odd_number)
    print("Количество нулей ->", string.count('0'), ", количество единиц ->", string.count('1'))


linear_congruent_oscillator(57, 56, 181, 11)
