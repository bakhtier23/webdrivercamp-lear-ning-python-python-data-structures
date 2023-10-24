#!/usr/bin/python3
my_list = [5, 4, 3, 2, 1]

def is_even(number):
  return number % 2 == 0


def create_even_elements_tuple(list_of_numbers):
  
  even_elements_tuple = tuple(is_even(number) for number in list_of_numbers)
  return even_elements_tuple

even_elements_tuple = create_even_elements_tuple(my_list)

print(my_list)
print(even_elements_tuple)
