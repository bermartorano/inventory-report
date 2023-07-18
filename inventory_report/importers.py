from typing import Dict, Type
from abc import ABC, abstractmethod
import json
from inventory_report.product import Product


class Importer(ABC):
    def __init__(self, path: str) -> None:
        self.path = path

    @abstractmethod
    def import_data(self) -> list[Product]:
        pass


class JsonImporter(Importer):
    def import_data(self) -> list[Product]:
        with open(self.path) as json_file:
            json_content = json.load(json_file)

        product_list = []
        for product_info in json_content:
            new_product = Product(
                product_info['id'],
                product_info['product_name'],
                product_info['company_name'],
                product_info['manufacturing_date'],
                product_info['expiration_date'],
                product_info['serial_number'],
                product_info['storage_instructions'],
            )
            product_list.append(new_product)

        return product_list


class CsvImporter(Importer):
    pass


# Não altere a variável abaixo

IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}
