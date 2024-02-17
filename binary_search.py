# binary_search with divide and conqueror method.
def binarySearch(array, left, ryte, target):
	
	while left <= ryte:
		mid = left + (ryte - left) // 2               # mid element of an array__.
		
		if array[mid] == target:                      # if target found.
			return mid
			
		elif array[mid] < target:                     # if target greater than mid element of an array.
			left = mid + 1
			
		else:
			ryte = mid - 1                              # if  target lesser than mid element of an array.
			
	return -1

array = [2, 3, 4, 10, 40]
print(binarySearch(array, 0, len(array)-1, 4))