import sys
from typing import Optional

from models.order import Order
from models.catalog import Catalog
from models.database import append_order, load_orders


catalog = Catalog()
current_order: Optional[Order] = None


def show_catalog() -> None:
    print("\n--- 📦 Product Catalog ---")
    for i, product in enumerate(catalog, start=1):
        print(f"{i}. {product}")


def create_order() -> None:
    global current_order

    if current_order and current_order.status == "OPEN":
        print(
            f"⚠️ There is already an open order for {current_order.customer_name}.")
        print("   Finish it, cancel it, or view the cart.")
        return

    name = input("Enter customer name: ").strip()
    if not name:
        print("❌ Customer name cannot be empty.")
        return

    current_order = Order(name)
    print(f"\n✅ Order started for {name}!")


def view_cart() -> None:
    if not current_order:
        print("⚠️ No open order.")
        return

    print("\n--- 🛒 Current Cart ---")
    print(current_order.summary())


def add_item() -> None:
    global current_order

    if not current_order:
        print("⚠️ Create an order first.")
        return

    show_catalog()
    try:
        choice = int(input("\nProduct number: ")) - 1
        qty = int(input("Quantity: "))

        if 0 <= choice < len(catalog):
            product = catalog.get(choice)
            current_order.add_item(product, qty)
            catalog.save()
        else:
            print("❌ Invalid product.")
    except ValueError:
        print("❌ Enter only numbers.")


def remove_item() -> None:
    global current_order

    if not current_order:
        print("⚠️ No open order.")
        return
    if current_order.is_empty():
        print("🛒 Cart is empty.")
        return

    print("\n--- 🗑️ Remove Item ---")
    print(current_order.summary())

    try:
        idx = int(input("\nCart item number to remove: ")) - 1
        qty_raw = input(
            "Quantity to remove (ENTER = remove whole line): ").strip()

        if qty_raw == "":
            current_order.remove_item(idx, None)
        else:
            qty = int(qty_raw)
            current_order.remove_item(idx, qty)

        catalog.save()
    except ValueError:
        print("❌ Enter only numbers.")


def cancel_order() -> None:
    global current_order

    if not current_order:
        print("⚠️ No open order.")
        return

    confirm = input(
        f"Cancel order for {current_order.customer_name}? (y/n): ").strip().lower()
    if confirm != "y":
        print("ℹ️ Cancel aborted.")
        return

    current_order.cancel()
    catalog.save()
    current_order = None


def finish_order() -> None:
    global current_order

    if not current_order:
        print("⚠️ No order to finish.")
        return

    current_order.finish_order()
    if current_order.status == "PAID":
        # Save to history BEFORE clearing
        append_order(current_order.to_record())
        catalog.save()
        current_order = None


def view_order_history() -> None:
    orders = load_orders()
    if not orders:
        print("ℹ️ No orders in history yet.")
        return

    print("\n--- 🧾 Order History (latest first) ---")
    for i, order in enumerate(reversed(orders[-10:]), start=1):
        name = order.get("customer_name", "Unknown")
        status = order.get("status", "Unknown")
        total = order.get("total", 0.0)
        when = order.get("finished_at_utc", "Unknown time")
        print(f"{i}. {name} | {status} | Total: ${float(total):.2f} | {when}")


def main() -> None:
    catalog.load_or_seed()

    while True:
        print("\n" + "=" * 34)
        print("   🛒 PYSTORE CLI (WITH DATABASE)")
        print("=" * 34)
        print("1. View Catalog")
        print("2. New Order")
        print("3. Add Item")
        print("4. View Cart")
        print("5. Remove Item")
        print("6. Cancel Order")
        print("7. Finish Order (Checkout)")
        print("8. View Order History")
        print("0. Exit")

        option = input("Option: ").strip()

        if option == "1":
            show_catalog()
        elif option == "2":
            create_order()
        elif option == "3":
            add_item()
        elif option == "4":
            view_cart()
        elif option == "5":
            remove_item()
        elif option == "6":
            cancel_order()
        elif option == "7":
            finish_order()
        elif option == "8":
            view_order_history()
        elif option == "0":
            catalog.save()
            print("Exiting... Come back soon! 👋")
            sys.exit()
        else:
            print("❌ Invalid option.")


if __name__ == "__main__":
    main()
