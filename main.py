import sys
from typing import List, Optional
from models.product import Product, PhysicalProduct, DigitalProduct
from models.order import Order

# --- 1. Simulated Database (In Memory) ---
catalog: List[Product] = []
current_order: Optional[Order] = None


def initial_setup():
    """Creates some products so the store does not start empty."""
    catalog.append(PhysicalProduct("iPhone 15", 900.00, 10, 0.2))
    catalog.append(PhysicalProduct("Dell Laptop", 1500.00, 5, 2.5))
    catalog.append(DigitalProduct("Python Pro Ebook", 29.90, 1000, 15.0))
    catalog.append(DigitalProduct("Antivirus License", 50.00, 1000, 0.0))


def show_catalog():
    print("\n--- 📦 Product Catalog ---")
    for i, product in enumerate(catalog):
        print(f"{i + 1}. {product}")


def create_order():
    global current_order
    customer_name = input("Enter customer name: ")
    current_order = Order(customer_name)
    print(f"\n✅ Order started for {customer_name}!")


def add_item():
    if not current_order:
        print("⚠️ You need to create an order first (Option 2).")
        return

    show_catalog()
    try:
        choice = int(input("\nEnter the product number: ")) - 1
        quantity = int(input("Enter the quantity: "))

        if 0 <= choice < len(catalog):
            selected_product = catalog[choice]
            current_order.add_item(selected_product, quantity)
        else:
            print("❌ Invalid product.")
    except ValueError:
        print("❌ Please enter numbers only.")


def view_cart():
    if not current_order:
        print("⚠️ No open order.")
        return

    print("\n--- 🛒 Your Cart ---")
    print(current_order)  # Uses Order.__str__()
    for item in current_order.items:
        print(f"   - {item}")


def finish_order():
    global current_order
    if not current_order:
        print("⚠️ No order to finish.")
        return

    current_order.finish_order()
    current_order = None  # Clears the current order to start a new one


# --- MAIN MENU ---

def main():
    initial_setup()

    while True:
        print("\n" + "=" * 30)
        print("   🛒 PYSTORE CLI V1.0")
        print("=" * 30)
        print("1. View Catalog")
        print("2. New Order")
        print("3. Add Item to Cart")
        print("4. View Cart")
        print("5. Checkout")
        print("0. Exit")

        option = input("\nChoose an option: ")

        if option == "1":
            show_catalog()
        elif option == "2":
            create_order()
        elif option == "3":
            add_item()
        elif option == "4":
            view_cart()
        elif option == "5":
            finish_order()
        elif option == "0":
            print("Exiting... Come back soon! 👋")
            sys.exit()
        else:
            print("❌ Invalid option.")


if __name__ == "__main__":
    main()
