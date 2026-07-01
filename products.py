"""
Process a purchase request for a specified quantity of the product.

This method attempts to purchase a given `quantity` of the product.
It first validates that the requested quantity is positive and does
not exceed the current stock. If valid, it reduces the product's
available stock and calculates the total cost based on the product's
unit price. If the purchase reduces the quantity to zero, the
product will be automatically deactivated via `set_quantity`.

:param quantity: The number of units of the product to purchase. Must
    be a positive integer.
:type quantity: int
:raises ValueError: If the requested `quantity` is less than or equal
    to 0.
:raises ValueError: If the requested `quantity` exceeds the available
    stock.
:return: The total cost of the purchased items.
:rtype: float
"""


class Product:
    """
    Represent a product available for purchase, managing its name, price,
    and quantity.

    This class provides a comprehensive model for a product, encompassing
    its core attributes such as a unique name, price, and current stock
    level. It includes functionalities for managing product availability,
    handling promotions, and processing purchase transactions. The class
    ensures data integrity by validating input values and maintaining
    an 'active' status, which indicates whether the product is available
    or not. Products with zero quantity are automatically deactivated.

    :ivar name: The unique identifier and name of the product.
    :type name: str
    :ivar price: The unit price of the product.
    :type price: float
    :ivar active: A boolean flag indicating if the product is currently active
        and available.
    :type active: bool
    :ivar promotion: An object representing an active promotion applied to
        the product. This can be ``None`` if no promotion is active.
    :type promotion: object or None
    """

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Initialize a new product instance with the given name, price, and initial quantity.

        This constructor sets up the basic attributes of a product, including its
        name, price, and stock quantity. It ensures that critical attributes
        like name and price meet initial validity constraints. The product
        is initially marked as active and without any active promotions.
        Quantity assignment and validation are delegated to the `set_quantity`
        method.

        :param name: The unique name identifier for the product.
        :type name: str
        :param price: The unit price of the product. Must be a positive value.
        :type price: float
        :param quantity: The initial stock quantity for the product.
        :type quantity: int
        :raises ValueError: If `name` is an empty string.
        :raises ValueError: If `price` is not greater than 0.
        :raises ValueError: If `quantity` is less than 0 (raised by `set_quantity`).
        :return: None
        :rtype: None
        """
        if not name:
            raise ValueError("Name is required")
        if price <= 0:
            raise ValueError("Price must be greater than 0")
        self.name = name
        self.price = price
        self.active = True
        self.promotion = None
        self.set_quantity(quantity)

    def get_promotion(self):
        """
        Retrieve the promotion associated with the instance.

        :return: The promotion identifier or object currently associated with the
            instance.
        :rtype: str
        """
        return self.promotion

    def set_promotion(self, promotion) -> None:
        """
        Set the promotion attribute for the instance.

        This method assigns the provided `promotion` value to the instance's
        `promotion` attribute. It serves as a simple setter for this specific
        attribute.

        :param promotion: The value representing the promotion to be
            associated with the object.
        :type promotion: object
        :return: None
        :rtype: None
        """
        self.promotion = promotion

    def __repr__(self) -> str:

        return (
                f"Product(name={self.name}, price={self.price}, quantity={self.quantity})"
        )

    def get_quantity(self) -> int:
        """
        Get the quantity of the item.

        :return: The current quantity of the item.
        :rtype: int
        """
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
        :raises: This method explicitly raises no exceptions.
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

    def __str__(self) -> str:
        """
        Return a string representation of the item.

        This method constructs a human-readable string that includes the item's
        name, price, quantity, and optionally, the name of any associated
        promotion.

        :return: A formatted string detailing the item's attributes.
        :rtype: str
        """
        promotion_info = f", Promotion: {self.promotion.name}" if self.promotion else ""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}{promotion_info}"

    # def show(
    #     self,
    # ) -> None:  # only using show() and not __repr__() because it is asked for in the instructions
    #     """
    #     Display the item's name, price, and quantity.
    #
    #     This method prints a user-friendly string representation of the
    #     `Item` object's current state to standard output, including its
    #     name, price, and quantity. It is intended for quick inspection
    #     or simple display purposes rather than a formal string
    #     representation (`__repr__` or `__str__`).
    #
    #     :return: None, as the method's primary effect is a side effect
    #         (printing to console) and it does not explicitly return a value.
    #     :rtype: None
    #     """
    #     promotion_info = f", Promotion: {self.promotion.name}" if self.promotion else ""
    #     print(
    #         f"{self.name}, Price: {self.price}, Quantity: {self.quantity}{promotion_info}"
    #     )

    def buy(self, quantity: int) -> float:
        """
        Processes a purchase for a specified quantity of the product, updating
        the available stock and calculating the total cost. This method ensures
        that the product is active, the quantity is valid, and sufficient stock
        is available before proceeding with the transaction.

        Args:
            quantity: The number of items to purchase. This must be a positive
                integer.

        Returns:
            The total monetary cost of the purchased quantity.

        Raises:
            ValueError: If the product is not currently marked as active,
                preventing any purchases.
            ValueError: If the requested quantity to buy is zero or a negative
                number, which is an invalid amount.
            ValueError: If the requested quantity exceeds the currently available
                stock for this product.
        """
        if not self.active:
            raise ValueError(f"Product '{self.name}' is not active.")
        if quantity <= 0:
            raise ValueError("Can't buy a negative amount of products")
        if quantity > self.quantity:
            raise ValueError(f"Not enough of {self.name} in stock")

        self.set_quantity(self.quantity - quantity)
        return float(
                self.price * quantity,
        )


