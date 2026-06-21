import products
import store


def start(store_obj: store.Store) -> None:
	while True:
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
		choice = input("\n Please enter your choice: \n ").strip()

		if choice == "1":
			print()
			print(80 * "_")
			print()
			all_products = store_obj.get_all_products()
			for i, product in enumerate(all_products, start=1):
				print(f"{i}.", end="")
				product.show()
			print()
			print(80 * "_")

		elif choice == "2":
			total_amount = store_obj.get_total_quantity()
			print()
			print(f"Total amount of products in the store: {total_amount}")

		elif choice == "3":
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

					quantity_choice = input(f"How many {all_products[product_index].name} do you want? \n ").strip()
					quantity = int(quantity_choice)

					selected_product = all_products[product_index]
					shopping_list.append((selected_product, quantity))
				except ValueError as shopping_list_error:
					print(f"Invalid product number {shopping_list_error}")

			if shopping_list:
				try:
					total_price = store_obj.order(shopping_list)
					print(f"\n Order made successfully!\n Your total price is: $ {total_price}\n")
					print(80 * "$")
				except ValueError as order_error:
					print(f"Error: {order_error}")
				shopping_list.clear()
			else:
				print("No products added to the order")

		elif choice == "4":
			print("\n Thank you for using BestBuy \n Exiting... \n Bye!")
			break
		else:
			print("Please enter a valid choice (1-4).")


def main():
	product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
	                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
	                products.Product("Google Pixel 7", price=500, quantity=250)
	                ]
	best_buy = store.Store(product_list)
	start(best_buy)


if __name__ == "__main__":
	main()
