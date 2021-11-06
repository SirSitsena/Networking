import socket

ans = ""
SCORE_STOP = 2
PORT = 60002

while ans not in ["S", "C"]:
    ans = input("Do you want to be server (S) or client (C): ").upper()

sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)


def serverRun():
    sock.bind(('127.0.0.1', PORT))
    sock.listen(1)
    sock.listen(1)
    cPoint = 0
    sPoint = 0

    print('\nlistening...\n')
    (sockC, addr) = sock.accept()
    print('connection from {}'.format(addr))
    while True:
        player1 = ""
        while player1 not in ["R", "P", "S"]:
            player1 = input("({},{}) Your move:".format(sPoint, cPoint))
        sockC.sendall(bytearray(player1, 'ascii'))

        player2 = sockC.recv(1024).decode('ascii')

        print("(opponent's move: {})".format(player2))
        calc = pointCalc(player1, player2)
        sPoint += calc[0]
        cPoint += calc[1]
        if sPoint == SCORE_STOP:
            print("You won with {} vs {}".format(SCORE_STOP, cPoint))
            break
        elif cPoint == SCORE_STOP:
            print("You lost with {} vs {}".format(SCORE_STOP, sPoint))
            break

    sockC.close()
    sock.close()

    print('client {} disconnected'.format(addr))


def clientRun():
    # sock.connect(('127.0.0.1', PORT))
    sock.connect((input("Enter servers IP addres or localhost: "), PORT))
    cPoint = 0
    sPoint = 0

    while True:
        player2 = sock.recv(1024).decode('ascii')

        player1 = ""
        while player1 not in ["R", "P", "S"]:
            player1 = input('({},{}) Your move: '.format(cPoint, sPoint))
        sock.sendall(bytearray(player1, 'ascii'))
        print("(opponent's move: {})".format(player2))

        calc = pointCalc(player1, player2)
        cPoint += calc[0]
        sPoint += calc[1]
        if cPoint == SCORE_STOP:
            print("You won with {} vs {}".format(SCORE_STOP, sPoint))
            break
        elif sPoint == SCORE_STOP:
            print("You lost with {} vs {}".format(SCORE_STOP, cPoint))
            break

    sock.close()

    print('Opponent disconnected')


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
