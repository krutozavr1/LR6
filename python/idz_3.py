#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    s = "иинформаця"

    correct_s = s[1:len(s) - 1] + s[0] + s[len(s) - 1]

    print(correct_s)
