"""
Define the abstract base class for all promotion types.

This class serves as a blueprint for various promotion strategies, ensuring
that all concrete promotion implementations adhere to a common interface.
Subclasses must implement specific methods to define the promotion's logic,
such as how it applies to products or orders. It acts as a contract
that all derived promotion classes must fulfill.
"""

# pylint: disable=too-few-public-methods

from abc import ABC, abstractmethod


class Promotion(ABC):
    """
    Define the abstract base class for all promotion types.

    This class serves as a blueprint for various promotion strategies, ensuring
    that all concrete promotion implementations adhere to a common interface.
    Subclasses must implement specific methods to define the promotion's logic,
    such as how it applies to products or orders. It acts as a contract
    that all derived promotion classes must fulfill.
    """

    def __init__(self, name: str) -> None:
        """
        Initialize a new instance of the class.

        This constructor sets up the initial state of the object, assigning
        the provided name to an instance attribute.

        :param self: The instance of the class.
        :param name: The name to be associated with this instance.
        :return: None
        """
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity: int) -> float:
        """
        Apply a promotional discount to a given product and quantity.

        This abstract method calculates the final price after applying any
        applicable promotions or discounts for a specified product and its
        quantity. Implementations should define the specific promotion logic.

        :param product: The product object for which to apply the promotion.
        :type product: Any
        :param quantity: The number of units of the product.
        :return: The discounted total price for the given product and quantity.
        :rtype: float
        """


class PercentDiscount(Promotion):
    """
    Represent a percentage-based discount promotion.

    This class models a promotional discount applied as a fixed percentage
    off the original price of an item or service. It inherits core promotion
    functionalities from the `Promotion` base class and specifically implements
    the logic for calculating the final price after applying a percentage-based
    reduction. The discount percentage is stored as an instance variable.

    :ivar percent: The percentage value of the discount to be applied.
                       This value should be between 0.0 and 100.0,
                       inclusive, where 100.0 represents a full discount.
    :type percent: float
    """

    def __init__(self, name: str, percent: float | int) -> None:
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity: int) -> float:
        return float(product.price * quantity * (1 - self.percent / 100))


class SecondHalfPrice(Promotion):
    """
    Represents a 'buy one, get one half price' promotional offer.

    This promotion applies a discount where every second item purchased
    is sold at half its original price. It is a specific implementation
    of a broader `Promotion` concept, designed to be applied to individual
    products within an order.
    """

    def apply_promotion(self, product, quantity: int) -> float:
        """
        Apply a promotional discount to a product's price based on quantity.

        This method calculates the final price for a given product, taking into
        account any specific promotions that might apply based on the quantity
        purchased. The exact promotional logic is handled internally.

        :param product: The product object to which the promotion is applied.
        :type product: object
        :param quantity: The number of units of the product being purchased.
        :return: The total price after applying the promotion.
        :rtype: float
        """
        full_price_items = quantity - (quantity // 2)
        half_price_items = quantity // 2
        return float(
            (product.price * full_price_items)
            + (half_price_items * product.price * 0.5)
        )


class ThirdOneFree(Promotion):
    """
    Implement a 'buy two, get the third free' promotion.

    This class defines a specific promotional rule where for every set of
    items purchased, a certain quantity within that set is offered for
    free. It's typically applied to the lowest-priced item(s) within the
    qualifying set of products. The promotion inherently requires at least
    three items to be eligible for any discount.

    :ivar items_per_set: The number of items that must be purchased as
        part of a qualifying set to trigger the free item benefit. For a
        "third one free" promotion, this value is typically 3.
    :type items_per_set: int
    :ivar free_items_per_set: The number of items awarded for free within
        each complete qualifying set. For a "third one free" promotion,
        this value is typically 1.
    :type free_items_per_set: int
    """

    def apply_promotion(self, product, quantity: int) -> float:
        """
        Apply a promotional discount to a product based on the specified quantity.

        This method calculates the final price of a product after applying any
        relevant promotions. Promotions might include volume discounts, special
        offer pricing, or other conditional price reductions that depend on the
        purchased quantity or the product's attributes. The specific rules for
        applying promotions are determined by the implementing class.

        :param self: The instance of the class containing this method.
        :param product: The product to which the promotion should be applied. This
            could be a product identifier, a dictionary representing product
            details, or a specific product object.
        :type product: Any
        :param quantity: The number of units of the product being considered for
            promotion.
        :raises ValueError: If the quantity is non-positive, or if the product
            is not recognized or valid for promotion.
        :raises TypeError: If the product parameter is of an unexpected type that
            prevents promotion calculation.
        :return: The total price of the product after applying all applicable
            promotions for the given quantity.
        """
        groups_of_three = quantity // 3
        remainder = quantity % 3
        return float((groups_of_three * 2 + remainder) * product.price)
