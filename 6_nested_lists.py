#!/usr/bin/python3
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def print_matrix(matrix):
  """Prints a matrix of integers to the console.

  Args:
    matrix: A list of lists of integers.
  """

  for row in matrix:
    for element in row:
      print(element, end=" ")
    print()
print_matrix(matrix)
