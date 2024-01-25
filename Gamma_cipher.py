def read_file(filename): #функция для чтения содержимого файла в бинарном режиме
    with open(filename, 'rb') as f:
        content = f.read()
    return content


def write_file(filename, content): #функция для записи содержимого в файл в бинарном режиме
    with open(filename, 'wb') as f:
        f.write(content)


def linear_feedback_shift_register(register_value, characteristic_function): #функция реализующая линейный регистр сдвига
    register_size = len(characteristic_function)
    # находим новый бит
    new_bit = sum([register_value >> n & 1 for n in range(register_size) if characteristic_function[n]]) % 2
    # обновляем значение регистра
    register_value = (register_value >> 1) | (new_bit << (register_size - 1))
    return register_value


#функция генерации потока ключей на основе линейного регистра сдвига
def generate_keystream(register_value, characteristic_function, length):
    # инициализируем пустой байтовый объект, который будет хранить поток ключей
    keystream = b''
    # генерируем поток ключей длиной length
    for i in range(length):
        # обновляем значение регистра
        register_value = linear_feedback_shift_register(register_value, characteristic_function)
        # добавляем младший байт регистра в поток ключей
        keystream += bytes([register_value & 0xff])
        # возвращаем поток ключей
    return keystream


# keystream - это последовательность случайных битов, сгенерированных из ключа и переданных в функцию generate_keystream
# ciphertext - это зашифрованный текст, полученный путем применения операции XOR между plaintext и keystream
def encrypt(plaintext, key):
    # генерируем keystream из ключа и передаем его в функцию generate_keystream, также передаем дополнительный параметр
    keystream = generate_keystream(key, [1, 0, 1, 0, 0, 0, 0, 1, 1], len(plaintext))
    # применяем операцию XOR между каждым байтом plaintext и соответствующим байтом keystream, результат записываем в ciphertext
    ciphertext = bytes([plaintext[i] ^ keystream[i] for i in range(len(plaintext))])
    # возвращаем зашифрованный текст
    return ciphertext


# keystream - это последовательность случайных битов, сгенерированных из ключа и переданных в функцию generate_keystream
# plaintext - это расшифрованный текст, полученный путем применения операции XOR между ciphertext и keystream
def decrypt(ciphertext, key):
    # генерируем keystream из ключа и передаем его в функцию generate_keystream, также передаем дополнительный параметр - длину ciphertext
    keystream = generate_keystream(key, [1, 1, 1, 0, 0, 0, 1, 0, 1], len(ciphertext))
    # применяем операцию XOR между каждым байтом ciphertext и соответствующим байтом keystream, результат записываем в plaintext
    plaintext = bytes([ciphertext[i] ^ keystream[i] for i in range(len(ciphertext))])
    # возвращаем расшифрованный текст
    return plaintext


filename = input("Введите имя файла: ")
key = int(input("Введите начальное значение регистра: "))

content = read_file(filename)
ciphertext = encrypt(content, key)
write_file(filename + ".encrypted", ciphertext)

print("Файл успешно зашифрован.\n")


filename_encrypted = filename + ".encrypted"
key = int(input("Введите начальное значение регистра: "))

content_encrypted = read_file(filename_encrypted)
plaintext = decrypt(content_encrypted, key)
write_file(filename + ".decrypted", plaintext)

print("Файл успешно расшифрован.")

