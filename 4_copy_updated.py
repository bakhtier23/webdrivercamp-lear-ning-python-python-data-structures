#!/usr/bin/python3


def replace_element(list_, index, element_to_replace):
  if index < 0 or index >= len(list_):
    return
  list_[index] = element_to_replace

list_ = [5, 4, 3, 2, 1]
index = 1
element_to_replace = 5

# created a copy of the list
modified_list = list_.copy()

# replaced the element in the modified list
replace_element(modified_list, index, element_to_replace)

# Print the modified list and the original list
print(f"Copy:{modified_list}")
print(f"Original:{list_}")
