def get_hash_function(number: int) -> str:
    # Задаем полином для хэш-функции
    polynomial = [False] * 7
    polynomial[0] = True
    polynomial[3] = True
    polynomial[6] = True

    # Преобразуем число в двоичное представление и записываем его в стек
    binary_number = bin(number)[2:].zfill(8)
    stack = [False] * 7
    position = len(binary_number) - 1
    for i in range(6, -1, -1):
        stack[i] = binary_number[position] == "1"
        position -= 1

    # Применяем полином для получения хэш-функции
    for i in range(len(stack) - len(polynomial) + 1):
        if stack[i]:
            for j in range(len(polynomial)):
                stack[i + j] ^= polynomial[j]

    # Преобразуем полученную хэш-функцию в строку и возвращаем ее
    hash_function = "".join(str(int(bit)) for bit in stack[-3:])
    return hash_function


def calculate_the_hash_function():
    # Считываем число от пользователя и вычисляем для него хэш-функцию
    number = int(input("Введите число (0-255): "))
    hash_function = get_hash_function(number)
    print(f"Хэш-функция для числа {number}: {hash_function}")


def iterating_over_all_numbers_and_finding_all_collisions():
    # Перебираем все числа от 0 до 255 и находим для них хэш-функции
    # Если хэш-функция уже встречалась, то добавляем число в список коллизий
    # Выводим все хэш-функции и соответствующие им числа-коллизии
    collisions = {}
    for i in range(256):
        hash_function = get_hash_function(i)
        if hash_function not in collisions:
            collisions[hash_function] = [i]
        else:
            collisions[hash_function].append(i)

    for hash_function, numbers in collisions.items():
        print(f"Хэш-функция {hash_function} имеет коллизии для чисел: {', '.join(map(str, numbers))}")


def execute():
    # Основной цикл программы
    while True:
        print("[1]. Вычислить ХЭШ-функцию для сообщения")
        print("[2]. Найти все коллизии для хэш функции.")
        print("[0]. Выход из программы.")
        try:
            # Считываем выбор пользователя и выполняем соответствующую операцию
            choice = int(input("Выберите пункт меню -> : "))
            if choice == 1:
                calculate_the_hash_function()
            elif choice == 2:
                iterating_over_all_numbers_and_finding_all_collisions()
            elif choice == 0:
                break
        except ValueError:
            print("Некорректный ввод.")


if __name__ == '__main__':
    execute()


    def get_hash_function(number: int) -> str:
        # Задаем полином для хэш-функции
        polynomial = [False] * 7
        polynomial[0] = True
        polynomial[1] = True
        polynomial[2] = True
        polynomial[4] = True

        # Преобразуем число в двоичное представление и записываем его в стек
        binary_number = bin(number)[2:].zfill(8)
        stack = [False] * 7
        position = len(binary_number) - 1
        for i in range(6, -1, -1):
            stack[i] = binary_number[position] == "1"
            position -= 1

        # Применяем полином для получения хэш-функции
        for i in range(len(stack) - len(polynomial) + 1):
            if stack[i]:
                for j in range(len(polynomial)):
                    stack[i + j] ^= polynomial[j]

        # Преобразуем полученную хэш-функцию в строку и возвращаем ее
        hash_function = "".join(str(int(bit)) for bit in stack[-3:])
        return hash_function


    def calculate_the_hash_function():
        # Считываем число от пользователя и вычисляем для него хэш-функцию
        number = int(input("Введите число (0-255): "))
        hash_function = get_hash_function(number)
        print(f"Хэш-функция для числа {number}: {hash_function}")


    def iterating_over_all_numbers_and_finding_all_collisions():
        # Перебираем все числа от 0 до 255 и находим для них хэш-функции
        # Если хэш-функция уже встречалась, то добавляем число в список коллизий
        # Выводим все хэш-функции и соответствующие им числа-коллизии
        collisions = {}
        for i in range(256):
            hash_function = get_hash_function(i)
            if hash_function not in collisions:
                collisions[hash_function] = [i]
            else:
                collisions[hash_function].append(i)

        for hash_function, numbers in collisions.items():
            print(f"Хэш-функция {hash_function} имеет коллизии для чисел: {', '.join(map(str, numbers))}")


    def execute():
        # Основной цикл программы
        while True:
            print("[1]. Вычислить ХЭШ-функцию для сообщения")
            print("[2]. Найти все коллизии для хэш функции.")
            print("[0]. Выход из программы.")
            try:
                # Считываем выбор пользователя и выполняем соответствующую операцию
                choice = int(input("Выберите пункт меню -> : "))
                if choice == 1:
                    calculate_the_hash_function()
                elif choice == 2:
                    iterating_over_all_numbers_and_finding_all_collisions()
                elif choice == 0:
                    break
            except ValueError:
                print("Некорректный ввод.")


    if __name__ == '__main__':
        execute()
