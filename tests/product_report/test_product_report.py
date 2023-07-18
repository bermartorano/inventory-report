from inventory_report.product import Product

mock = {
    'id': '654',
    'company_name': 'Empresa SA',
    'product_name': 'produto da empresa',
    'manufacturing_date': '2023-01-30',
    'expiration_date': '2024-01-30',
    'serial_number': '123456789',
    'storage_instructions': 'keep it away from heat',
}


def test_product_report() -> None:
    new_prod = Product(
        mock['id'],
        mock['product_name'],
        mock['company_name'],
        mock['manufacturing_date'],
        mock['expiration_date'],
        mock['serial_number'],
        mock['storage_instructions']
    )

    right_message = (
        f"The product {mock['id']} - {mock['product_name']} "
        f"with serial number {mock['serial_number']} "
        f"manufactured on {mock['manufacturing_date']} "
        f"by the company {mock['company_name']} "
        f"valid until {mock['expiration_date']} "
        f"must be stored according to the following instructions: "
        f"{mock['storage_instructions']}."
    )

    assert right_message == str(new_prod)
