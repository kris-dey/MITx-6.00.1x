# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 14:53:14 2018

@author: KrishanuDey
"""

def longestRun(L):
    mLen = -1
    length = 1
    for i in range(len(L)-1):
        if L[i] <= L[i+1]:
            length+=1
        elif L[i] > L[i+1]:
            if length > mLen:
                mLen = length
                length = 1
    if length > mLen:
            mLen = length
    return mLen


L = [10, 8, 9, 5, 6, 7, 1, 2, 3, 4]
print(longestRun(L))