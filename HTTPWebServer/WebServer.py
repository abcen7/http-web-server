import socket
from typing import Union, List, Callable

from HTTPWebServer.Singleton import Singleton
from abc import ABC, abstractmethod


class WebServer(Singleton, ABC):

    @abstractmethod
    def _receive_all(self, socket: socket.socket) -> Union[None, str]:
        pass

    @abstractmethod
    def _normalize_request(self, request: str) -> List[str]:
        pass

    @abstractmethod
    def execute_routing(self, request: str) -> None:
        pass

    @staticmethod
    @abstractmethod
    def get(function) -> Callable:
        pass

    @abstractmethod
    def run(self):
        pass