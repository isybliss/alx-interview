#!/usr/bin/python3
"""
Pascal triangle
"""


def pascal_triangle(n):
    """
    return a list of lists of integers representing
    the pascal triangle
    """
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        tri = triangle[-1]
        """the value of tri is the last list index in triangle"""
        tmp = [1]
        """ 1 is a constant first digit in each nested list"""
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        triangle.append(tmp)
    return triangle
