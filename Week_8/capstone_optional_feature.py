# Capstone Project for Python Programming 26-27

# Optional features to be added: Allow products to be deselected after being selected

# These items and pricing are from my company; Lighting Dynamics
# Available products

RED = "\033[31m"
BLUE = "\033[34m"
GREEN = "\033[32m"
BOLD = "\033[1m"
RESET = "\033[0m"

# Can replace these values with my contact information.
# Won't because repo is public
CONTACT_EMAIL = "your-email@example.com"
CONTACT_PHONE = "(555) 555-5555"

# added new more products
products = [
    {"id": 1, "name": "Cluster Lighting", "price": 220},
    {"id": 2, "name": "Cluster Rebuild", "price": 250},
    {"id": 3, "name": "Offroad Lighting", "price": 400},
    {"id": 4, "name": "Alternative Switch Lighting", "price": 150},
    {"id": 5, "name": "Roof Rack Lighting", "price": 300},
    {"id": 6, "name": "Custom Work", "price": 350},
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


def parse_product_ids(raw_text, valid_ids):
    """Return a set of valid product IDs or None if the input is invalid."""
    values = raw_text.replace(",", " ").split()
    if not values:
        return None

    ids = set()
    for value in values:
        if not value.isdigit():
            return None
        product_id = int(value)
        if product_id not in valid_ids:
            return None
        ids.add(product_id)

    return ids


def sync_selected_products(product_menu, selected_ids):
    """Keep each product's selected flag aligned with the selected IDs."""
    for product in product_menu:
        product["selected"] = product["id"] in selected_ids


def main():
    # Allows each item to be selected by a numbered menu choice
    product_menu = build_product_menu()
    valid_product_ids = {product["id"] for product in product_menu}
    selected_ids = set()

    while True:
        print("\nAvailable products:")
        for product in product_menu:
            status = "SELECTED" if product["selected"] else "AVAILABLE"
            print(
                f"{BLUE}{product['id']}. {product['name']} - ${product['price']} [{status}]{RESET}"
            )

        action = input(
            "Enter product numbers to select, 'deselect 2, 3' to remove them, or 'done' to finish: "
        ).strip()

        if not action or action.lower() == "done":
            break

        if action.lower().startswith("deselect"):
            raw_text = action[8:].strip()
            deselect_ids = parse_product_ids(raw_text, selected_ids)
            if deselect_ids is None:
                print(f"{RED}{BOLD}Please enter only numbers for currently selected products.{RESET}")
                continue
            selected_ids.difference_update(deselect_ids)
            sync_selected_products(product_menu, selected_ids)
            continue

        selected_ids_to_add = parse_product_ids(action, valid_product_ids)
        if selected_ids_to_add is None:
            print(f"{RED}{BOLD}No valid products selected. Please try again.{RESET}")
            continue

        selected_ids.update(selected_ids_to_add)
        sync_selected_products(product_menu, selected_ids)

    selected_products = [product for product in product_menu if product["selected"]]

    print("\nSelected products:")
    if selected_products:
        for product in selected_products:
            print(f"{BLUE}{product['name']} - ${product['price']}{RESET}")
        if any(product["id"] == 6 for product in selected_products):
            print(f"Contact me: {CONTACT_EMAIL} | {CONTACT_PHONE}")
    else:
        print("No valid products selected.")

    total = sum(product["price"] for product in selected_products)
    print(f"{GREEN}Total: ${total}{RESET}")


if __name__ == "__main__":
    main()  

