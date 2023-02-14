from abc import ABC, abstractmethod
from HTTPWebServer.Singleton import Singleton


class Router(Singleton, ABC):

    @abstractmethod
    def add_route(self, route_path: str) -> None:
        pass

    @abstractmethod
    def is_route_exists(self, route_path: str) -> bool:
        pass
