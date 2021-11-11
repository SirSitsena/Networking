import socket
PORT = 80

server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM, proto=0)
server.bind(('127.0.0.1', PORT))
server.listen(1)
print('\nlistening...\n')

while True:
    (clientSocket, addr) = server.accept()
    print('connection from {}'.format(addr))

    request = clientSocket.recv(1024)

    print(request.decode('ascii'))
    response = """
    <html>
    <pre>
    {}
    </pre>
    </html>
    """.format(request.decode('ascii'))

    clientSocket.sendall(bytearray("HTTP/1.1 200 ok\n", "ASCII"))
    clientSocket.sendall(bytearray("\n", "ASCII"))
    clientSocket.sendall(bytearray(response, "ASCII"))

    clientSocket.close()


server.close()
