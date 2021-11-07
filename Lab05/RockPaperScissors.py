import socket

SCORE4WIN = 10
PORT = 12345

myPoints = 0
enemyPoints = 0


def printRules():
    print('\n----------------------Welcome/Rules----------------------\n')
    print('This is the Rock Paper Scissors game!\n')

    print('Rules: R - for rock, P - for paper, S - for scissors')
    print('The game goes on until one of you wins {} times\n'.format(SCORE4WIN))
    print('----------------------- GAME START ----------------------\n')


def calcPoints(myMove, enemyMove):
    global myPoints
    global enemyPoints

    if myMove == enemyMove:
        return

    # my win
    if (myMove == "R" and enemyMove == "S") or (myMove == "P" and enemyMove == "R") or (
            myMove == "S" and enemyMove == "P"):
        myPoints += 1

    # enemy wins
    if (myMove == "R" and enemyMove == "P") or (myMove == "P" and enemyMove == "S") or (
            myMove == "S" and enemyMove == "R"):
        enemyPoints += 1


def runGame(sock):
    printRules()

    while (myPoints != SCORE4WIN) and (enemyPoints != SCORE4WIN):

        myMove = ""
        while myMove not in ["R", "P", "S"]:
            myMove = input("Your move: ").upper()

        sock.sendall(bytearray(myMove, 'ascii'))

        print("Waiting opponent's turn...")
        enemyMove = sock.recv(1024).decode('ascii')

        calcPoints(myMove, enemyMove)
        print("Current scores: {}, {}\n".format(myPoints, enemyPoints))

    print("\n---------------------- GAME OVER ------------------------\n")
    iamWinner = (myPoints == SCORE4WIN)
    print("You {} with {} vs {}".format("WON" if iamWinner else "LOST", myPoints, enemyPoints))


def runServer():
    serverSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    serverSocket.bind(('', PORT))
    serverSocket.listen(1)
    print('\nWaiting client...\n')
    (clientSocket, clientAddress) = serverSocket.accept()
    print('Client connected from {}'.format(clientAddress))

    runGame(clientSocket)

    clientSocket.close()
    serverSocket.close()


def runClient():
    sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    host = input("Enter server's IP address or localhost: ")
    sock.connect((host, PORT))

    runGame(sock)

    sock.close()


def main():
    answer = ""
    while answer not in ["S", "C"]:
        answer = input("\nStart as server (S) or client (C): ").upper()

    runServer() if (answer == "S") else runClient()

    input("\nPress 'Enter' to close game\n")


main()
