from abc import ABC

from HTTPResponse.Builder import Builder
from HTTPResponse.HTTPResponse import HTTPResponse


class HTTPResponseBuilder(Builder, ABC):
    response = ''
    NEWLINE_CHAR = '\r\n'
    SPACE_CHAR = ' '

    def __init__(self) -> None:
        self._response = None
        self.reset()

    def reset(self) -> None:
        self._response = HTTPResponse()

    @property
    def response(self) -> HTTPResponse:
        response = self._response
        self.reset()
        return response

    def produce_newline_char(self) -> None:
        self._response.add(self.NEWLINE_CHAR)

    def produce_space_char(self) -> None:
        self._response.add(self.SPACE_CHAR)

    def produce_protocol(self, protocol: str) -> None:
        self._response.add(protocol)

    def produce_content_type(self, content_type: str) -> None:
        self._response.add(content_type)

    def produce_status_code(self, status_code: str) -> None:
        self._response.add(status_code)

    def produce_html(self, html: str) -> None:
        self._response.add(html)
