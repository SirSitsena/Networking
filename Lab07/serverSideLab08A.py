import socket
import select

PORT = 60003

serverS = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverS.bind(("", PORT))
serverS.listen(1)
listOfSockets = [serverS]
print("Listening on port " + str(PORT))


def broadCast(msg):
    for s in listOfSockets:
        if s != serverS:
            s.sendall(bytearray(msg, "ASCII"))


def userFormat(tup):
    return "[{}:{}]: ".format(tup[0], tup[1])


def disconnect(sock):
    sock.shutdown(1)
    sock.close()
    listOfSockets.remove(sock)


while True:
    tup = select.select(listOfSockets, [], [])
    sock = tup[0][0]

    if sock == serverS:
        (sockClient, addr) = serverS.accept()
        listOfSockets.append(sockClient)
        broadCast(userFormat(addr) + "has connected")

    else:
        try:
            data = sock.recv(2048)
            if not data:
                broadCast(userFormat(sock.getpeername()) + "has disconnected")
                disconnect(sock)
            else:
                text = data.decode('ascii')
                broadCast(userFormat(sock.getpeername()) + text)
                if "/exit" in text:
                    disconnect(sock)
        except socket.error as error:
            print(error)
            listOfSockets.remove(sock)
            broadCast(userFormat(sock.getpeername()) + "just crashed....")
