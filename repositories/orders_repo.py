from __future__ import annotations

import json
import os
from typing import List, Dict, Any


class OrdersRepository:
    """Reads/writes orders.json. No business rules here."""

    def __init__(self, base_dir: str) -> None:
        self.orders_file = os.path.join(base_dir, "orders.json")

    def load(self) -> List[Dict[str, Any]]:
        if not os.path.exists(self.orders_file):
            return []

        try:
            with open(self.orders_file, "r", encoding="utf-8") as f:
                data = json.load(f)
            return data if isinstance(data, list) else []
        except (OSError, json.JSONDecodeError) as e:
            print(f"❌ Error reading orders: {e}")
            return []

    def append(self, order_record: Dict[str, Any]) -> None:
        orders = self.load()
        orders.append(order_record)

        try:
            with open(self.orders_file, "w", encoding="utf-8") as f:
                json.dump(orders, f, indent=4)
            print("🧾 Order saved to history (orders.json).")
        except (OSError, TypeError) as e:
            print(f"❌ Error saving order history: {e}")
