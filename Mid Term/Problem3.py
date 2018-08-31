# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 16:15:20 2018

@author: KrishanuDey
"""

def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    diff = 0
    exp = -1
    e = 0
    wh = True
    lDiff = 999999
    while wh:
        exp+=1
        
        diff = abs(num - (base**exp))
        if diff < lDiff:
            e = exp
        if num < (base**(exp - 1)):
            wh = False
        lDiff = diff
    return e

print(closest_power(4,1))