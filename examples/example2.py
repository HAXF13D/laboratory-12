#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import lru_cache


@lru_cache
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 2) + fib(n - 1)


def main():
    n = int(input("Введите n = "))
    print(f"Вычисление {n} числа Фибоначи с помощью рекурсии = {fib(n)}")


if __name__ == '__main__':
    main()
