"""This will be the main module"""
import tools

def print_out_stuff(number=0):
	"""
	this function tests out what's avaliable in the namespace from tools


	Parameters
	----------
	number: int, optional
		the number which to test on

	Returns
	-------
	number: int
	"""

	print(f'call add_two function from multi.py on {number}')
	number = add_two(number)
	print(f'after adding {number}')
	print(f'call multiply function from multi.py on {number}')
	number = multiply(number)
	print(f'after multiplication {number}')
	print('====')
	print(f'test: important number from tools = {important_number}')
	print('====')
	print(f'test: important number from test_package = {non_important_number}')
	print(f'test: timefrom test_package = {today}')
	return number


if __name__ == '__main__':
	print(f'start of main script')
	number = print_out_stuff(number=0)


