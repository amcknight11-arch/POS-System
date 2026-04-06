# POS SYSTEM FOR BEST BUY RETAIL STORE
# I CERTIFY THAT I HAVE NOT GIVEN OR RECEIVED ANY UNAUTHORIZED ASSISTANCE ON THIS ASSIGNMENT
# Aaliyah McKnight
# A.McKnight
# Course Code: ITT103

"""
This dictionary stores all available products sold by Best Buy Retail.
Each product has a price stored in its own dictionary along with stock(quantity).
"""
# PRODUCT CATALOG
products = {
    "Shrimp": {"Price": 2010.00, "Stock": 16},
    "Fish": {"Price": 1662.00, "Stock": 14},
    "Rice": {"Price": 871.00, "Stock": 18},
    "Flour": {"Price": 693.00, "Stock": 15},
    "Biscuit": {"Price": 135.00, "Stock": 20},
    "Crackers": {"Price": 117.00, "Stock": 23},
    "Cornflakes": {"Price": 751.00, "Stock": 21},
    "Fish Seasoning": {"Price": 698.00, "Stock": 24},
    "Jerk Seasoning": {"Price": 812.00, "Stock": 22},
    "Tru Juice": {"Price": 1369.00, "Stock": 17},
    "Tropicana": {"Price": 426.00, "Stock": 19},
    "Cranberry Juice": {"Price": 1246.00, "Stock": 12},
    "Water": {"Price": 105.00, "Stock": 32},
    "Dawn Dish Liquid": {"Price": 281.00, "Stock": 8},
    "Napkins": {"Price": 124.00, "Stock": 15},
    "Ariel": {"Price": 379.00, "Stock": 11},
    "Fabuloso": {"Price": 569.00, "Stock": 12},
    "Scott Tissue": {"Price": 110.00, "Stock": 13}
}

cart = {}

"""
WELCOME HEADER
It welcomes the user once the program is opened for the first time
"""
print("\n   WELCOME TO BEST BUY RETAIL STORE!")

"""
This is the DISPLAY PRODUCTS FUNCTION
It displays all available products with their prices and stock availability
"""
def display_products():
    print("\n  ======== Available Merchandise ========")

# This loops through every product in the product catalog and prints their details
    for goods, value in products.items():
        print(f"{goods.upper():<20} - Price: ${value['Price']:<8.2f} | Stock: {value['Stock']}")


"""
This is the ADD TO CART FUNCTION
It allows users to add items to the cart. It validates stock availability
before adding them to the cart.
It also includes: 
input validation, displays the available products, stock updates,
out of stock notice, low stock warning, and the option 
to add another item to the cart without going back to the main menu.
"""
def add_to_cart():
    while True:
    # Shows available products for a smoother add to cart experience
        display_products()
        print("---------------------------------------------------")
        
    # Asks for product name
        items = input("\nEnter Product Name: ").strip().title()

    # Checks if the product is available
        if items in products:
            try:
            # Asks user to enter their desired quantity
                quantity = int(input("Enter Quantity: "))
                
            # Validates if the quantity the user entered is available
                if quantity <= 0:
                    print("\nInvalid Quantity!")
                    continue
             # If the product is sold out during the session, it will print out of stock
                if products[items]["Stock"] == 0:
                    print(f"\n{items.upper()} - Out of Stock!")
                    continue

            # Checks if enough stock is available
                elif quantity <= products[items]["Stock"]:
                    
                # This adds the selected item to the cart or updates the quantity
                    cart[items] = cart.get(items, 0) + quantity
                # Reduces the stock in inventory
                    products[items]["Stock"] -= quantity
                    print(f"\n{quantity} x {items} added to cart successfully.")
                else:
                # If the user enters more stock than what's available
                    print("\nExceeds Available Quantity!")
                    continue

            # Implementing Low Stock Alert - If Product Quantity Falls Below 5
                if products[items]["Stock"] < 5:
                    print(f"\n⚠️LOW STOCK ALERT⚠️: {items.upper()} has only {products[items]['Stock']} left in stock.")

            # This asks the user if they want to add another item without going back to the main menu
                if input("\nDo you wish to add another item? (YES/NO): ").lower() != 'yes':
                    return
            except ValueError:
                print("\nInvalid Input!")
        else:
        # This handles if the user enters a name that's not in the product catalog
            print("\nProduct Not Found!")


"""
This is the REMOVE FROM CART FUNCTION
It allows users to remove items or quantities from the cart
It updates the product catalog immediately after confirmation
"""
def remove_from_cart():
# This is a confirmation if the cart is empty
    if not cart:
        print("\n   Cart is Empty!")
        return
        
# This displays items that are currently in the cart for users to choose what to remove
    view_cart
    
# Input asking for product name
    items = input("\nEnter Product Name to Remove: ").strip().title()

# Validating if an item exist in the cart
    if items not in cart:
        print("\nInvalid! Item Not Found!")
        return

    while True:
        try:
            quantity_to_remove = int(input("Enter Amount to Remove: "))
            
        # Validates the available quantity
            if quantity_to_remove <= 0:
                print("\n Invalid Quantity!")
                print()
                continue
            elif quantity_to_remove > cart[items]:
                print("\n Invalid Quantity! Exceeds Quantity in Cart!")
                print()
                continue
                
        # If the user is removing all the available quantity in the cart
            if quantity_to_remove == cart[items]:
                removed_quantity = cart[items]
                
            # This returns the removed quantity to inventory
                products[items]["Stock"] += removed_quantity
        
            # This removes the item completely from the cart
                del cart[items]
                print(f"\n{removed_quantity} x {items} removed from cart successfully.")
                break
            else:
            # This is a partial removal; only the entered quantity will be removed
                cart[items] -= quantity_to_remove
                
            # Inventory updates immediately after
                products[items]["Stock"] += quantity_to_remove
                
                print(f"\n{quantity_to_remove} x {items} removed from cart successfully.")
                break
        except ValueError:
            print("\n Invalid Input!")


