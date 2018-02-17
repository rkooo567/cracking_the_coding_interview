"""
	Find indices in which the sum of them is a given target number
"""

def two_sum(lst, target):
	two_sums = []
	lookup = {}
	for i, element in enumerate(lst):
		lookup[element] = i
	for i, element in enumerate(lst):
		if target - element in lookup.keys():
			two_sums.append([lookup[target - element], i])
	return two_sums

def main():
	lst = [1, 2, 4, 4, 5, 6, 7]
	print(two_sum(lst, 8))

if __name__ == "__main__":
	main()