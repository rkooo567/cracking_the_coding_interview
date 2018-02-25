# Find a number of sub string in a string

def num_sub_string(string, sub_string):
	"""
		return the number of sub string in the given string
	"""
	first_char_sub_string = sub_string[0]
	result = 0
	for i in range(len(string)):
		if string[i] == first_char_sub_string:
			result += check_sub_string(string[i + 1:], sub_string[1:])
	return result

def check_sub_string(string, sub_string):
	"""
		check if the first chars of given string is the sub string
	"""
	if sub_string == "":
		return 1
	else:
		for i in range(len(string)):
			if string[0] == sub_string[0]:
				return check_sub_string(string[1:], sub_string[1:])
			else:
				return 0


def main():
	string = "This is a good day is very is gisris"
	sub_string_one = "is"
	sub_string_two = 'o'
	sub_string_three = "Th"
	result_one = num_sub_string(string, sub_string_one)
	result_two = num_sub_string(string, sub_string_two)
	result_three = num_sub_string(string, sub_string_three)
	assert result_one == 6
	assert result_two == 2
	assert result_three == 1

if __name__ == "__main__":
	main()