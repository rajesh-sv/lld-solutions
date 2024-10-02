from vending_machine_state import VendingMachineState
from money import Money
from product import Product


class ReadyState(VendingMachineState):
    def __init__(self, vending_machine) -> None:
        super().__init__(vending_machine)

    def add_money(self, money: Money) -> None:
        self.vending_machine.add_money(money)
        if self.vending_machine.get_money_added() >= self.vending_machine.get_required_money():
             self.vending_machine.set_state(self.vending_machine.dispense_state)

    def select_product(self, product: Product) -> None:
            print('A product is already selected.')

    def dispense_product(self) -> None:
        print('Please add the required amount.')

    def return_change(self) -> None:
        self.vending_machine.set_state(self.vending_machine.return_change_state)
