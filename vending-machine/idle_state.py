from vending_machine_state import VendingMachineState
from money import Money
from product import Product


class IdleState(VendingMachineState):
    def __init__(self, vending_machine) -> None:
        super().__init__(vending_machine)

    def add_money(self, money: Money) -> None:
        print('Please select a product first.')

    def select_product(self, product: Product) -> None:
        if self.vending_machine.is_available(product):
            self.vending_machine.set_selected_product(product)
            print(f'Product selected: {product.name}')
            self.vending_machine.set_state(self.vending_machine.ready_state)
        else:
            print(f'Product not available: {product.name}')

    def dispense_product(self) -> None:
        print('Please select a product and make payment.')

    def return_change(self) -> None:
        print('No change to return.')
