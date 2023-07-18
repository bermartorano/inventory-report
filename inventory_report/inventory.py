from inventory_report.product import Product


class Inventory:
    def __init__(self, data: list[Product] | None = None):
        self.__data = data if data else []

    @property
    def data(self) -> list[Product]:
        return self.__data

    def add_data(self, data: list[Product]) -> None:
        for product in data:
            self.__data.append(product)
