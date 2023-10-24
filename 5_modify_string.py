#!/usr/bin/python3

string = """AbraCadabra
A new string voila!"""

def remove_char(some_string):
  """Removes all characters a (both lower and upper) from the string.

  Args:
    some_string: A string.

  Returns:
    A string with all characters a removed.
  """

  new_string = ""
  for char in some_string:
    if char != "a" and char != "A":
      new_string += char
  return new_string


# Print the modified string
print(remove_char(string))