"""
This is the VIEW CART FUNCTION 
It allows users to view all items that were added to the cart
It displays the price per item, the quantity, and calculates the total price
"""
def view_cart():
# Display if there's nothing in the cart to view
    if not cart:
        print("\n------ Shopping Cart is Empty! ------")
        return

    total_price = 0

    print("\n=========== SHOPPING CART ==========")
    print()
    
# Loop through the cart items
    for items, quantity in cart.items():
        price = products[items]["Price"]
        
    # How to get the subtotal calculation
        subtotal = quantity * price

        print(f"{items.upper():<16} {quantity} @ ${price:<8,.2f} = ${subtotal:,.2f}")
        
    # Total of every item in cart
        total_price += subtotal

    print("----------------------------------------------")
    print(f"Cart Total:                     ${total_price:,.2f}")

"""
This is the CHECKOUT FUNCTION
It displays the cart summary, shows the total calculation,
discount (12% if > 7000), tax at 10%, and it processes all payments
"""
def checkout():
# Display if there's nothing in the cart to check out
    if not cart:
        print()
        print("\n------ Shopping Cart is Empty! Nothing to Checkout. ------")
        return

# Calculating the subtotal for all items in cart
    subtotal = sum(products[items]["Price"] * quantity for items, quantity in cart.items())

# Apply discount if eligible - 12% Discount if Cart Total is > 7000
    discount = 0
    if subtotal > 7000:
        discount = subtotal * 0.12

    discounted_subtotal = subtotal - discount

# Calculating the 10% Tax
    tax = discounted_subtotal * 0.10
    
# Final total, inclusive of tax and discount
    total = discounted_subtotal + tax

# Checkout Display
    print("\n          CHECKOUT")
    print(f"\nSubtotal:            ${subtotal:<5,.2f}")
# This validates that the discount will only be shown when it meets the threshold
    if discount > 0:
        print(f"Discount:           -${discount:<5,.2f}")
    print(f"Tax:                 ${tax:<5,.2f}")
    print("-------------------------------------")
    print(f"Grand Total:           ${total:<5,.2f}")
    print("-------------------------------------")

# Validating Payments with commas

    while True:
        try:
            payments = float(input("Enter Amount Received: $").replace(",", "").strip())
            if payments < total:
                print("\nInsufficient Funds! Please Try Again.")
                print()
            else:
                change = payments - total

            # Generating Receipt
                generate_receipt(subtotal, discount, tax, total, payments, change)

            # This clears the cart after payment is successful
                cart.clear()
                break
        except ValueError:
            print("\nInvalid Input!")
            

"""
This is the RECEIPT FUNCTION
It prints a formatted receipt that includes: header, store name,
date and time, items purchased, and all totals
"""
def generate_receipt(subtotal, discount, tax, total, payments, change):

# The Header
    print("\n                 RECEIPT")
    print("\n           BEST BUY RETAIL STORE ")

# Gets current date and time
    from datetime import datetime
    now = datetime.now()
    print(f"            {now:%Y-%m-%d %H:%M:%S}")
    print("============================================")

# Displays all the items purchased on the receipt
    for items, quantity in cart.items():
        price = products[items]["Price"]
        print(f"{items.upper():<18} {quantity} @ ${price:<8,.2f} = ${quantity * price:,.2f}")

# Details that Will Print on Receipt
    print("============================================")
    print(f"Subtotal:                         ${subtotal:<8,.2f}")
    if discount > 0:
        print(f"Discount:                        -${discount:<8,.2f}")
    print(f"Tax:                              ${tax:<8,.2f}")
    print("---------------------------------------------")
    print(f"Grand Total:                      ${total:<8,.2f}")
    print("---------------------------------------------")
    print(f"Amount Paid:                      ${payments:<8,.2f}")
    print(f"Change:                            ${change:,.2f}")
    print("\n         Thank You for Shopping!")
    print("             Come Back Soon!\n")


"""
This is the MAIN PROGRAM FUNCTION, it's the main loop
It has the main menu system, which allows users to 
select different actions repeatedly
"""
def main():
    while True:
        try:
        # Displays the main menu
            print("\n===== POS SYSTEM =====")
            print("1. View Products")
            print("2. Add to Cart")
            print("3. Remove from Cart")
            print("4. View Cart")
            print("5. Checkout")
            print("0. Exit")

            print()

        # Prompts user to choose number selection
            selection = int(input("Enter your selection: "))

            if selection == 1:
                display_products()
            elif selection == 2:
                add_to_cart()
            elif selection == 3:
                remove_from_cart()
            elif selection == 4:
                view_cart()
            elif selection == 5:
                checkout()
            elif selection == 0:
                print("Exiting System. Thank You for Coming!")
                break
            else:
                print("Invalid Selection!")
        except ValueError:
            print("Invalid Input! Please select a number that matches your desired section.")



# Run Program
main()

# I CERTIFY THAT I HAVE NOT GIVEN OR RECEIVED ANY UNAUTHORIZED ASSISTANCE ON THIS ASSIGNMENT
# Aaliyah McKnight
# A.McKnight
# March 29, 2026


