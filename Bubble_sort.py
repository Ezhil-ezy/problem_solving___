# [22, 7, 6, 26, 29, 22, 11, 17, 24, 5, 15]
def sorting(array, n):
  for i in range(n - 1):
    for j in range(n - i - 1):
      if array[j] > array[j + 1]:
        array[j], array[j + 1] = array[j + 1], array[j]
  return array
array = [22, 7, 6, 26, 29, 22, 11, 17, 24, 5, 15]
n = len(array)
print(sorting(array, n))
