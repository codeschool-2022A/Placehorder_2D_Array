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
  temp = []
  for i in range(n):
    for j in range(1, m+1):
      temp.append(i*m+j)
    arr.append(temp)
    temp = []
  return arr

print(crete_arr_ord_num(3,4))