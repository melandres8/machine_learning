#!/usr/bin/env python3
# calculates the shape of a matrix

def matrix_shape(matrix):
    """Shape of a matrix"""
    size_sub_item = 0
    size_sub = 0
    shape = []
    size = len(matrix)

    for item in matrix:
        size_sub = len(item)
        for sub_item in item:
            if isinstance(sub_item, list):
                size_sub_item = len(sub_item)

    shape.append(size)
    shape.append(size_sub)
    if size_sub_item != 0:
        shape.append(size_sub_item)
    return shape
