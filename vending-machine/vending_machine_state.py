from abc import ABC, abstractmethod
from money import Money
from product import Product


class VendingMachineState(ABC):
    def __init__(self, vending_machine) -> None:
        self.vending_machine = vending_machine

    @abstractmethod
    def add_money(self, money: Money) -> None:
        raise NotImplementedError

    @abstractmethod
    def select_product(self, product: Product) -> None:
        raise NotImplementedError

    @abstractmethod
    def dispense_product(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def return_change(self) -> None:
        raise NotImplementedError
