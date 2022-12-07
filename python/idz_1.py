#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    s = input("Введите предложение: ")

    cnt = s.count("o")

    print(f"There are {cnt} 'o' in {s}")