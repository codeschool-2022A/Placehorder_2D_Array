def crete_arr_ord_num(n,m):
  """
  Create 2D array NxM
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