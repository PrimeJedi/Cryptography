import math
# Функция gcd находит наибольший общий делитель двух чисел


def gcd(a: int, b: int) -> int:
    """
    Находит наибольший общий делитель двух чисел
    """
    while b != 0:
        a, b = b, a % b
    return a

# Функция extended_gcd находит наибольший общий делитель двух чисел и их коэффициенты Безу


def extended_gcd(a: int, b: int) -> tuple:
    """
    Находит наибольший общий делитель двух чисел и их коэффициенты Безу
    """
    # Если первый аргумент равен 0, то возвращается кортеж из второго аргумента, 0 и 1
    if a == 0:
        return b, 0, 1
    # Иначе вычисляется наибольший общий делитель и коэффициенты Безу
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x

# Функция modular_inverse находит обратный элемент по модулю


def modular_inverse(a: int, m: int) -> int:
    """
    Находит обратный элемент по модулю
    """
    # Вызывается функция extended_gcd для нахождения наибольшего общего делителя и коэффициентов Безу
    gcd, x, _ = extended_gcd(a, m)
    # Если наибольший общий делитель не равен 1, то обратный элемент не существует
    if gcd != 1:
        raise ValueError("Modular inverse does not exist")
    # Иначе возвращается обратный элемент по модулю
    return x % m

# Функция factorize разлагает число на простые множители


def factorize(N: int) -> list:
    """
    Разлагает число на простые множители
    """
    factors = []
    # Пока число делится на 2, добавляется множитель 2 и число делится на 2
    while N % 2 == 0:
        factors.append(2)
        N //= 2
    # Вычисляется квадратный корень из числа
    sqrt_N = int(math.isqrt(N))
    # Для всех нечетных чисел от 3 до квадратного корня из числа
    for i in range(3, sqrt_N + 1, 2):
        # Пока число делится на i, добавляется множитель i и число делится на i
        while N % i == 0:
            factors.append(i)
            N //= i
    # Если остаток от деления числа N на sqrt_N равен 0, то добавляется множитель sqrt_N
    if N > 2:
        factors.append(N)
    return factors

# Функция decrypt расшифровывает сообщение с помощью закрытого ключа


def decrypt(ciphertext: int, private_key: tuple) -> int:
    """
    Расшифровывает сообщение с помощью закрытого ключа
    """
    # Извлекаются значения N и d из закрытого ключа
    N, d = private_key
    # Вычисляется расшифрованное сообщение
    plaintext = pow(ciphertext, d, N)
    return plaintext

# Вводятся значения N, e и зашифрованного сообщения


N = int(input("Введите значение N: "))
e = int(input("Введите значение e: "))
ciphertext = int(input("Введите зашифрованное сообщение: "))

# Число N разлагается на простые множители, из которых извлекаются p и q

factors = factorize(N)
p, q = factors[0], factors[1]

# Выводятся факторы числа N

print("Факторы N:", factors)

# Вычисляется значение функции Эйлера от числа N

phi_N = (p - 1) * (q - 1)

# Вычисляется значение d с помощью функции modular_inverse

d = modular_inverse(e, phi_N)

# Создается закрытый ключ

private_key = (N, d)

# Расшифровывается сообщение с помощью закрытого ключа

plaintext = decrypt(ciphertext, private_key)

# Выводятся зашифрованное и расшифрованное сообщения

print("Зашифрованное сообщение:", ciphertext)
print("Расшифрованное сообщение:", plaintext)
