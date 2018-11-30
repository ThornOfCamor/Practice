"""
Practice - 2
"""

if __name__ == "__main__":
	num = int(raw_input("Enter the dividend to be checked: "), 10)
	check = int(raw_input("Enter the divisor to check with: "), 10)
	if num%check == 0:
		print "%d divides %d evenly" % (check, num)
	else:
		print "%d does not divide %d evenly" % (check, num)