class NonStockedProduct(Product):
    """
    Represent a product not kept in physical stock.

    This class extends the `Product` class to model items that do not maintain
    an inventory quantity. The `quantity` attribute for `NonStockedProduct`
    instances is always effectively zero, and methods related to stock management
    are overridden or adapted to reflect this characteristic. Purchases are
    calculated based on demand, not available stock.
    """

    def __init__(self, name: str, price: float) -> None:
        """
        Initialize a new product instance.

        This method initializes the base product attributes (name and price) by
        delegating to the superclass constructor, setting the initial quantity to zero.

        :param name: The unique identifier or name of the product.
        :param price: The unit price of the product.
        """
        super().__init__(name, price, quantity=0)

    def set_quantity(self, quantity: int) -> None:
        """
        Set the instance's quantity attribute to zero.

        This method assigns a fixed value of zero to the instance's `quantity`
        attribute. The `quantity` parameter provided to the method is
        intentionally ignored, effectively resetting the instance's quantity.

        :param quantity: The integer value intended for quantity, which is
                         ignored by the method's current implementation.
        :type quantity: int
        :return: No value is returned by this method.
        :rtype: None
        """
        self.quantity = 0

    def buy(self, quantity: int) -> float:
        """
        Calculate the total price for a specified quantity of the item.

        This method determines the final cost of purchasing a given number of
        items. If an active promotion is associated with the item, it applies
        the promotion's logic to calculate the discounted price. Otherwise, it
        computes the standard price based on the item's unit price.

        :param quantity: The number of items to be purchased.
        :raises ValueError: If the `quantity` is less than or equal to zero,
            indicating an invalid purchase amount.
        :return: The total calculated cost of the purchase.
        :rtype: float
        """
        if quantity <= 0:
            raise ValueError(f"Not enough of {self.name} in stock")

        if self.promotion:
            return self.promotion.apply_promotion(self, quantity)
        return float(self.price * quantity)

    def __str__(self) -> str:
        """
        Return a string representation of the product.

        This method generates a human-readable string that includes the product's
        name and price. If a promotion is associated with the product, its name
        is also appended to the string.

        :return: A formatted string containing the product's name, price,
                 and optionally, the promotion name.
        """
        promotion_info = f", Promotion: {self.promotion.name}" if self.promotion else ""
        return f"{self.name}, Price: {self.price}{promotion_info}"

    # def show(self) -> None:
    #
    #     promotion_info = f", Promotion: {self.promotion.name}" if self.promotion else ""
    #     print(f"{self.name}, Price: {self.price}{promotion_info}")


class LimitedProduct(Product):
    """
    Represent a product with a maximum purchase quantity allowed per order.

    This class extends the base :class:`Product` functionality by introducing a
    strict limit on the quantity of items that can be purchased in a single
    transaction. It ensures that any attempt to buy more than the `maximum`
    specified quantity will result in an error, adhering to sales or inventory
    policies.

    :ivar maximum: The maximum allowed quantity for a single purchase operation.
    :type maximum: int
    """

    def __init__(self, name: str, price: float, quantity: int, maximum: int) -> None:
        """
        Initialize the product with its name, price, quantity, and maximum stock level.

        :param name: The descriptive name of the product.
        :param price: The unit price of the product.
        :param quantity: The current stock quantity of the product.
        :param maximum: The maximum allowable stock quantity for this product.
        """
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, quantity: int) -> float:
        """
        Purchase a specified quantity of the product.

        This method attempts to buy the given `quantity` of the product,
        enforcing a per-order maximum limit. It prevents transactions that exceed
        the product's allowed quantity, ensuring adherence to inventory or sales
        policies.

        :param quantity: The number of units of the product to purchase.
        :raises ValueError: If the requested `quantity` exceeds the product's
            `maximum` purchase limit per order.
        :return: The total cost of the purchased quantity.
        """
        if quantity > self.maximum:
            raise ValueError(
                    f"Product {self.name} can only purchased up to {self.maximum} times per order"
            )
        return super().buy(quantity)

    def __str__(self) -> str:
        """
        Return a string representation of the product.

        This method provides a human-readable string that details the product's
        key attributes, including its name, current price, available quantity,
        the maximum amount permitted per order, and any active promotion. The
        promotion information is appended only if a `promotion` attribute is
        set on the object.

        :return: A formatted string describing the product's core details.
        :rtype: str
        """
        promotion_info = f", Promotion: {self.promotion.name}" if self.promotion else ""
        return (
                f"{self.name}, Price: {self.price}, Quantity: {self.quantity},"
                f" Max. amount/order: {self.maximum}{promotion_info}"
        )

    # def show(self) -> None:
    #     promotion_info = f", Promotion: {self.promotion.name}" if self.promotion else ""
    #     print(
    #         f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, Max. amount/order: {self.maximum}{promotion_info}"
    #     )
