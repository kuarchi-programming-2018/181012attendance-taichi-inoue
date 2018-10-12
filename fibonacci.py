# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 16:35:06 2018

@author: Inoue
"""

#フィボナッチ数列の表示
def fib(i):
    x,y = 0,1
    for i in range(0,i):
        x,y = y,x+y
    return x