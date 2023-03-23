#!/usr/bin/python3
"""main file"""

makeChange = __import__('0-making_change').makeChange

print(makeChange([40, 1], 42))

print(makeChange([1,2,25], 37))

print(makeChange([1256, 54, 48, 16, 102], 1453))
