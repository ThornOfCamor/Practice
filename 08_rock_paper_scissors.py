"""
Practice - 8
"""

def RPS_game():
    """
    Output = 1: P1 wins
    Output = -1: P2 wins
    Output = 0: Draw
    """
    P1 = int(raw_input("\nPlayer 1 move: "), 10)
    P2 = int(raw_input("Player 2 move: "), 10)
    if P1 == 1:
        if P2 == 1:
            return 0
        elif P2 == 2:
            return -1
        elif P2 == 3:
            return 1
    elif P1 == 2:
        if P2 == 1:
            return 1
        elif P2 == 2:
            return 0
        elif P2 == 3:
            return -1
    elif P3 == 3:
        if P2 == 1:
            return -1
        elif P2 == 2:
            return 1
        elif P2 == 3:
            return 0

if __name__ == '__main__':
    print "Rock Paper Scissors \n"
    print "Instructions:"
    print "Rock: 1, Paper: 2, Scissors: 3\n"
    print "Do you want to begin?"
    c = raw_input("Enter Y for yes and N for no: ")
    while c == 'Y':
        d = RPS_game()
        if d == 1:
           print "Player 1 wins\n"
        if d == -1:
           print "Player 2 wins\n"
        if d == 0:
           print "The game was a draw\n"
        print "Do you want to continue?"
        c = raw_input("Enter Y for yes and N for no: ")
