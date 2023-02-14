from HTTPResponse.Builder import Builder


class Director:
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def build(self) -> None:
        self._builder.produce_protocol("HTTP/1.1")
        self._builder.produce_space_char()
        self._builder.produce_status_code("200 OK")
        self._builder.produce_newline_char()
        self._builder.produce_content_type("Content-Type: text/html")
        self._builder.produce_newline_char()
        self._builder.produce_newline_char()
        self._builder.produce_html("<html><body>Hello World</body></html>")
