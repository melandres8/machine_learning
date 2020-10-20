#!/usr/bin/env python3
# Adds two arrays elements-wise

def add_arrays(arr1, arr2):
    """Adds two arrays"""
    arr = []
    if len(arr1) == len(arr2):
        for num1, num2 in zip(arr1, arr2):
            arr.append(num1 + num2)
    else:
        return None
    return arr
