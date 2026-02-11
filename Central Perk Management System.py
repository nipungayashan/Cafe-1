from typing import Dict, Any
import sys

menu = {
    "1": {"name": "Milk Tea", "price" :140},
    "2": {"name": "Coffee", "price"   :200},
    "3": {"name": "Sandwich", "price" :350},
    "4": {"name": "Pastry", "price"   :300},
    "5": {"name": "Juice", "price"    :250},
}


def login():
    print("--------LOGIN------------")
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if username == "admin" and password == "1234" :
        print("Login Sucessfull! \n")
        return True
    else:
        print("Login Failed! \n")
        return False

#----------Displays the Cafe menu---------------
def display_menu():
    """
    This Function shows the complete Cafe Menu to the customers.
    Prints all items in a neat table structure with code, name and price.
    :return: None
    """
    print("\n" +  "=" *  60)
    print("                     CENTRAL PERK MENU")
    print("=" * 60)
    print(f"{'Code': <15} {'Item': <25} {'Price(LKR)':<22}")
    print("-" * 60)

    #Loop through each menu item and displays them
    for code, item in menu.items():
        print(f"{code:<15} {item['name']:<25} LKR {item['price']:<22}")
    print("=" * 60)

def get_valid_int_input(prompt):
    """
    This function keeps asking user for a number until correct number is entered.
    It prevents program crash when user types letters instead of numbers.

    Args:
    prompt (str): The message shown to the user e.g.:("Enter Choice:")

    Returns:
        int: Number entered after validation.
    """
    while True:
        try:
            # Converting the user input to integer and return if successful
            return int(input(prompt).strip())
        except ValueError:
            # Handles non-integer values entered with error message
            print("Please Enter a Valid Number!")

def get_valid_menu_selection():
    """
    This function gets valid menu code from user when placing order.
    Shows error if wrong code entered.
    Returns:
        str: Menu code entered after validation or exit using 'done'.
    """
    while True:
        #Taking user input for order placement
        user_choice = input("Enter item code to place order (or 'done' to exit) ").strip()
        if user_choice.lower() == "done":
            return "done"
        if user_choice in menu:
            return user_choice
        print("Please Enter an valid menu item!")


def menu_sorting(sort_type):
    """
    This function sorts the menu and shows it in a sorted order.
    Sorting by price or name is done through this functon.
    Args:
    sort_type: 'name' to sort alphabetically or 'price' to sort by price.
    Returns:
        None
    """
    sort_items = list(menu.items())

    if sort_type == "name":
        sort_items.sort(key=lambda x: x[1]["name"])
        print("\nMenu sorted alphabetically: ")
    else:
        sort_items.sort(key=lambda x: x[1]["price"])
        print("\nMenu sorted by price(lowest to highest): ")

    # Display sorted menu
    print("\n" + "=" * 60)
    print("              Central Park Menu")
    print("="  *  60)
    print(f"{'Code' :<15} {'Item':<25} {'Price (LKR)':<22}")
    print("-" * 60)
    for code, item in sort_items:
        print(f"{code:<15} {item['name']:<25} LKR {item['price']:<22}")
    print("="  *  60 )

def search_item():
    """
    This function find items by typing part of item name.

    Returns:
        None:
    """
    search_item = input("\nEnter Item Name to Search: ").strip().lower()
    search_results = []

    for code, item in menu.items():
        if search_item in item["name"].lower():
            search_results.append((code, item))

    #Display
    if search_results:
        print(f"\n Found {len(search_results)} matching item: ")
        print("-"  * 50)
        for code, item in search_results:
            print(f"Code {code}: {item['name']} - LKR {item['price']:.2f}")
    else:
        print("No items found matching to your search. ")

