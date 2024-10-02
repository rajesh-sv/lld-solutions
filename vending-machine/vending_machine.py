from __future__ import annotations
from threading import Lock
from inventory import Inventory
from idle_state import IdleState
from ready_state import ReadyState
from dispense_state import DispenseState
from return_change_state import ReturnChangeState
from vending_machine_state import VendingMachineState
from product import Product
from money import Money


class VendingMachine:
    _instance = None
    _lock = Lock()

    def __new__(cls) -> VendingMachine:
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls._instance.inventory = Inventory()
                cls._instance.idle_state = IdleState(cls._instance)
                cls._instance.ready_state = ReadyState(cls._instance)
                cls._instance.dispense_state = DispenseState(cls._instance)
                cls._instance.return_change_state = ReturnChangeState(cls._instance)
                cls._instance.current_state = cls._instance.idle_state
                cls._instance.selected_product = None
                cls._instance.money_added = 0
            return cls._instance
        
    @classmethod
    def get_instance(cls):
        return cls()
    
    def set_state(self, new_state: VendingMachineState) -> None:
        self.current_state = new_state
        
    def select_product(self, product: Product) -> None:
        self.current_state.select_product(product)
    
    def set_selected_product(self, product: Product) -> None:
        self.selected_product = product
    
    def get_selected_product(self) -> Product:
        return self.selected_product

    def insert_money(self, money: Money) -> None:
        self.current_state.add_money(money)

    def add_money(self, money: Money) -> None:
        self.money_added += money.value

    def dispense_product(self) -> None:
        self.current_state.dispense_product()

    def return_change(self) -> None:
        self.current_state.return_change()

    def get_money_added(self) -> int:
        return self.money_added
    
    def get_required_money(self) -> int:
        return self.selected_product.price
    
    def add_product(self, product: Product, qty: int) -> None:
        self.inventory.add_product(product, qty)

    def delete_product(self, product: Product) -> None:
        self.inventory.delete_product(product)

    def update_qty(self, product: Product, qty: int) -> None:
        self.inventory.update_qty(product, qty)
    
    def get_qty(self, product: Product) -> int:
        return self.inventory.get_qty(product)

    def is_available(self, product: Product) -> None:
        return self.inventory.is_available(product)
    
    def get_inventory_status(self) -> None:
        print(self.inventory)

    def reset_machine(self) -> None:
        self.money_added = 0
        self.selected_product = None
        self.set_state(self.idle_state)