from vending_machine_state import VendingMachineState
from money import Money
from product import Product


class DispenseState(VendingMachineState):
    def __init__(self, vending_machine) -> None:
        super().__init__(vending_machine)

    def add_money(self, money: Money) -> None:
        print('Payment completed. Dispensing product.')

    def select_product(self, product: Product) -> None:
        print('Product selected and payment completed. Dispensing product.')

    def dispense_product(self) -> None:
        product = self.vending_machine.get_selected_product()
        self.vending_machine.update_qty(product, -1)
        print(f'Product dispensed: {product.name}')
        self.vending_machine.set_state(self.vending_machine.return_change_state)

    def return_change(self) -> None:
        print('Please collect the dispensed product first.')
