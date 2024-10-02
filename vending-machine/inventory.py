from typing import Dict
from product import Product
from collections import Counter


class Inventory:
    def __init__(self) -> None:
        self.products: Dict[Product: int] = Counter()

    def add_product(self, product: Product, qty: int) -> None:
        self.products[product] = qty

    def delete_product(self, product: Product) -> None:
        self.products.pop(product)

    def update_qty(self, product: Product, qty: int) -> None:
        self.products[product] += qty

    def get_qty(self, product: Product) -> None:
        return self.products[product]
    
    def is_available(self, product: Product) -> bool:
        return self.products[product] > 0
    
    def __str__(self) -> str:
        inventory_str = 'Inventory:\n'

        for product, qty in self.products.items():
            inventory_str += f'Product name: {product.name}\n'
            inventory_str += f'Product price: {product.price}\n'
            inventory_str += f'Product stock: {qty}\n\n'
