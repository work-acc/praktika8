#!/usr/bin/env python 3
# -*- config: utf-8 -*-

# Решите задачу: создайте словарь, где ключами являются числа, а значениями – строки.
# Примените к нему метод items(), c с помощью полученного объекта dict_items создайте
# новый словарь, "обратный" исходному, т. е. ключами являются строки, а значениями – числа.

if __name__ == '__main__':
    dict1 = {1: "один", 2: "два", 3: "три", 4: "четыре", }
    dict2 = {j: i for i, j in dict1.items()}
    print(dict1, dict2)