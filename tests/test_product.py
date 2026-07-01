# pylint: disable=missing-docstring
import pytest

import promotions
from products import LimitedProduct, NonStockedProduct, Product


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


def test_non_stocked_product() -> None:

    product = NonStockedProduct("Windows License", price=125)
    assert product.quantity == 0
    assert product.buy(5) == 625.0
    assert product.quantity == 0


def test_limited_product() -> None:

    product = LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
    assert product.buy(1) == 10.0
    with pytest.raises(ValueError):
        product.buy(2)


def test_percent_discount() -> None:

    product = Product("Test Product", price=100, quantity=10)
    discount = promotions.PercentDiscount("20% off", percent=20)
    product.set_promotion(discount)
    assert product.buy(2) == 160.0


def test_second_half_price() -> None:

    product = Product("Test Product", price=100, quantity=10)
    discount = promotions.SecondHalfPrice("Second Half Price")
    product.set_promotion(discount)
    assert product.buy(2) == 150.0
    assert product.buy(3) == 250.0


def test_third_one_free() -> None:

    product = Product("Test Product", price=100, quantity=10)
    discount = promotions.ThirdOneFree("Third One Free")
    product.set_promotion(discount)
    assert product.buy(3) == 200.0
    assert product.buy(4) == 300.0


def test_product_str() -> None:

    product = Product("Test Product", price=100, quantity=10)
    assert str(product) == "Test Product, Price: 100, Quantity: 10"
    discount = promotions.PercentDiscount("20% off", percent=20)
    product.set_promotion(discount)
    assert str(product) == "Test Product, Price: 100, Quantity: 10, Promotion: 20% off"
