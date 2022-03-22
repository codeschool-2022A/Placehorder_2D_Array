def create_arr_ones(n,m):
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
    arr.append([1]*m)
  return arr