# хэш-функция
def h(x):
    polynomial = [False] * 7
    polynomial[0] = True
    polynomial[3] = True
    polynomial[6] = True

    binary_number = bin(x)[2:].zfill(8)
    stack = [False] * 7
    position = len(binary_number) - 1
    for i in range(6, -1, -1):
        stack[i] = binary_number[position] == "1"
        position -= 1

    for i in range(len(stack) - len(polynomial) + 1):
        if stack[i]:
            for j in range(len(polynomial)):
                stack[i + j] ^= polynomial[j]

    hash_function = "".join(str(int(bit)) for bit in stack[-3:])
    return int(hash_function, 2)


def digital_signature(m: str, p: int, g: int, x: int, k: int) -> tuple:
    # вычисление открытого ключа
    y = pow(g, x, p)

    # хэширование сообщения
    hashed_m = h(int.from_bytes(m.encode(), 'big'))

    # вычисление r
    r = pow(g, k, p)

    # вычисление k^-1
    k_inv = pow(k, -1, p-1)

    # вычисление s
    s = ((hashed_m - x*r) * k_inv) % (p-1)

    # вывод подписи
    return r, s

# параметры для подписи
p = 167
g = 10
x = 5
m = 'Hello world'
k = 23

# вывод подписи
print("Digital signature for message '{}': {}".format(m, digital_signature(m, p, g, x, k)))

# проверка электронной цифровой подписи
def verify_signature(m: str, p: int, g: int, y: int, signature: tuple) -> bool:
    r, s = signature

    # хэширование сообщения
    hashed_m = h(int.from_bytes(m.encode(), 'big'))

    # вычисление левой части уравнения
    left_part = (pow(y, r, p) * pow(r, s, p)) % p

    # вычисление правой части уравнения
    right_part = pow(g, hashed_m, p)

    # проверка подписи
    return left_part == right_part

# проверка подписи для сообщения
signature = digital_signature(m, p, g, x, k)
print("Verification of digital signature for message '{}': {}".format(m, verify_signature(m, p, g, pow(g, x, p), signature)))
