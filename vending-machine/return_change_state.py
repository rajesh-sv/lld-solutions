from vending_machine_state import VendingMachineState
from money import Money
from product import Product


class ReturnChangeState(VendingMachineState):
    def __init__(self, vending_machine) -> None:
        super().__init__(vending_machine)

    def add_money(self, money: Money) -> None:
        print('Please collect the change first.')

    def select_product(self, product: Product) -> None:
        print('Please collect the change first.')

    def dispense_product(self) -> None:
        print('Please collect the change first.')

    def return_change(self) -> None:
        change = self.vending_machine.get_money_added() - self.vending_machine.get_required_money()
        if change:
            print(f'Change returned: {change}')
        else:
            print('No change returned.')
        self.vending_machine.reset_machine()
