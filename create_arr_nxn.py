def create_arr_nxn(n,k):
  """
  Create 2D array NxN of k
  Args:
    int: n
    int: k
  Returns:
    list: 2D list
  """
  arr = []
  for i in range(n):
    arr.append([k]*n)
  return arr
  