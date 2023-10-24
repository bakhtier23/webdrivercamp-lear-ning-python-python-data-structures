#!/usr/bin/python3
def tuple_addition(first_arg, second_arg):
  if not first_arg and not second_arg:
    return (0, 0)

  first_element_of_first_arg = first_arg[0] if len(first_arg) >= 1 else 0
  second_element_of_first_arg = first_arg[1] if len(first_arg) >= 2 else 0

  first_element_of_second_arg = second_arg[0] if len(second_arg) >= 1 else 0
  second_element_of_second_arg = second_arg[1] if len(second_arg) >= 2 else 0

  sum_of_first_elements = first_element_of_first_arg + first_element_of_second_arg
  sum_of_second_elements = second_element_of_first_arg + second_element_of_second_arg

  return (sum_of_first_elements, sum_of_second_elements)

first_arg = (1, 99)
second_arg = (-1, 1)

result = tuple_addition(first_arg, second_arg)

print(result)
