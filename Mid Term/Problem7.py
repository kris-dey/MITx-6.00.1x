# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 17:17:58 2018

@author: KrishanuDey
"""

def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements. Remaining elements in L
            should be in the same order.
    Returns the length of L after mutation
    """
    t = []
    for thing in L:
        if f(thing):
            t.append(thing)    
    L[:] = t
    return len(L)

def f(s):
    return 'a' in s
      
L = ['a', 'b', 'a']
print (satisfiesF(L))
print (L)