from abc import ABC, abstractmethod


class Builder(ABC):

    @property
    @abstractmethod
    def response(self) -> None:
        pass

    @abstractmethod
    def produce_protocol(self, protocol: str) -> None:
        pass

    @abstractmethod
    def produce_content_type(self, content_type: str) -> None:
        pass

    @abstractmethod
    def produce_status_code(self, status_code: str) -> None:
        pass

    @abstractmethod
    def produce_space_char(self) -> None:
        pass

    @abstractmethod
    def produce_newline_char(self) -> None:
        pass

    @abstractmethod
    def produce_html(self, html: str) -> None:
        pass
