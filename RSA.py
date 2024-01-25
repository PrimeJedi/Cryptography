import random


# Функция для нахождения НОД двух чисел
def gcd(a, b):
    # Пока b не равно 0, находим остаток от деления a на b и присваиваем его b, а сам же b присваиваем a
    while b != 0:
        a, b = b, a % b
    # Возвращаем a - результат вычисления НОД
    return a


# Функция для нахождения расширенного НОД двух чисел
def gcd_extended(a, b):
    # Если a равно 0, то возвращаем кортеж (b, 0, 1)
    if a == 0:
        return (b, 0, 1)
    # Если a не равно 0, то рекурсивно вызываем эту же функцию с аргументами (b % a, a) и присваиваем результат соответствующим переменным
    else:
        g, y, x = gcd_extended(b % a, a)
        # Возвращаем кортеж (g, x - (b // a) * y, y) - результат вычисления расширенного НОД
        return (g, x - (b // a) * y, y)


# Функция для нахождения обратного элемента по модулю
def mod_inv(a, m):
    # Вызываем функцию gcd_extended с аргументами (a, m) и присваиваем результат соответствующим переменным
    g, x, y = gcd_extended(a, m)
    # Если НОД a и m не равен 1, то возникает исключение
    if g != 1:
        raise ValueError('Решение не существует')
    # Возвращаем x % m - результат вычисления обратного элемента по модулю
    return x % m


# функция для генерации открытого и закрытого ключей
def gcd_and_gen_keys(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randrange(1, phi)  # выбираем число e взаимно простое с phi
    while gcd(e, phi) != 1:
        e = random.randrange(1, phi)

    d = mod_inv(e, phi)  # находим число d, обратное к e по модулю phi
    return ((e, n), (d, n))


# функция для шифрования сообщения
def encrypt(message, public_key):
    e, n = public_key
    return pow(message, e, n)


# функция для расшифрования сообщения
def decrypt(ciphertext, private_key):
    d, n = private_key
    return pow(ciphertext, d, n)


# функция для генерации нескольких пар ключей
def generate_multiple_keys(p, q, num_keys):
    keys = []
    for _ in range(int(num_keys)):
        keys.append(gcd_and_gen_keys(p, q))
    return keys


p, q = 167, 311  # задаем значения p, q

num_keys = input("Введите количество пар ключей: ")  # генерируем ключи
keys = generate_multiple_keys(p, q, int(num_keys))

print(f"Сгенерировано {num_keys} пары ключей:")  # выводим на экран сгенерированные ключи
for i, key_pair in enumerate(keys):
    public_key, private_key = key_pair
    print("Пара", i + 1, ":", " Открытый ключ", public_key, " Закрытый ключ", private_key)


choice = int(input("Выберите пару: "))  # запрашиваем у пользователя номер пары ключей для использования
if choice > 1 or choice < int(num_keys):
    public_key, private_key = keys[choice - 1]  # получаем выбранную пару ключей
    message = input("Введите сообщение: ").upper()  # запрашиваем у пользователя сообщение для шифрования
    message_nums = [ord(c) - ord('А') + 10 if c != " " else 99 for c in message]  # преобразуем сообщение в числовой вид
    ciphertext = [encrypt(m, public_key) for m in message_nums]  # шифруем сообщение
    decrypted_nums = [decrypt(c, private_key) for c in ciphertext]  # расшифровываем сообщение
    decrypted_message = "".join([chr(n - 10 + ord('А')) if n != 99 else " " for n in decrypted_nums])
    print("Исходное сообщение:", message)
    print("Сообщение в числовом виде:", message_nums)
    print("Зашифрованный текст:", ciphertext)
    print("Расшифрованное сообщение:", decrypted_message)
