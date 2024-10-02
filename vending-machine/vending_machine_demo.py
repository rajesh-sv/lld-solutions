from vending_machine import VendingMachine
from product import Product
from coins import *
from notes import *

class VendingMachineDemo:
    @staticmethod
    def run():
        vending_machine = VendingMachine.get_instance()

        # Add products to the inventory
        coke = Product("Coke", 45)
        pepsi = Product("Pepsi", 40)
        water = Product("Water", 12)

        vending_machine.add_product(coke, 5)
        vending_machine.add_product(pepsi, 3)
        vending_machine.add_product(water, 2)

        # Select a product
        vending_machine.select_product(coke)

        # Insert coins
        vending_machine.insert_money(OneRupeeCoin())
        vending_machine.insert_money(TwoRupeeCoin())
        vending_machine.insert_money(TwoRupeeCoin())

        # Insert a note
        vending_machine.insert_money(TwentyRupeeNote())
        vending_machine.insert_money(TwentyRupeeNote())

        # Dispense the product
        vending_machine.dispense_product()

        # Return change
        vending_machine.return_change()

        # Select another product
        vending_machine.select_product(pepsi)

        # Insert insufficient money
        vending_machine.insert_money(FiveRupeeCoin())

        # Try to dispense the product
        vending_machine.dispense_product()

        # Insert more money
        vending_machine.insert_money(FifetyRupeeNote())
        

        # Dispense the product
        vending_machine.dispense_product()

        # Return change
        vending_machine.return_change()

if __name__ == "__main__":
    VendingMachineDemo.run()