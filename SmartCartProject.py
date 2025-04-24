# SmartCart Pro - Modular E-Commerce System
# This program simulates an e-commerce shopping cart system with various features.
# It includes product catalog management, cart operations, checkout process,
# order history tracking, sales analytics, and string utilities.


# ------------------- STEP 1: Product Catalog -------------------
# defines functiona and takes argument catalog
def displayCatalog(catalog):
    print("Product Catalog:")
    for productName, price in catalog: # iterates through the catalog
        # displays the product name and price
        # formatted to 2 decimal places
        print(f"- {productName}: ${price:.2f}")

# This function retrieves the price of a product from the catalog.
# It takes the catalog and product name as arguments.
def getProductPrice(catalog, productName):
    for name, price in catalog: # iterates through the catalog
        # checks if the product name matches
        if name == productName:
            return price # returns the price if found
    # returns None if the product is not found
    return None

# ------------------- STEP 2: Cart Operations -------------------
# This function checks if the requested quantity of a product is available in stock.
# It takes the stock, product name, and quantity as arguments.
def checkStock(stock, product, qty):
    if product in stock: # checks if the product is in stock
        if stock[product] >= qty: # checks if the requested quantity is available
            return True # returns True if available
    return False # returns False if not available

# This function adds a product to the cart if it is in stock.
# It takes the cart, stock, product name, and quantity as arguments.
def addToCart(cart, stock, product, qty): 
    if checkStock(stock, product, qty): # checks if the product is in stock
        cart.append({"product": product, "quantity": qty}) # adds the product to the cart
        stock[product] -= qty # updates the stock
        print(f"Added {qty} x {product} to cart.") # confirms addition
    else:
        print("Not enough stock or product not found.")

# This function removes a product from the cart.
# It takes the cart and product name as arguments.
def removeFromCart(cart, product):
    for item in cart:
        if item["product"] == product: # checks if the product is in the cart
            cart.remove(item) # removes the product from the cart
            print(f"Removed {product} from cart.") # confirms removal
            break

# This function updates the quantity of a product in the cart.
def viewCart(cart):
    if not cart:
        print("Your cart is empty.") # checks if the cart is empty
    else:
        print("Current cart:") # displays the cart
        for item in cart:
            print(f"- {item["product"]}: {item["quantity"]}") # displays the product and quantity

# ------------------- STEP 3: Checkout -------------------
# This function calculates the total price of items in the cart.
# It takes the cart and catalog as arguments.
def calculateTotal(cart, catalog):
    total = 0 # initializes total to 0
    for item in cart:
        product = item["product"] # gets the product name
        # gets the quantity of the product
        qty = item["quantity"]
        for name, price in catalog: # iterates through the catalog
            # checks if the product name matches
            if name == product:
                total += price * qty # calculates the total price
    return total

# This function applies discounts based on the total price.
# It takes the total price as an argument.
def applyDiscounts(total):
    if total > 200: # applies 10% discount for orders over $200
        return total * 0.90  # 10% off
    elif total > 100: # applies 5% discount for orders over $100
        return total * 0.95  # 5% off
    else:
        return total

# This function applies tax to the total price.
# It takes the total price as an argument.
def applyTax(total):
    return total * 1.08  # 8% tax added to total

# This function generates a receipt for the items in the cart.
# It takes the cart and catalog as arguments.
def generateReceipt(cart, catalog):
    print("\n--- RECEIPT ---")
    for item in cart:
        product = item["product"] # gets the product name
        # gets the quantity of the product
        qty = item["quantity"]
        price = getProductPrice(catalog, product) # gets the price of the product
        print(f"{product} x{qty} = ${price * qty:.2f}") # displays the product, quantity, and total price
    subtotal = calculateTotal(cart, catalog) # calculates the subtotal
    discounted = applyDiscounts(subtotal) # applies discounts
    finalTotal = applyTax(discounted) # applies tax
    print(f"Subtotal: ${subtotal:.2f}") # displays the subtotal
    print(f"After Discount: ${discounted:.2f}") # displays the discounted total
    print(f"Final Total (with Tax): ${finalTotal:.2f}") # displays the final total

# ------------------- STEP 4: Recommendation (Recursive) -------------------
# This function recommends a product based on the user's cart.
# It takes the catalog, cart, and index as arguments.
def recommendProduct(catalog, cart, index=0):  # checks if the index is provided
    if index >= len(catalog): # checks if the index is out of range
        return "No recommendation available."
    product = catalog[index][0] # gets the product name
    for item in cart:
        if item["product"] == product: # checks if the product is in the cart
            return recommendProduct(catalog, cart, index + 1) # recursively calls the function with the next index
    return product

# ------------------- STEP 5: Order History -------------------
# This function updates the order history with the current cart.
# It takes the order history and cart as arguments.
def updateOrderHistory(orderHistory, cart):
    order = tuple((item["product"], item["quantity"]) for item in cart) # creates a tuple of the cart items
    orderHistory.append(order) # adds the order to the history

# This function summarizes the order history.
# It takes the order history as an argument.
def summarizeOrders(orderHistory):
    print("\n--- Order History ---")
    for i, order in enumerate(orderHistory, start=1): # iterates through the order history
        print(f"Order {i}:") # displays the order number
        for product, qty in order: # iterates through the order items
            print(f"  {product} x{qty}") # displays the product and quantity

# ------------------- STEP 6: Sales Analytics -------------------
# This function retrieves the top-selling products from the sales data.
def getTopProducts(salesData): 
    print("\n--- Top Selling Products ---")
    sortedProducts = sorted(salesData.items(), key=lambda x: x[1], reverse=True) # sorts the products by sales count
    for product, count in sortedProducts[:3]: # gets the top 3 products
        print(f"{product}: {count} sold") # displays the product and sales count

# ------------------- STEP 7: String Utilities -------------------
# This function checks if a string is a palindrome.
def stringMatchScore(str1, str2):
    score = 0 # initializes score to 0
    for i in range(min(len(str1), len(str2))): # iterates through the strings
        # checks if the characters at the same index match
        if str1[i] == str2[i]:
            score += 1 # increments score if they match
    return score

# ------------------- Main Function -------------------
# This function runs the main program loop.
# It initializes the catalog, stock, cart, order history, and sales data.
# It displays the menu and handles user input.
def main():
    catalog = [("Avocado", 1.99), ("Banana", 0.99), ("Orange", 1.29)]
    stock = {"Avocado": 10, "Banana": 15, "Orange": 12}
    cart = []
    orderHistory = []
    salesData = {"Avocado": 0, "Banana": 0, "Orange": 0}

    while True:
        print("\nSmartCart Menu:")
        print("1. View Catalog")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Checkout")
        print("5. Recommend a Product")
        print("6. View Order History")
        print("7. View Top Products")
        print("8. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            displayCatalog(catalog)
        elif choice == "2":
            product = input("Enter product name: ")
            qty = int(input("Enter quantity: "))
            addToCart(cart, stock, product, qty)
            if product in salesData:
                salesData[product] += qty
        elif choice == "3":
            viewCart(cart)
        elif choice == "4":
            generateReceipt(cart, catalog)
            updateOrderHistory(orderHistory, cart)
            cart.clear()
        elif choice == "5":
            suggestion = recommendProduct(catalog, cart)
            print(f"We recommend you try: {suggestion}")
        elif choice == "6":
            summarizeOrders(orderHistory)
        elif choice == "7":
            getTopProducts(salesData)
        elif choice == "8":
            print("Thank you for shopping!")
            break
        else:
            print("Invalid option. Try again.")

# Run the main function
if __name__ == "__main__":
    main()
