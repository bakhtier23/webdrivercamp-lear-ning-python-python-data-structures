#!/usr/bin/python3


def replace_element(list_, index, element_to_replace):
  if index < 0 or index >= len(list_):
    return
  list_[index] = element_to_replace

list_ = [5, 4, 3, 2, 1]
index = 1
element_to_replace = 5

replace_element(list_, index, element_to_replace)

print(list_)
