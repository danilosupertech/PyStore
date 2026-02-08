from __future__ import annotations

import json
import os
from typing import List

from models.product import Product, PhysicalProduct, DigitalProduct


class InventoryRepository:
    """Reads/writes inventory.json. No business rules here."""

    def __init__(self, base_dir: str) -> None:
        self.inventory_file = os.path.join(base_dir, "inventory.json")

    def exists(self) -> bool:
        return os.path.exists(self.inventory_file)

    def load(self) -> List[Product]:
        if not self.exists():
            return []

        try:
            with open(self.inventory_file, "r", encoding="utf-8") as f:
                data = json.load(f)

            if not isinstance(data, list):
                print("❌ inventory.json is not a list. Ignoring.")
                return []

            products: List[Product] = []
            for idx, item in enumerate(data, start=1):
                try:
                    products.append(Product.from_dict(item))
                except Exception as e:
                    print(f"❌ Failed to load inventory item #{idx}: {item}")
                    print(f"   Reason: {e}")

            return products

        except (OSError, json.JSONDecodeError) as e:
            print(f"❌ Error reading inventory: {e}")
            return []

    def save(self, products: List[Product]) -> None:
        data_list = [p.to_dict() for p in products]
        try:
            with open(self.inventory_file, "w", encoding="utf-8") as f:
                json.dump(data_list, f, indent=4)
            print("💾 Inventory saved successfully!")
        except (OSError, TypeError) as e:
            print(f"❌ Error saving inventory: {e}")


def default_seed_products() -> List[Product]:
    """Default seed used when inventory.json does not exist or is empty."""
    return [
        PhysicalProduct("iPhone 15", 900.00, 10, 0.2),
        PhysicalProduct("Notebook Dell", 1500.00, 5, 2.5),
        DigitalProduct("Python Ebook", 29.90, 1000, 15.0),
    ]
