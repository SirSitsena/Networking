import socket

SCORE4WIN = 2
PORT = 12345


def printRules():
    print('\n****************************************\n')
    print('\nWelcome to the Rock Paper Scissors game!\n')
    print('\n---------------RULES--------------------\n')
    print('Rules: R - for rock, P - for paper, S - for scissors')
    print('You play until one of you wins {} times\n'.format(SCORE4WIN))
    print('\n****************************************\n')


def printEndGame(myPoints, enemyPoints):
    if myPoints == SCORE4WIN:
        print("\n****************CONGRATS****************\n")
        print("You won with {} vs {}".format(SCORE4WIN, enemyPoints))
        print("\n****************CONGRATS****************\n")
    else:
        print("\n***************GAME-OVER****************\n")
        print("You lost with {} vs {}".format(myPoints, SCORE4WIN))
        print("\n***************GAME-OVER****************\n")


def winCheck(myPoints, enemyPoints):
    if myPoints == SCORE4WIN or enemyPoints == SCORE4WIN:
        printEndGame(myPoints, enemyPoints)
        return False
    else:
        print("Current score: {}, {}".format(myPoints, enemyPoints))
        return True


def moveCalc(myMove, enemyMove):
    if myMove == enemyMove:
        return 0, 0
    if myMove == "R" and enemyMove == "P":
        return 0, 1
    if myMove == "R" and enemyMove == "S":
        return 1, 0
    if myMove == "P" and enemyMove == "R":
        return 1, 0
    if myMove == "P" and enemyMove == "S":
        return 0, 1
    if myMove == "S" and enemyMove == "R":
        return 0, 1
    if myMove == "S" and enemyMove == "P":
        return 1, 0


def game(sock, turn):
    myPoints = 0
    enemyPoints = 0
    gameStatus = True
    myMove = ""
    flag = turn

    printRules()

    # Server makes the first move ->

    while gameStatus:
        myMove = ""
        if turn:
            while myMove not in ["R", "P", "S"]:
                myMove = input("({},{}) Your move: ".format(myPoints, enemyPoints)).upper()
            sock.sendall(bytearray(myMove, 'ascii'))
            enemyMove = sock.recv(1024).decode('ascii')
        else:
            enemyMove = sock.recv(1024).decode('ascii')
            while myMove not in ["R", "P", "S"]:
                myMove = input("({},{}) Your move: ".format(myPoints, enemyPoints)).upper()
            sock.sendall(bytearray(myMove, 'ascii'))
        print("\nYour opponent's turn...\n")
        moveResult = moveCalc(myMove, enemyMove)
        myPoints += moveResult[0]
        enemyPoints += moveResult[1]
        gameStatus = winCheck(myPoints, enemyPoints)
    # Client makes the second move ->


def server():
    serverSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    serverSocket.bind(('127.0.0.1', PORT))
    serverSocket.listen(1)
    print('\nlistening...\n')
    (clientSocket, addr) = serverSocket.accept()
    print('connection from {}'.format(addr))

    game(clientSocket, True)

    serverSocket.close()
    clientSocket.close()

    print('client {} disconnected'.format(addr))
    input("\npress Enter to exit\n\n")


def client():
    serverSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    serverSocket.connect((input("Enter servers IP address or localhost: "), PORT))

    game(serverSocket, False)

    serverSocket.close()

    print('Opponent disconnected')
    input("\npress Enter to exit\n\n")


def Main():
    ans = ""
    while ans not in ["S", "C"]:
        ans = input("\nDo you want to be server (S) or client (C): ").upper()

    if ans == "S":
        server()
    else:
        client()


Main()
