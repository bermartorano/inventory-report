from inventory_report.product import Product

prod_mock = {
    'id': '654',
    'company_name': 'Empresa SA',
    'product_name': 'produto da empresa',
    'manufacturing_date': '2023-01-30',
    'expiration_date': '2024-01-30',
    'serial_number': '123456789',
    'storage_instructions': 'keep it away from heat',
}


def test_create_product() -> None:
    new_prod = Product(
        prod_mock['id'],
        prod_mock['product_name'],
        prod_mock['company_name'],
        prod_mock['manufacturing_date'],
        prod_mock['expiration_date'],
        prod_mock['serial_number'],
        prod_mock['storage_instructions']
    )

    assert new_prod.id == prod_mock['id']
    assert new_prod.product_name == prod_mock['product_name']
    assert new_prod.company_name == prod_mock['company_name']
    assert new_prod.manufacturing_date == prod_mock['manufacturing_date']
    assert new_prod.expiration_date == prod_mock['expiration_date']
    assert new_prod.serial_number == prod_mock['serial_number']
    assert new_prod.storage_instructions == prod_mock['storage_instructions']
