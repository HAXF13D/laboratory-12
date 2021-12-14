#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


def rec_func(a, i=0, k=0):
    if len(a) == k:
        print("В списке нет отрицательных чисел", file=sys.stderr)
        exit(0)
    elif a[i] < 0:
        return 0, k
    else:
        return a[i] + rec_func(a, i + 1, k + 1)[0], rec_func(a, i + 1, k + 1)[1]


def main():
    array = list(map(int, input("Введите список:\n").split()))
    summa, amount = rec_func(array)
    print(f"Сумма чисел = {summa}")
    print(f"Количество чисел = {amount}")


if __name__ == '__main__':
    main()
