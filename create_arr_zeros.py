def create_arr_zeros(n,m):
  """
  Create 2D array NxM of zeros
  Args:
    int: n
    int: m
  Returns:
    list: 2D list
  """
  arr = []
  for i in range(n):
    arr.append([0]*m)
  return arr