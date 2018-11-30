"""
Practice - 6
"""

def isPalindrome(string):
    A = list(string)
    length = len(A) - 1
    i = 0
    while i<=int(length/2):
        if A[i] != A[length-i]:
            return 0
        i += 1
    return 1

if __name__ == '__main__':
    string = raw_input("Enter a string: ")
    if isPalindrome(string) == 0:
        print "Given string is not a palindrome"
    else:
        print "Given string is a palindrome"
