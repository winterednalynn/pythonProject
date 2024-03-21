#Edna Lynn L.
#Computer Programming V
#Final Project

from decimal import Decimal # placing decimal as an accessible module

items = []  # List to store purchased items for each transaction
prices = []  # List to store prices for each transaction
transactions = []  # List to store complete transactions

while True: # Using Infinity Loop to keep the purchases going until a condition is met
    print("\nEnter items to buy (type 'done' when finished):") # Displaying Enter Item Name
#NESTED LOOP
    while True: # Infinite loop to continue requesting user's input for item and price
        item = input().lower()  # Get item name, convert to lowercase for case-insensitive search
        if item == "done":
            break ## Break out , when DONE is prompt

        price = Decimal(input(f"Enter price of '{item}': $")) #
        print("\nEnter another item to buy (type 'done' when finished):")

    # Append method basically add elements to our array , targeting item & price array
        items.append(item)
        prices.append(price)

    total_price = sum(prices)  # SUMS UP TOTAL PRICE

    # THIS IS TO SAVE TRANSACTION IN THE COLLECTION
    transactions.append({"items": items.copy(), "prices": prices.copy(), "total_price": total_price})

    # CLEAR ITEMS , CLEAR PRICES for NEXT PURCHASE
    items.clear()
    prices.clear()

    print("\nItems in your cart:")
    for item, price in zip(items, prices):  # Efficiently iterate together using zip
        print(f"- {item}: ${price}")

    print(f"\nYour total is: ${total_price}")

    # Payment processing logic (replace with payment gateway integration)
    print("Please pay for your items.")
    input("Press Enter to continue...")  # Wait for user acknowledgment

    another_purchase = input("Would you like to make another purchase? (yes/no): ").lower()
    if another_purchase != "yes":
        print("Thank you for shopping with us!")
        break

# USING LINEAR SEARCH STRUCTURE TO LOCATE KEYWORD W/IN DESIRE TRANSACTION
search_term = input("\nSearch for a transaction with item purchase or view first transaction ever (enter item name or "
                    "type 'first transaction'): ").lower()


if not search_term: # Checking to see if the user entered the said search term
    search_term = "first transaction" # The search term auto generates the first transaction if a keyword is not prompt

found_transaction = False # serves as a flag to track weather a transaction is matching or not
for transaction in transactions: # This loop iterates over each transaction in the transaction array
    if search_term == "first transaction" or any(item.lower() == search_term for item in transaction["items"]):
        # this condition checks for 2 possible matches the search term aka first transaction or just keywords in gen.
        print("\nTransaction details:") # Display print
        for item, price in zip(transaction["items"], transaction["prices"]):
            # iterates through items and prices together, displaying each item and it's cost
            print(f"- {item}: ${price}") # format
        print(f"Total: ${transaction['total_price']}") #display total price of that particular search transaction
        found_transaction = True # set to target to indicate a match has been located
        break # Exits the loop , stopping iterations.

if not found_transaction: # Similar to C# if (! condition)
    print("No transaction found for a specific item search term.")