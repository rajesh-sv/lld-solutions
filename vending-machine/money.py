from abc import ABC


class Money(ABC):
    def __init__(self, value: int) -> None:
        self.value = value