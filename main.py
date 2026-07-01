"""
Initiate the main user interface for the Best Buy store application.

This function runs an interactive command-line interface, allowing users to
browse products, check inventory, and place orders. It continually displays a
menu with options to list products, view total inventory, place an order, or
exit the application. Input validation is performed for menu choices and
product selections during the ordering process.

:param store_obj: The store object providing access to product data and
    ordering functionality.
:return: This function does not return any value; it runs indefinitely until
    the user explicitly chooses to exit.
"""

import products
import store


def display_menu() -> str:
    """Display the main menu and return the user's choice."""
    print()
    print(80 * "=")
    print("Welcome to the Best Buy store!")
    print(80 * "=")
    print()
    print("1. List all products in the store")
    print("2. Show total amount of products in the store")
    print("3. Place your order")
    print("4. Exit")
    print()
    print(80 * "_")
    return input("\n Please enter your choice: \n ").strip()


def list_products(store_obj: store.Store) -> None:
    """List all active products in the store."""
    print()
    print(80 * "_")
    print()
    all_products = store_obj.get_all_products()
    for i, product in enumerate(all_products, start=1):
        print(f"{i}.", end="")
        product.show()
    print()
    print(80 * "_")


def show_total_quantity(store_obj: store.Store) -> None:
    """Display the total quantity of all products."""
    total_amount = store_obj.get_total_quantity()
    print()
    print(f"Total amount of products in the store: {total_amount}")


def place_order(store_obj: store.Store) -> None:
    """Handle the interactive ordering process."""
    print()
    print(80 * "_")
    all_products = store_obj.get_all_products()
    for i, product in enumerate(all_products, start=1):
        print(f"{i}.", end="")
        product.show()
    print()
    print(80 * "_")
    print()
    print("For finishing your order enter an empty line.")

    shopping_list = []
    while True:
        product_choice = input("\n Which product # do you want? \n ").strip()
        if product_choice == "":
            break
        try:
            product_index = int(product_choice) - 1
            if product_index < 0 or product_index >= len(all_products):
                print("Invalid product number")
                continue

            quantity_choice = input(
                    f"How many {all_products[product_index].name} do you want? \n "
            ).strip()
            quantity = int(quantity_choice)

            selected_product = all_products[product_index]
            shopping_list.append((selected_product, quantity))
        except ValueError as shopping_list_error:
            print(f"Invalid product number {shopping_list_error}")

    if shopping_list:
        try:
            total_price = store_obj.order(shopping_list)
            print(
                    f"\n Order made successfully!\n Your total price is: $ {total_price}\n"
            )
            print(80 * "$")
        except ValueError as order_error:
            print(f"Error: {order_error}")
        shopping_list.clear()
    else:
        print("No products added to the order")


def start(store_obj: store.Store) -> None:
    """
    Initiate the main user interface for the Best Buy store application.

    This function runs an interactive command-line interface, allowing users to
    browse products, check inventory, and place orders. It continually displays a
    menu with options to list products, view total inventory, place an order, or
    exit the application. Input validation is performed for menu choices and
    product selections during the ordering process.

    :param store_obj: The store object providing access to product data and
        ordering functionality.
    :return: This function does not return any value; it runs indefinitely until
        the user explicitly chooses to exit.
    """
    while True:
        choice = display_menu()

        if choice == "1":
            list_products(store_obj)

        elif choice == "2":
            show_total_quantity(store_obj)

        elif choice == "3":
            place_order(store_obj)

        elif choice == "4":
            print("\n Thank you for using BestBuy \n Exiting... \n Bye!")
            break
        else:
            print("Please enter a valid choice (1-4).")


def main():
    """
    Set up the application's initial state and start its main loop.
    """
    product_list = [
            products.Product("MacBook Air M2", price=1450, quantity=100),
            products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
            products.Product("Google Pixel 7", price=500, quantity=250),
    ]
    best_buy = store.Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()
