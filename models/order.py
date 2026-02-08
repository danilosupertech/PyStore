from __future__ import annotations

from typing import Dict, Any
from datetime import datetime, timezone

from models.cart import Cart


class Order:
    """Order lifecycle/status + owns a cart."""

    def __init__(self, customer_name: str):
        self.customer_name = customer_name
        self.cart = Cart()
        self.status = "OPEN"
        self.created_at = datetime.now(timezone.utc).isoformat()

    def cancel(self) -> None:
        if self.status != "OPEN":
            print("❌ Only OPEN orders can be canceled.")
            return
        self.cart.clear(restock=True)
        self.status = "CANCELED"
        print(f"🚫 Order canceled for {self.customer_name}. Stock restored.")

    def finish_order(self) -> None:
        if self.status != "OPEN":
            print("❌ Only OPEN orders can be finished.")
            return
        if self.cart.is_empty():
            print("❌ Cannot finish empty order.")
            return

        self.status = "PAID"
        print(f"🎉 Order finished for {self.customer_name}! Total to pay: ${self.cart.total:.2f}")

    def summary(self) -> str:
        return "\n".join(
            [
                f"Customer: {self.customer_name}",
                f"Status: {self.status}",
                self.cart.summary(),
            ]
        )

    def to_record(self) -> Dict[str, Any]:
        return {
            "customer_name": self.customer_name,
            "status": self.status,
            "created_at_utc": self.created_at,
            "finished_at_utc": datetime.now(timezone.utc).isoformat(),
            "items": [item.to_record() for item in self.cart.items],
            "total": self.cart.total,
        }
