""" 
order.py
Module that represents an order. 
"""
from __future__ import annotations
from typing import List, Optional, Dict, Any
from datetime import datetime

from models.product import Product


class OrderItem:
    """Represents an item inside an order. Price is frozen when added."""

    def __init__(self, product: Product, quantity: int):
        self.product = product
        self.quantity = quantity
        self._price = product.price  # freeze price

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


class Order:
    """Represents a sale order."""

    def __init__(self, customer_name: str):
        self.customer_name = customer_name
        self.items: List[OrderItem] = []
        self.status = "OPEN"
        self.created_at = datetime.utcnow().isoformat()

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def find_item_index_by_name(self, name: str) -> Optional[int]:
        for i, item in enumerate(self.items):
            if item.product.name.lower() == name.lower():
                return i
        return None

    def add_item(self, product: Product, quantity: int) -> None:
        """Add an item if there is enough stock. If it exists, increase quantity."""
        if self.status != "OPEN":
            print("❌ You cannot modify a closed order.")
            return

        if not isinstance(quantity, int):
            print("❌ Quantity must be an integer.")
            return
        if quantity <= 0:
            print("❌ Quantity must be positive.")
            return

        if product.stock < quantity:
            print(
                f"❌ Stock unavailable for {product.name}. Available: {product.stock}")
            return

        for item in self.items:
            if item.product == product:
                item.quantity += quantity
                product -= quantity
                print(
                    f"✅ Added {quantity}x {product.name} to {self.customer_name}'s order.")
                return

        self.items.append(OrderItem(product, quantity))
        product -= quantity
        print(
            f"✅ Added {quantity}x {product.name} to {self.customer_name}'s order.")

    def remove_item(self, item_index: int, quantity: Optional[int] = None) -> None:
        """
        Remove items from the cart.
        - If quantity is None: remove the entire item line (restock full qty).
        - If quantity is provided: reduce quantity and restock that amount.
        """
        if self.status != "OPEN":
            print("❌ You cannot modify a closed order.")
            return

        if not (0 <= item_index < len(self.items)):
            print("❌ Invalid cart item number.")
            return

        item = self.items[item_index]

        if quantity is None:
            # remove entire line
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
            print(
                f"❌ You only have {item.quantity} of {item.product.name} in the cart.")
            return

        item.product += quantity
        item.quantity -= quantity
        print(f"🗑️ Removed {quantity}x {item.product.name} from the cart.")

        if item.quantity == 0:
            self.items.pop(item_index)
            print("ℹ️ Item quantity reached 0, line removed.")

    def cancel(self) -> None:
        """Cancel the order and restore all stock."""
        if self.status != "OPEN":
            print("❌ Only OPEN orders can be canceled.")
            return

        # Restock everything
        for item in self.items:
            item.product += item.quantity

        self.items.clear()
        self.status = "CANCELED"
        print(f"🚫 Order canceled for {self.customer_name}. Stock restored.")

    @property
    def total(self) -> float:
        return sum(item.total for item in self.items)

    def finish_order(self) -> None:
        """Mark order as PAID."""
        if self.status != "OPEN":
            print("❌ Only OPEN orders can be finished.")
            return
        if self.is_empty():
            print("❌ Cannot finish empty order.")
            return

        self.status = "PAID"
        print(
            f"🎉 Order finished for {self.customer_name}! Total to pay: ${self.total:.2f}")

    def summary(self) -> str:
        """Return a multi-line cart summary."""
        lines: List[str] = []
        lines.append(f"Customer: {self.customer_name}")
        lines.append(f"Status: {self.status}")
        lines.append("-" * 50)

        if self.is_empty():
            lines.append("🛒 Cart is empty.")
        else:
            for idx, item in enumerate(self.items, start=1):
                lines.append(f"{idx}. {item}")
            lines.append("-" * 50)
            lines.append(f"TOTAL: ${self.total:.2f}")

        return "\n".join(lines)

    def to_record(self) -> Dict[str, Any]:
        """Convert order to a JSON-safe record for orders.json."""
        return {
            "customer_name": self.customer_name,
            "status": self.status,
            "created_at_utc": self.created_at,
            "finished_at_utc": datetime.utcnow().isoformat(),
            "items": [item.to_record() for item in self.items],
            "total": self.total,
        }

    def __str__(self) -> str:
        return f"Order for {self.customer_name} | Items: {len(self.items)} | Total: ${self.total:.2f}"