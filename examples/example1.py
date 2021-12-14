#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def recursion(n):
    if n == 1:
        return 1
    return n + recursion(n - 1)


def main():
    n = int(input("Введите n = "))
    summa = 0
    for i in range(1, n + 1):
        summa += i
    print(f"Сумма посчитаная без рекурсии = {summa}")
    print(f"Сумма посчитанная с помощью рекурсии = {recursion(n)}")


if __name__ == '__main__':
    main()
