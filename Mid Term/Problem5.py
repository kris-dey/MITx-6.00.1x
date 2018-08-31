# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 16:40:03 2018

@author: KrishanuDey
"""

aDict = {1: 1, 2: 1, 4: 3, 3:2}

def uniqueValues(aDict):
    '''
    aDict: a dictionary
    '''
    k = []
    for key in aDict.keys():
        occ = 0
        for value in aDict.values():
            if aDict[key] == value:
                occ+=1
        if occ == 1:
            k.append(key) 
    k.sort()
print(k)