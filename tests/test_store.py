# pylint: disable=missing-docstring

from products import Product
from store import Store


def test_store_add_remove_product() -> None:

    p1 = Product("Test 1", price=10, quantity=10)
    p2 = Product("Test 2", price=20, quantity=20)
    store = Store([p1])

    store.add_product(p2)
    assert len(store.products) == 2

    store.remove_product(p1)
    assert len(store.products) == 1
    assert store.products[0].name == "Test 2"


def test_store_get_total_quantity() -> None:

    p1 = Product("Test 1", price=10, quantity=10)
    p2 = Product("Test 2", price=20, quantity=20)
    store = Store([p1, p2])

    assert store.get_total_quantity() == 30


def test_store_get_all_products() -> None:

    p1 = Product("Test 1", price=10, quantity=10)
    p2 = Product("Test 2", price=20, quantity=0)
    store = Store([p1, p2])

    active_products = store.get_all_products()

    assert len(active_products) == 1
    assert active_products[0].name == "Test 1"


def test_store_order() -> None:

    p1 = Product("Test 1", price=10, quantity=10)
    p2 = Product("Test 2", price=20, quantity=20)
    store = Store([p1, p2])
    shopping_list = [(p1, 2), (p2, 1)]

    assert store.order(shopping_list) == 40.0
    assert p1.quantity == 8
    assert p2.quantity == 19