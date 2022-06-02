#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numbers

def test():
    number = int(input('введите число: '))
    if number > 0:
        positive()
    elif number < 0:
        negative()
def positive():
    print('положительное')
def negative():
    print('отрицательное')
test()
