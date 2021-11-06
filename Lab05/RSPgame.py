import socket

ans = ""
SCORE_STOP = 2
PORT = 60002

while ans not in ["S", "C"]:
    ans = input("\nDo you want to be server (S) or client (C): ").upper()

sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)


def serverRun():
    sock.bind(('127.0.0.1', PORT))
    sock.listen(1)
    cPoint = 0
    sPoint = 0

    print('\nlistening...\n')
    (sockC, addr) = sock.accept()
    print('connection from {}'.format(addr))
    print('\n****************************************\n')
    print('\nWelcome to the Rock Paper Scissors game!\n')
    print('\n---------------RULES--------------------\n')
    print('Rules: R - for rock, P - for paper, S - for scissors')
    print('You play until one of you wins {} times\n'.format(SCORE_STOP))
    print('\n****************************************\n')
    while True:
        player1 = ""
        while player1 not in ["R", "P", "S"]:
            player1 = input("({},{}) Your move: ".format(sPoint, cPoint)).upper()

        sockC.sendall(bytearray(player1, 'ascii'))

        player2 = sockC.recv(1024).decode('ascii')
        print("(opponent's move: {})".format(player2))

        calc = pointCalc(player1, player2)
        sPoint += calc[0]
        cPoint += calc[1]
        print("Current score: {}, {}".format(sPoint, cPoint))

        if sPoint == SCORE_STOP:
            print("\n****************CONGRATS****************\n")
            print("You won with {} vs {}".format(SCORE_STOP, cPoint))
            print("\n****************CONGRATS****************\n")
            break
        elif cPoint == SCORE_STOP:
            print("\n***************GAME-OVER****************\n")
            print("You lost with {} vs {}".format(SCORE_STOP, sPoint))
            print("\n***************GAME-OVER****************\n")
            break
        print("\nYour opponent's turn...\n")

    sockC.close()
    sock.close()

    print('client {} disconnected'.format(addr))
    termination = input("\npress Enter to exit\n\n")


def clientRun():
    sock.connect((input("Enter servers IP addres or localhost: "), PORT))
    cPoint = 0
    sPoint = 0
    print('\n****************************************\n')
    print('\nWelcome to the Rock Paper Scissors game!\n')
    print('\n---------------RULES--------------------\n')
    print('Rules: R - for rock, P - for paper, S - for scissors')
    print('You play until one of you wins {} times\n'.format(SCORE_STOP))
    print('Your opponent makes the first move xD\n')
    print('\n****************************************\n')
    print("Your opponent's turn...\n")
    while True:
        player2 = sock.recv(1024).decode('ascii')

        player1 = ""
        while player1 not in ["R", "P", "S"]:
            player1 = input('({},{}) Your move: '.format(cPoint, sPoint)).upper()

        print("(opponent's move: {})".format(player2))
        calc = pointCalc(player1, player2)
        cPoint += calc[0]
        sPoint += calc[1]
        print("Current score: {}, {}".format(cPoint, sPoint))
        sock.sendall(bytearray(player1, 'ascii'))
        if cPoint == SCORE_STOP:
            print("\n****************CONGRATS****************\n")
            print("You won with {} vs {}".format(SCORE_STOP, sPoint))
            print("\n****************CONGRATS****************\n")
            break
        elif sPoint == SCORE_STOP:
            print("\n***************GAME-OVER****************\n")
            print("You lost with {} vs {}".format(SCORE_STOP, cPoint))
            print("\n***************GAME-OVER****************\n")
            break
        print("\nYour opponent's turn...\n")

    sock.close()

    print('Opponent disconnected')
    termination = input("\npress Enter to exit\n\n")


# R P S
def pointCalc(player1, player2):
    if player1 == player2:
        return 0, 0
    if player1 == "R" and player2 == "P":
        return 0, 1
    if player1 == "R" and player2 == "S":
        return 1, 0
    if player1 == "P" and player2 == "R":
        return 1, 0
    if player1 == "P" and player2 == "S":
        return 0, 1
    if player1 == "S" and player2 == "R":
        return 0, 1
    if player1 == "S" and player2 == "P":
        return 1, 0


if ans == "S":
    serverRun()

else:
    clientRun()
