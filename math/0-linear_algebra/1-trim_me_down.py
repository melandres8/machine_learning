#!/usr/bin/env python3
# the_middle should be a 2D matrix containing the 3rd and 4th columns of matrix
matrix = [[1, 3, 9, 4, 5, 8], [2, 4, 7, 3, 4, 0], [0, 3, 4, 6, 1, 5]]
the_middle = []
# your code here
for item in matrix:
    the_middle.append(item[2:4])

print("The middle columns of the matrix are: {}".format(the_middle))
