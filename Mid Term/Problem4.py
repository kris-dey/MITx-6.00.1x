# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 16:36:31 2018

@author: KrishanuDey
"""

listA = [1, 2, 3] 
listB = [4, 5, 6]


def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    dt = 0
    for i in range(len(listA)):
        dt += (listA[i]*listB[i]) 
    return dt

print(dt)