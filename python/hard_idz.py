#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import re

if __name__ == '__main__':
    s = input("Введите предложение: ")

    list_of_words = re.split("\W", s)

    for str in list_of_words:
        if str != "привет":
            print(str)
