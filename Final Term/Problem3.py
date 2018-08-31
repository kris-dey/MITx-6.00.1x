# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 14:30:49 2018

@author: KrishanuDey
"""
def calc(a,b,c):
    return (6*a + 9*b + 20*c)

def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    for a in range(n):
       for b in range(n):
           for c in range(n):
               if calc(a,b,c) == n:
                 return True

    return False

