from abc import ABC, abstractmethod


class Promotion(ABC):
    def __init__(self, name: str) -> None:
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity: int) -> float:

        pass


class PercentDiscount(Promotion):
    def __init__(self, name: str, percent: float | int) -> None:
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity: int) -> float:
        return float(product.price * quantity * (1 - self.percent / 100))


class SecondHalfPrice(Promotion):
    def apply_promotion(self, product, quantity: int) -> float:
        full_price_items = quantity - (quantity // 2)
        half_price_items = quantity // 2
        return float(
            (product.price * full_price_items)
            + (half_price_items * product.price * 0.5)
        )


class ThirdOneFree(Promotion):
    def apply_promotion(self, product, quantity: int) -> float:
        groups_of_three = quantity // 3
        remainder = quantity % 3
        return float((groups_of_three * 2 + remainder) * product.price)
