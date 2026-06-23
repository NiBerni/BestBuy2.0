import pytest

from products import Product


def test_create_normal_product() -> None:

    product = Product("Test Product 1", price=1455, quantity=100)
    assert product.name == "Test Product 1"
    assert product.price == 1455
    assert product.quantity == 100
    assert product.is_active() is True


def test_create_product_invalid_details() -> None:

    # Empty name
    with pytest.raises(ValueError):
        Product("", price=1455, quantity=100)
    # Negative price
    with pytest.raises(ValueError):
        Product("Test Product 1", price=-1, quantity=100)
    # Negative quantity
    with pytest.raises(ValueError):
        Product("Test Product 1", price=1455, quantity=-1)


def test_product_reaches_zero_quantity() -> None:

    product = Product("Test Product 1", price=1455, quantity=1)
    product.buy(1)
    assert product.quantity == 0
    assert product.is_active() is False


def test_product_purchase_modifies_quantity_and_returns_right_output() -> None:

    product = Product("Test Product 1", price=1455, quantity=100)
    assert product.buy(5) == 7275.0
    assert product.quantity == 95


def test_buy_larger_quantity_than_existed() -> None:

    product = Product("Test Product 1", price=1455, quantity=100)
    with pytest.raises(ValueError):
        product.buy(101)


def test_buy_negative_amount() -> None:

    product = Product("Test Product 1", price=1455, quantity=100)
    with pytest.raises(ValueError):
        product.buy(-1)


def test_buy_zero_amount() -> None:
    product = Product("Test Product 1", price=1455, quantity=100)
    with pytest.raises(ValueError):
        product.buy(0)
