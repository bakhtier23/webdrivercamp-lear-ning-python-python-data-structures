#!/usr/bin/python3
list_ = [5, 4, 3, 2, 1]
index = 2

def get_element(list_, index):
  if index < 0 or index >= len(list_):
    return None

  return list_[index]

element = get_element(list_, index)
if element is not None:
  print(f"The element retrieved is {element}")
else:
  print("The index is out of range.")
