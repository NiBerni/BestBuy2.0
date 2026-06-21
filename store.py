import products


class Store:

	def __init__(self, product_list: list[products.Product]) -> None:
		self.products = product_list

	def add_product(self, product) -> None:
		self.products.append(product)

	def remove_product(self, product) -> None:
		if product in self.products:
			self.products.remove(product)

	def get_total_quantity(self) -> int:

		total_quantity = 0
		for product in self.products:
			total_quantity += product.get_quantity()
		return total_quantity

	def get_all_products(self) -> list[products.Product]:
		active_products = [product for product in self.products if product.is_active()]
		return active_products

	def order(self, shopping_list: list[tuple[products.Product, int]]) -> float:

		total_price = 0
		for product, quantity in shopping_list:
			total_price += product.buy(quantity)
		return total_price

	def __repr__(self) -> str:
		return f"Store(products={self.products})"


def main():
	product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
	                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
	                products.Product("Google Pixel 7", price=500, quantity=250),
	                ]
	best_buy = Store(product_list)
	products_in_store = best_buy.get_all_products()
	print(products_in_store)
	print(best_buy.get_total_quantity())
	print(best_buy.order([(products_in_store[0], 1), (products_in_store[1], 2)]))


if __name__ == "__main__":
	main()
