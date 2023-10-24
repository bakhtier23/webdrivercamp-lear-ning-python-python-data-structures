def tuple_return(arg):
  if len(arg) == 0:
    return (0, None)
  else:
    return (len(arg), arg[0])

list_ = [1, 2, 3, 4, 5]

result = tuple_return(list_)
print(result)
