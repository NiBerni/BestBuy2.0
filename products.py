class Product:

	def __init__(self, name: str, price: float, quantity: int) -> None:
		if not name:
			raise ValueError("Name is required")
		if price <= 0:
			raise ValueError("Price must be greater than 0")
		self.name = name
		self.price = price
		self.active = True
		self.set_quantity(quantity)

	def __repr__(self) -> str:

		return f"Product(name={self.name}, price={self.price}, quantity={self.quantity})"

	def get_quantity(self) -> int:
		return self.quantity

	def set_quantity(self, quantity: int) -> None:

		if quantity < 0:
			raise ValueError("Quantity can not be less than 0")
		self.quantity = quantity
		if self.quantity == 0:
			self.deactivate()

	def is_active(self) -> None:
		return self.active

	def activate(self) -> None:
		self.active = True

	def deactivate(self) -> None:
		self.active = False

	def show(self) -> None:  # only using show() and not __repr__() beacause it is asked for in the instructions

		print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

	def buy(self, quantity: int) -> None:
		if quantity <= 0:
			raise ValueError("Can't buy a negative amount of products")
		if quantity > self.quantity:
			raise ValueError(f"Not enough of {self.name} in stock")

		self.set_quantity(self.quantity - quantity)
		return float(self.price * quantity, )


def main():
	headphones = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
	macbook = Product("MacBook Air M2", price=1450, quantity=100)

	print(headphones.buy(50))
	print(macbook.buy(100))
	print(macbook.is_active())

	headphones.show()
	macbook.show()

	headphones.set_quantity(1000)
	headphones.show()


if __name__ == "__main__":
	main()
