from typing import Any


class HTTPResponse:
    def __init__(self) -> None:
        self.response = ""

    def add(self, part: Any) -> None:
        self.response += part

    def get_response(self) -> bytes:
        return self.response.encode()
