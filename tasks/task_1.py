#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import timeit


def factorial_rec(n, acc=1):
    if n == 0:
        return acc
    return factorial_rec(n - 1, n * acc)


def fib_rec(i, current=0, next=1):
    if i == 0:
        return current
    else:
        return fib_rec(i - 1, next, current + next)


def factorial_iter(n):
    if n == 0 or n == 1:
        return 1
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


def fib_iter(n):
    a = 0
    b = 1
    for i in range(n):
        c = a + b
        a = b
        b = c
    return a


def main():

    number = 500

    start_time = timeit.default_timer()
    factorial_rec(number)
    print("Execution factorial_rec time is :", timeit.default_timer() - start_time)

    start_time = timeit.default_timer()
    factorial_iter(number)
    print("Execution factorial_iter time is :", timeit.default_timer() - start_time)

    start_time = timeit.default_timer()
    fib_rec(number)
    print("Execution fib_rec time is :", timeit.default_timer() - start_time)

    start_time = timeit.default_timer()
    fib_iter(number)
    print("Execution fib_iter time is :", timeit.default_timer() - start_time)


if __name__ == '__main__':
    main()