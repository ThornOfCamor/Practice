"""
Practice - 6
"""

if __name__ == '__main__':
    A = [ 1, 2, 3, 5, 1, 1, 5, 6, 7, 8, 10, 11, 12, 19, 13, 100, 139, 122, 134, 1001, 12929]
    B = [12, 45, 122, 11, 1, 3, 5, 6, 7, 100, 10001, 123423]
    C = []

    for x in A:
        if x in B and x not in C:
            C.append(x)
    C.sort()
    print C
