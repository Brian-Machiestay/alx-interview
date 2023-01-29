#!/usr/bin/python3
"""A function that computes the pascal's triangle for a number"""


def pascal_triangle(n):
    """this function computes the pascal triangle for a number"""
    if n <= 0:
        return []
    triangle = [[1]]
    if n == 1:
        return triangle
    for i in range(n - 1):
        coefficient = []
        if len(triangle[i]) == 1:
            triangle.append([1, 1])
            continue
        for j in range(len(triangle[i])):
            if j == 0 or j == len(triangle[i]) - 1:
                coefficient.append(1)
            if j + 1 < len(triangle[i]):
                coefficient.append(triangle[i][j] + triangle[i][j + 1])
        triangle.append(coefficient)
    return triangle
