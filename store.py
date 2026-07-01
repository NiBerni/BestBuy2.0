"""
Manage a collection of products for inventory and ordering operations.

This class provides functionality to add, remove, and query products
within an internal collection. It supports calculating total quantities
and processing orders based on product-specific pricing logic.
Products are expected to be instances of the :class:`~products.Product`
class, which should implement methods such as `get_quantity`,
`is_active`, and `buy`.

:ivar products: The internal list of :class:`~products.Product`
    objects currently managed by this store instance.
:vartype products: list[products.Product]
"""

import products


class Store:
    """
    Manage a collection of products for inventory and ordering operations.

    This class provides functionality to add, remove, and query products
    within an internal collection. It supports calculating total quantities
    and processing orders based on product-specific pricing logic.
    Products are expected to be instances of the :class:`~products.Product`
    class, which should implement methods such as `get_quantity`,
    `is_active`, and `buy`.

    :ivar products: The internal list of :class:`~products.Product`
        objects currently managed by this store instance.
    :vartype products: list[products.Product]
    """

    def __init__(self, product_list: list[products.Product]) -> None:
        """
        Initialize the product list with a collection of products.

        This constructor assigns the provided list of :class:`~products.Product`
        objects to the instance's internal storage, making them available
        for management operations.

        :param product_list: The initial list of product objects to be
            managed by this instance.
        :type product_list: list[products.Product]
        """
        self.products = product_list

    def add_product(self, product) -> None:
        """
        Add a product instance to the collection of products.

        This method appends the given product object to the internal list of
        products maintained by the class instance. It directly modifies the
        state of the object by adding the product to the `self.products` list.

        :param product: The product instance to be added to the collection.
        :type product: object
        :return: None, as this method modifies the object's state in-place.
        """
        self.products.append(product)

    def remove_product(self, product) -> None:
        """
        Remove a specified product from the collection.

        This method checks if the given product exists within the internal
        `products` list and removes the first occurrence of it if found.
        If the product is not present in the collection, no action is taken.

        :param product: The product item to be removed from the collection.
        :type product: Any
        :return: None
        :rtype: None
        """
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self) -> int:
        """
        Get the total quantity of all products managed by the instance.

        This method iterates through the `products` list, which is expected to be
        an attribute of the class instance. For each product, it calls the
        `get_quantity()` method to retrieve its individual quantity and
        accumulates these values to compute the grand total.

        :return: The sum of quantities from all products.
        :rtype: int
        """
        total_quantity = 0
        for product in self.products:
            total_quantity += product.get_quantity()
        return total_quantity

    def get_all_products(self) -> list[products.Product]:
        """
        Retrieve all active products managed by the service.

        This method iterates through the service's internal collection of products
        and filters them, returning only those instances that are currently
        marked as active based on their ``is_active`` status.

        :return: A list of `Product` objects that are currently active.
        """
        active_products = [product for product in self.products if product.is_active()]
        return active_products

    def order(self, shopping_list: list[tuple[products.Product, int]]) -> float:
        """
        Calculate the total price of all products in a shopping list.

        Iterates through each product and its corresponding quantity in the
        provided shopping list. For each item, it calls the product's `buy`
        method to determine its cost for the specified quantity and accumulates
        this cost into a running total.

        :param shopping_list: A list of tuples, where each tuple contains a
            `products.Product` object and the integer quantity to be purchased.
        :return: The aggregate price of all items after applying their
            respective `buy` logic.
        """
        total_price = 0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price

    def __repr__(self) -> str:
        return f"Store(products={self.products})"


if __name__ == "__main__":
    main()
