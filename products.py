"""
Represent a product available for purchase in an inventory system.

This class manages product details such as name, price, current stock
quantity, and its active status. It provides methods for updating
the quantity, activating/deactivating the product, and simulating
purchase operations, including checks for stock availability.

:ivar name: The name of the product.
:type name: str
:ivar price: The price per unit of the product.
:type price: float
:ivar active: The active status of the product; True if available for
    purchase, False otherwise.
:type active: bool
:ivar quantity: The current stock quantity of the product.
:type quantity: int
"""


class Product:
	"""
	Represent a product available for purchase in an inventory system.

	This class manages product details such as name, price, current stock
	quantity, and its active status. It provides methods for updating
	the quantity, activating/deactivating the product, and simulating
	purchase operations, including checks for stock availability.

	:ivar name: The name of the product.
	:type name: str
	:ivar price: The price per unit of the product.
	:type price: float
	:ivar active: The active status of the product; True if available for
	    purchase, False otherwise.
	:type active: bool
	:ivar quantity: The current stock quantity of the product.
	:type quantity: int
	"""

	def __init__(self, name: str, price: float, quantity: int) -> None:
		"""
		Initialize a new product instance with the given name, price, and quantity.

		This constructor validates the product's name and price, ensuring they
		meet the business rules before setting the initial state. The `active`
		status is set to True by default, and the quantity is set using a
		dedicated method (`set_quantity`), which handles its own validation
		and assignment.

		:param name: The unique name of the product. Must not be an empty string,
		    as it serves as a primary identifier.
		:param price: The monetary value of a single unit of the product.
		    Must be a positive number greater than zero to ensure valid pricing.
		:param quantity: The initial stock level for the product. This value is
		    passed to the `set_quantity` method for further validation and
		    assignment, ensuring inventory integrity from creation.
		:raises ValueError: If `name` is an empty string, indicating a missing
		    or invalid product identifier that is essential for product management.
		:raises ValueError: If `price` is not greater than zero, ensuring that
		    products have a valid, positive cost in the system.
		:return: None, as this is an initializer method and does not explicitly
		    return a value.
		:rtype: None
		"""
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
		"""
		Set the quantity of the item and handle its deactivation if quantity
		reaches zero.

		This method updates the ``quantity`` attribute of the object. A negative
		quantity is not allowed and will result in a :exc:`ValueError`.
		If the updated quantity becomes zero, the :meth:`deactivate` method is
		automatically called to signal that the item is no longer available
		or active.

		:param quantity: The new integer value for the item's quantity.
		:raises ValueError: If the provided ``quantity`` is less than 0.
		:return: None.
		"""
		if quantity < 0:
			raise ValueError("Quantity can not be less than 0")
		self.quantity = quantity
		if self.quantity == 0:
			self.deactivate()

	def is_active(self) -> bool:
		"""
		Check if the object is active.

		:return: True if the object is active, False otherwise.
		"""
		return self.active

	def activate(self) -> None:
		"""
		Set the object's active status to True.

		This method marks the current instance as active, typically enabling
		subsequent operations or state changes that depend on an active status.
		It changes the internal state of the object by setting the ``active``
		attribute to ``True``.

		:param self: The instance of the object to be activated.
		:type self: object
		:return: Indicates that the method completes its execution without
		    returning any specific value.
		:raises: No exceptions are explicitly raised by this method.
		"""
		self.active = True

	def deactivate(self) -> None:
		"""
		Deactivate the object by setting its active status to False.

		This method sets the ``active`` attribute of the object instance to ``False``,
		effectively marking the object as inactive. This operation is idempotent,
		meaning repeated calls will not change the object's state further
		if it is already inactive.

		:param self: The instance of the object to be deactivated.
		:type self: object
		:return: None.
		:raises: This method does not explicitly raise any exceptions.
		"""
		self.active = False

	def show(self) -> None:  # only using show() and not __repr__() because it is asked for in the instructions
		"""
		Display the item's name, price, and quantity.

		This method prints a user-friendly string representation of the
		`Item` object's current state to standard output, including its
		name, price, and quantity. It is intended for quick inspection
		or simple display purposes rather than a formal string
		representation (`__repr__` or `__str__`).

		:return: None, as the method's primary effect is a side-effect
		    (printing to console) and it does not explicitly return a value.
		:rtype: None
		"""
		print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

	def buy(self, quantity: int) -> float:
		"""
		Process a purchase request for a specified quantity of the products.

		This method decrements the available stock quantity by the
		`quantity` requested and calculates the total cost of the purchase.
		It validates the input `quantity` to ensure it is positive and does
		not exceed the currently available stock.

		:param quantity: The number of units of the product to purchase.
		:type quantity: int
		:raises ValueError: If `quantity` is less than or equal to zero.
		:raises ValueError: If the requested `quantity` exceeds the currently
		    available stock.
		:return: The total monetary cost of the transaction.
		:rtype: float
		"""
		if quantity <= 0:
			raise ValueError("Can't buy a negative amount of products")
		if quantity > self.quantity:
			raise ValueError(f"Not enough of {self.name} in stock")

		self.set_quantity(self.quantity - quantity)
		return float(self.price * quantity, )


def main():
	"""
	Demonstrate the functionality of the `Product` class.
	"""
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
