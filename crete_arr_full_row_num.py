def crete_arr_full_row_num(n,m):
  """
  Create 2D array NxM of ones
  Args:
    int: n
    int: m
  Returns:
    list: 2D list
  """
  arr = []
  for i in range(n):
    arr.append([i]*m)
  return arr