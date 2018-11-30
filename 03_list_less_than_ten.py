"""
Practice - 3
"""

if __name__ == '__main__':
    a = [ 1, 1, 2, 3, 5, 6, 10, 12, 12, 15, 18, 33, 80]
    b = []
    maxi = int(raw_input("Enter upper limit: "), 10)
    for x in a:
        if maxi>x:
            b.append(x)
    print b

