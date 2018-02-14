def bubble_sort(lst):
    num_swap = 0
    is_sorted = False
    while (not is_sorted):
        last_unsorted = len(lst) - 1
        is_sorted = True
        for i in range(last_unsorted):
            if lst[i] > lst[i + 1] :
                swap(lst, i, i + 1)
                num_swap += 1
                is_sorted = False
        last_unsorted -= 1
    return num_swap

def swap(lst, i, j):
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
num_swap = str(bubble_sort(a))
first_element = str(a[0])
last_element = str(a[-1])
print("Array is sorted in " + num_swap + " swaps.")
print("First Element: " + first_element)
print("Last Element: " + last_element)
