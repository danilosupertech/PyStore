"""
database.py

Database module for saving/loading the product catalog (inventory.json)
and storing finished orders (orders.json).

NOTE:
This module handles only JSON I/O.
Object reconstruction is delegated to Product.from_dict() (domain).
"""
import json
import os
from typing import List, Dict, Any

from models.product import Product

# Always store JSON files at the project root (one folder above /models)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INVENTORY_FILE = os.path.join(BASE_DIR, "inventory.json")
ORDERS_FILE = os.path.join(BASE_DIR, "orders.json")


def inventory_exists() -> bool:
    """True if inventory.json exists on disk."""
    return os.path.exists(INVENTORY_FILE)


def save_catalog(products: List[Product]) -> None:
    """Save product catalog to inventory.json."""
    data_list = [p.to_dict() for p in products]

    try:
        with open(INVENTORY_FILE, "w", encoding="utf-8") as file:
            json.dump(data_list, file, indent=4)
        print("💾 Inventory saved successfully!")
    except (OSError, TypeError) as e:
        print(f"❌ Error saving inventory: {e}")


def load_catalog() -> List[Product]:
    """
    Reads the JSON and recreates product objects using Product.from_dict().
    Returns an empty list if the file does not exist or cannot be read.
    """
    if not os.path.exists(INVENTORY_FILE):
        return []

    try:
        with open(INVENTORY_FILE, "r", encoding="utf-8") as file:
            data_list = json.load(file)

        if not isinstance(data_list, list):
            print("❌ inventory.json is not a list. Ignoring.")
            return []

        print(f"📂 JSON records found: {len(data_list)}")

        products_catalog: List[Product] = []

        for idx, item in enumerate(data_list, start=1):
            try:
                product = Product.from_dict(item)
                products_catalog.append(product)
            except Exception as e:
                print(f"❌ Failed to load item #{idx}: {item}")
                print(f"   Reason: {e}")

        print(f"📂 {len(products_catalog)} products loaded from inventory.")
        return products_catalog

    except (OSError, json.JSONDecodeError) as e:
        print(f"❌ Error reading inventory: {e}")
        return []


def _load_orders_raw() -> List[Dict[str, Any]]:
    """Internal: load orders list from orders.json (or return empty list)."""
    if not os.path.exists(ORDERS_FILE):
        return []

    try:
        with open(ORDERS_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            return []
    except (OSError, json.JSONDecodeError) as e:
        print(f"❌ Error reading orders: {e}")
        return []


def append_order(order_record: Dict[str, Any]) -> None:
    """Append a finished order record to orders.json."""
    orders = _load_orders_raw()
    orders.append(order_record)

    try:
        with open(ORDERS_FILE, "w", encoding="utf-8") as file:
            json.dump(orders, file, indent=4)
        print("🧾 Order saved to history (orders.json).")
    except (OSError, TypeError) as e:
        print(f"❌ Error saving order history: {e}")


def load_orders() -> List[Dict[str, Any]]:
    """Public: load order history from orders.json."""
    return _load_orders_raw()
