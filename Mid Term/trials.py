# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 15:55:35 2018

@author: KrishanuDey
"""
#
#def f(x):  
#    while x > 3:
#        print("while")
#        f(x+1)
#
#x = -1
#f(x)
#print("end")
# 
#
#
#x = "asdf"
#y = "qwerty"
#
#(x,y)=(y,x)
#

#i = -1
#j = -9
#
#while i >= 0:
#    while j >= 0:
#        print(i, j)
#
#print("end")
#
#s = ("iBoy", "iGirl", "iQ", "iC","iPaid","iPad")
#for thing in s :
#    if s == 'iQ':
#        print("found it")


def Square(x):
    return SquareHelper(abs(x), abs(x))

def SquareHelper(n, x):
    if n == 0:
        return 0
    return SquareHelper(n-1, x) + x


print(Square(-5))

























