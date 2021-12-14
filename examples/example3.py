#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def cursing(depth):
    try:
        cursing(depth + 1)  # actually, re-cursing
    except RuntimeError as RE:
        print('I recursed {} times!'.format(depth))


if __name__ == '__main__':
    cursing(0)
