"""
Practice - 4
"""

import math

if __name__ == '__main__':
    num = int(raw_input("Enter a number: "), 10)
    sqr = math.sqrt(num)
    divisors = []
    i = 1
    while i<sqr:
    	if num%i == 0:
    		divisors.append(i)
    		divisors.append(num/i)
    	i += 1
    if int(sqr)*int(sqr) == num:
    	divisors.append(int(sqr))
    divisors.sort()
    print divisors
