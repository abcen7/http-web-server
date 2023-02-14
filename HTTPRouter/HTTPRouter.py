from typing import List

from HTTPRouter.Route import Route
from HTTPRouter.Router import Router


class HTTPRouter(Router):
    routes: List[Route]

    def add_route(self, route_path: str):
        self.routes.append(Route(route_path))

    def is_route_exists(self, route_path: str) -> bool:
        return Route(route_path) in self.routes
