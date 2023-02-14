import socket
from enum import Enum

from HTTPResponse.HTTPResponseBuilder import HTTPResponseBuilder
from HTTPResponse.Director import Director

MAX_PACKET = 32768
SOCKET_TIMEOUT = 0.01
MAX_CONNECTIONS = 1000
HOST = '127.0.0.1'
PORT = 13500
LINUX_SEPARATOR = '\\n'
WINDOWS_SEPARATOR = '\\r\\n'


# Getting all data from reading socket
def receive_all(socket: socket.socket):
    previous_timeout = socket.gettimeout()
    try:
        socket.settimeout(SOCKET_TIMEOUT)
        data = []
        while True:
            try:
                data.append(socket.recv(MAX_PACKET))
            except BaseException:
                return ''.join(str(data))
    finally:
        socket.settimeout(previous_timeout)


def normalize_request(request: str):
    values = ["[b'", "']"]
    data = []
    for x in request.strip().split("\\r\\n"):
        for value in values:
            x = x.replace(value, '')
        if len(x) != 0:
            data.append(x)
    return data


def main():
    server_socket = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM,
        socket.IPPROTO_TCP
    )
    server_socket.bind((HOST, PORT))
    server_socket.listen(MAX_CONNECTIONS)

    print("SERVER ESTABLISHED")

    while True:
        client_socket, client_address = server_socket.accept()

        request = normalize_request(receive_all(client_socket))

        director = Director()
        builder = HTTPResponseBuilder()
        director.builder = builder
        director.build()
        # print(builder.response.get_response())
        print("""HTTP/1.1 200 OK
        Content-Type: text/html
        \r\n<html><body>Hello World</body></html>
        """.encode())

        client_socket.send(builder.response.get_response())
        # client_socket.send()
        client_socket.close()


main()
