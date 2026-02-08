from __future__ import annotations

from typing import List, Optional, Dict, Any

from models.product import Product


class CartItem:
    """Represents an item inside the cart. Price is frozen when added."""

    def __init__(self, product: Product, quantity: int):
        self.product = product
        self.quantity = quantity
        self._price = product.price

    @property
    def price(self) -> float:
        return self._price

    @property
    def total(self) -> float:
        return self._price * self.quantity

    def to_record(self) -> Dict[str, Any]:
        return {
            "name": self.product.name,
            "quantity": self.quantity,
            "unit_price": self.price,
            "subtotal": self.total,
        }

    def __str__(self) -> str:
        return (
            f"{self.product.name} | Qty: {self.quantity} | "
            f"Unit: ${self.price:.2f} | Subtotal: ${self.total:.2f}"
        )


class Cart:
    """Shopping cart. (Current behavior: updates stock immediately)."""

    def __init__(self) -> None:
        self.items: List[CartItem] = []

    def is_empty(self) -> bool:
        return len(self.items) == 0

    @property
    def total(self) -> float:
        return sum(item.total for item in self.items)

    def add_item(self, product: Product, quantity: int) -> None:
        if not isinstance(quantity, int):
            print("❌ Quantity must be an integer.")
            return
        if quantity <= 0:
            print("❌ Quantity must be positive.")
            return
        if product.stock < quantity:
            print(f"❌ Stock unavailable for {product.name}. Available: {product.stock}")
            return

        for item in self.items:
            if item.product == product:
                item.quantity += quantity
                product -= quantity
                print(f"✅ Added {quantity}x {product.name} to the cart.")
                return

        self.items.append(CartItem(product, quantity))
        product -= quantity
        print(f"✅ Added {quantity}x {product.name} to the cart.")

    def remove_item(self, item_index: int, quantity: Optional[int] = None) -> None:
        if not (0 <= item_index < len(self.items)):
            print("❌ Invalid cart item number.")
            return

        item = self.items[item_index]

        if quantity is None:
            item.product += item.quantity
            removed_name = item.product.name
            removed_qty = item.quantity
            self.items.pop(item_index)
            print(f"🗑️ Removed {removed_qty}x {removed_name} (line removed).")
            return

        if not isinstance(quantity, int):
            print("❌ Quantity must be an integer.")
            return
        if quantity <= 0:
            print("❌ Quantity must be positive.")
            return
        if quantity > item.quantity:
            print(f"❌ You only have {item.quantity} of {item.product.name} in the cart.")
            return

        item.product += quantity
        item.quantity -= quantity
        print(f"🗑️ Removed {quantity}x {item.product.name} from the cart.")

        if item.quantity == 0:
            self.items.pop(item_index)
            print("ℹ️ Item quantity reached 0, line removed.")

    def clear(self, restock: bool = True) -> None:
        if restock:
            for item in self.items:
                item.product += item.quantity
        self.items.clear()

    def summary(self) -> str:
        lines: List[str] = []
        lines.append("-" * 50)

        if self.is_empty():
            lines.append("🛒 Cart is empty.")
        else:
            for idx, item in enumerate(self.items, start=1):
                lines.append(f"{idx}. {item}")
            lines.append("-" * 50)
            lines.append(f"TOTAL: ${self.total:.2f}")

        return "\n".join(lines)
