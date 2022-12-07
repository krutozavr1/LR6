#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    s = input("Введите предложение: ")

    new_s = ""

    for i in range(len(s)):
        if i % 2 == 1:
            new_s += "ы"
        else:
            new_s += s[i]

    print(new_s)
