"""
	Quick sort is the sorting algorithm that is O(n*log(n)). 
	Algorithm is like this: 
		1. get the pivot
		2. set the wall index as the lowest index: it increases whenever swap happens
		3. iterate through the value and put the value that is smaller than the pivot to the wall index
		4. once swap happens, increase the wall index
		5. once iteration is over, put the pivot value on the wall index
		6. now let's repeat the process to the left side of the wall index and the right side of the 
			wall index
"""

def sort(lst):
	low = 0
	high = len(lst) - 1
	quick_sort(lst, low, high)

def quick_sort(lst, low, high):
	if low < high:
		pivot_index = partition(lst, low, high)
		quick_sort(lst, low, pivot_index - 1)
		quick_sort(lst, pivot_index + 1, high)

def partition(lst, low, high):
	"""
		Do parition and return the next index
	"""
	wall_index = low - 1
	pivot = lst[high]
	for i in range(low, high):
		if lst[i] <= pivot:
			wall_index += 1
			lst[i], lst[wall_index] = lst[wall_index], lst[i]
	wall_index += 1
	lst[high], lst[wall_index] = lst[wall_index], lst[high]
	return wall_index

def main():
	lst = [3, 4, 7, 9, 5, 1, 8, 2, 6]
	print("initial list: ", lst)
	sort(lst)
	expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	assert lst == expected
	print("final list: ", lst)

if __name__ == "__main__":
	main()