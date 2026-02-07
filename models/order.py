from typing import List
from models.product import Product


class OrderItem:
    """
    Representa um item DENTRO de um pedido.
    Conceito de COMPOSIÇÃO: Este item só faz sentido existindo dentro de um carrinho.
    """

    def __init__(self, product: Product, quantity: int):
        self.product = product
        self.quantity = quantity
        # 🌟 Ótima sacada: Congelar o preço no momento da compra!
        self._price = product.price

    @property
    def price(self) -> float:
        """Return the frozen price of the product."""
        return self._price

    @property
    def total(self) -> float:
        """Return the total price for this order item."""
        return self._price * self.quantity

    def __str__(self) -> str:
        return f"Item: {self.product.name} | Qtd: {self.quantity} | Sub: ${self.total:.2f}"


class Order:
    """
    Represents a sale order.
    """

    def __init__(self, customer_name: str):
        # AGREGAÇÃO: Recebemos o nome do cliente
        self.customer_name = customer_name
        # COMPOSIÇÃO: A lista começa vazia e nós (a classe Order) gerenciamos ela
        self.items: List[OrderItem] = []
        self.status = "OPEN"

    def add_item(self, product: Product, quantity: int) -> None:
        """
        Adds an item, but only if there is enough stock.
        If the product is already in the order, increases the quantity.
        """
        if quantity <= 0:
            print("❌ Quantity must be positive.")
            return

        # Check stock
        if product.stock >= quantity:
            # Check if product already in order
            for item in self.items:
                if item.product == product:
                    item.quantity += quantity
                    product -= quantity
                    print(f"✅ Added {quantity}x {product.name} to {self.customer_name}'s order.")
                    return
            # If not, add new item
            item = OrderItem(product, quantity)
            self.items.append(item)
            product -= quantity
            print(f"✅ Added {quantity}x {product.name} to {self.customer_name}'s order.")
        else:
            print(f"❌ Stock unavailable for {product.name}. Available: {product.stock}")

    @property
    def total(self) -> float:
        """Return the total price for this order."""
        return sum(item.total for item in self.items)

    def finish_order(self):
        """Changes status to PAID."""
        if not self.items:
            print("❌ Cannot finish empty order.")
            return
        self.status = "PAID"
        print(f"🎉 Order finished! Total to pay: ${self.total:.2f}")

    def __str__(self) -> str:
        return f"Order for {self.customer_name} | Items: {len(self.items)} | Total: ${self.total:.2f}"