def take_order():
    """
    This function lets user add multiple items with quantities

    Returns:
        dict: Order dictionary
    """
    order_items = {}
    display_menu()

    while True:
        item_code = get_valid_menu_selection()
        if item_code == "done":
            break

        qty = get_valid_int_input(f"Enter quantity for {menu[item_code]['name']}: ")
        if qty > 0:
            order_items[item_code] = {
                "quantity": qty,
                "price": menu[item_code]["price"]
            }
            print(f" Added {qty} x {menu[item_code]['name']}")
        else:
            print("Quantity must be greater than 0!")

    return order_items

def calculate_subtotal(order_items):
    """
    This function adds up total price before discount.

    Args:
        order_items: dictionary of ordered items

    Returns:
        float: total price
    """
    subtotal = 0.0
    for item_details in order_items.values():
        subtotal += item_details["quantity"] * item_details["price"]
    return subtotal

def calculate_discount(subtotal):
    """
    This function calculates and give 10% discount if subtotal is > LKR 2000.
    Returns:
        float: Discount amount
    """
    return subtotal * 0.10 if subtotal > 2000 else 0.0

def calculate_bill(order_items):
    """
    This function calculates complete bill with discount if applicable
    for the order.

    Args:
    order_items: Customer order details

    Returns:
        tuple: Three values (subtotal, discount, final_total)
    """
    subtotal = calculate_subtotal(order_items)
    discount = calculate_discount(subtotal)
    final_total = subtotal - discount
    return subtotal, discount, final_total

def generate_receipt(order_items,subtotal,discount,final_total):
    """
    This function creates a complete customer bill receipt showing all ordered
    items with quantities,unit prices, item totals, subtotal, discount (if applicable)
    and final payable amount.
    Args:
     order_items: Order details
     subtotal:Price before discount
    :param discount:
    :param final_total:
    :return:
    """
    print("\n "+ "=" * 70)
    print("                     Central Perk Receipt ")
    print("="  * 70)
    print(f"{'Item': <15} {'Qty': <5} {'Price': <8} {'Total': <10}")
    print("-" *70)

    for item_code, details in order_items.items():
        item_name = menu[item_code]["name"]
        qty = details["quantity"]
        price = details["price"]
        item_total = qty * price
        print(f"{item_name:<20} {qty:<5} {price: <10.2f} {item_total:<12,.2f}")

    print("-" *70)
    print(f"{'Subtotal':<35} LKR {subtotal:,.2f}")
    if discount > 0:
        print(f"{'Discount (10%)':<38}  -LKR {discount:,.2f}")
    print("-" * 70)
    print(f"{'Final Total:':<38}  LKR {final_total:,.2f}")
    print("=" * 70)
    print("Thank You for choosing Central Perk!")

def main():
    """
    Main entry point for the Central Perl Management System.
    Handles the login process and the main application loop.
    :return:
    """
    if not login():
        print("Unauthorized access.")
        return

    while True:
        print("\n" + "=" * 60)
        print("             CENTRAL PERK MANAGEMENT SYSTEM")
        print("1.View Menu")
        print("2.Sort Menu (Name/Price)")
        print("3.Search Menu Items")
        print("4.Place Order")
        print("5. Exit")
        print("=" * 60)

        try:
            choice = get_valid_int_input("Enter your choice (1-5): ")

            match choice:
                case 1:
                    display_menu()
                case 2:
                    sort_choice = get_valid_int_input("1=Name, 2=Price: ")
                    menu_sorting('name' if sort_choice == 1 else 'price')
                case 3:
                    search_item()
                case 4:
                    orders = take_order()
                    if orders:
                        subtotal, discount, final_total = calculate_bill(orders)
                        generate_receipt(orders, subtotal, discount, final_total)
                    else:
                        print("No Order Placed.")
                case 5:
                    print("Thank you for visiting Central Perk!")
                case _:
                    print("Invalid Choice! Choose from (1-5) only")

        except KeyboardInterrupt:
            print("\nThankyou for visiting Central Perk!")


if __name__ == "__main__":
    main()

