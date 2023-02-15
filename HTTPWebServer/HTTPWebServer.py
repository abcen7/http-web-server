import socket
from abc import ABC
from typing import Optional, Callable

from HTTPResponse.HTTPResponseBuilder import HTTPResponseBuilder
from HTTPResponse.Director import Director
from HTTPWebServer.WebServer import WebServer
from HTTPRouter.HTTPRouter import HTTPRouter


class HTTPWebServer(WebServer):
    MAX_PACKET = 32768
    SOCKET_TIMEOUT = 0.01
    MAX_CONNECTIONS = 1000

    DEFAULT_HOST: str = '127.0.0.1'
    DEFAULT_PORT: int = 13500

    def __init__(self, host: Optional[str] = DEFAULT_HOST, port: Optional[int] = DEFAULT_PORT):
        self.router = None
        self.host: str = host
        self.port: int = port
        self.router: HTTPRouter = HTTPRouter()
        self.run()

    # Getting all data from reading socket
    def _receive_all(self, socket: socket.socket):
        previous_timeout = socket.gettimeout()
        try:
            socket.settimeout(self.SOCKET_TIMEOUT)
            data = []
            while True:
                try:
                    data.append(socket.recv(self.MAX_PACKET))
                except BaseException:
                    return ''.join(str(data))
        finally:
            socket.settimeout(previous_timeout)

    def _normalize_request(self, request: str):
        values = ["[b'", "']"]
        data = []
        for x in request.strip().split("\\r\\n"):
            for value in values:
                x = x.replace(value, '')
            if len(x) != 0:
                data.append(x)
        return data

    def execute_routing(self, request: str):
        method, route, protocol = request[0].split()
        # check if requested url route exists
        print(method, route, protocol)

    def get(self, route_path: str) -> Callable:
        print(1)

        def decorator(function):
            async def wrapper(*args, **kwargs):
                self.router.add_route(route_path)
                await function(*args, **kwargs)
                print(self.router.routes)

            return wrapper

        return decorator

    def run(self):
        server_socket = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM,
            socket.IPPROTO_TCP
        )

        server_socket.bind((self.host, self.port))
        server_socket.listen(self.MAX_CONNECTIONS)

        print("SERVER ESTABLISHED")

        while True:
            client_socket, client_address = server_socket.accept()

            request = self._normalize_request(self._receive_all(client_socket))

            self.execute_routing(request)

            director = Director()
            builder = HTTPResponseBuilder()
            director.builder = builder
            director.build()

            client_socket.send(builder.response.get_response())
            client_socket.close()
