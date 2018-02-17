def print_permutation(string, result=""):
	"""
		Get the string and print the permutation
	"""	
	if len(string) == 0:
		print(result)
	else:
		for i in range(len(string)):
			print_permutation(string[0:i] + string[i + 1:], result + string[i])

def main():
	inp = "word"
	print_permutation(inp)

if __name__ == "__main__":
	main()