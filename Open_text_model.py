from re import sub
from math import log2

alfabet = ['a', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п',
           'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']  #Наш алфавит


def partition_counter(k):
    count = 0
    for i in range(len(split_line)):
        if len(split_line[i]) >= k: count += len(split_line[i])-k+1         # считаем количество разбиений
    return count


text = "Глухая пора листопада, Последних гусей косяки. Расстраиваться не надо: У страха глаза велики. Пусть ветер, рябину занянчив, Пугает ее перед сном. Порядок творенья обманчив, Как сказка с хорошим концом."
text = sub(r'[^\w\s]', '', text)                    # избавляемся от знаков препинания
text = text.lower()                                 # приводим строку в один регистр
split_line = text.split(" ")                        # разделяем строку по пробелам


def sipher(message):
    h_k_1 = 0
    h_k_2 = 0
    h_k_3 = 0
    h_k_4 = 0
    h_k_5 = 0
    probability = 0
    for i in range(len(alfabet)):
        probability = message.count(alfabet[i])/ partition_counter(1)        # находим вероятность буквы в строке
        if probability != 0: h_k_1 += probability * log2(probability)       # считаем энтропию
        for j in range(len(alfabet)):
            probability = message.count(alfabet[i] + alfabet[j]) / partition_counter(2) # находим вероятность буквы в строке
            if probability != 0: h_k_2 += probability * log2(probability)               # считаем энтропию
            for k in range(len(alfabet)):
                probability = message.count(alfabet[i] + alfabet[j] + alfabet[k]) / partition_counter(3)    # находим вероятность буквы в строке
                if probability != 0: h_k_3 += probability * log2(probability)                               # считаем энтропию
                for z in range(len(alfabet)):
                    probability = message.count(alfabet[i] + alfabet[j] + alfabet[k] + alfabet[z]) / partition_counter(4)   # находим вероятность буквы в строке
                    if probability != 0: h_k_4 += probability * log2(probability)                                           # считаем энтропию
                    for y in range(len(alfabet)):
                        probability = message.count(alfabet[i] + alfabet[j] + alfabet[k] + alfabet[z] + alfabet[y]) / partition_counter(5)  # находим вероятность буквы в строке
                        if probability != 0: h_k_5 += probability * log2(probability)                                                       # считаем энтропию

    print("H1 = ", abs(h_k_1), " k = 1" " H1/1 = ", abs(h_k_1 / 1))
    print("H2 = ", abs(h_k_2), " k = 2" " H1/2 = ", abs(h_k_2 / 2))
    print("H3 = ", abs(h_k_3), " k = 3" " H1/3 = ", abs(h_k_3 / 3))
    print("H4 = ", abs(h_k_4), " k = 4" " H1/4 = ", abs(h_k_4 / 4))
    print("H5 = ", abs(h_k_5), " k = 5" " H1/5 = ", abs(h_k_5 / 5))


sipher(text)
