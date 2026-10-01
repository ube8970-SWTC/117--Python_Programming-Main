# Capstone Project for Python Programming 26-27

# Optional features to be added: Allow products to be deselected after being selected

# These items and pricing are from my company; Lighting Dynamics
# Available products

products = [
    {"id": 1, "name": "Cluster Lighting", "price": 220},
    {"id": 2, "name": "Cluster Rebuild", "price": 250},
    {"id": 3, "name": "Offroad Lighting", "price": 400},
    {"id": 4, "name": "Alternative Switch Lighting", "price": 150},
]


def build_product_menu():
    """Create a menu list with a selected flag for each product."""
    return [
        {
            "id": product["id"],
            "name": product["name"],
            "price": product["price"],
            "selected": False,
        }
        for product in products
    ]


def main():
    # Allow each item to be selected by a numbered menu choice
    product_menu = build_product_menu()

    # Display the list with selectable IDs
    for product in product_menu:
        print(f"{product['id']}. {product['name']} - ${product['price']}")

    valid_product_ids = {product["id"] for product in product_menu}
    selected_ids = set()
    while not selected_ids:
        selected_ids_input = input(
            "Enter product numbers to select, separated by commas (for example: 1, 2, 3, 4): "
        )

        # Accept comma-separated numbers, spaces, or a mix such as "1, 2, 3, 4".
        values = selected_ids_input.replace(",", " ").split()
        entered_ids = set()
        valid_input = bool(values)
        for value in values:
            if not value.isdigit() or int(value) not in valid_product_ids:
                valid_input = False
                break
            entered_ids.add(int(value))

        if valid_input:
            selected_ids = entered_ids
        else:
            print("No valid products selected. Please try again.")

    for product in product_menu:
        product["selected"] = product["id"] in selected_ids

    while True:
        print("\nCurrent selection:")
        for product in product_menu:
            if product["selected"]:
                print(f"{product['id']}. {product['name']} - ${product['price']}")

        deselect_input = input(
            "Enter product numbers to deselect, separated by commas, or press Enter to continue: "
        ).strip()
        if not deselect_input:
            break

        values = deselect_input.replace(",", " ").split()
        deselect_ids = set()
        valid_input = bool(values)
        for value in values:
            if not value.isdigit() or int(value) not in selected_ids:
                valid_input = False
                break
            deselect_ids.add(int(value))

        if valid_input:
            selected_ids.difference_update(deselect_ids)
            for product in product_menu:
                product["selected"] = product["id"] in selected_ids
        else:
            print("Please enter only numbers for currently selected products.")

    selected_products = [product for product in product_menu if product["selected"]]

    print("\nSelected products:")
    if selected_products:
        for product in selected_products:
            print(f"{product['name']} - ${product['price']}")
    else:
        print("No valid products selected.")

    total = sum(product["price"] for product in selected_products)
    print(f"Total: ${total}")


if __name__ == "__main__":
    main()

