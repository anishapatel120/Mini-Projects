# Define a function to calculate the total bill amount
def calculate_total_bill(items):
    total_bill = 0
    for item in items:
        total_bill += item['price'] * item['quantity']
    return total_bill

# Define a function to generate and print the bill
def generate_bill(items, total_bill):
    print("\nBill Details:")
    print("------------------------------")
    for item in items:
        print(f"Item: {item['name']}, Price: {item['price']}, Quantity: {item['quantity']}, Total: {item['price'] * item['quantity']}")
    print("------------------------------")
    print(f"Total Bill Amount: {total_bill}")
    print("------------------------------")

# Define the main function to run the billing management system
def main():
    items = []

    # Input items and quantities
    while True:
        name = input("Enter item name (or 'done' to finish): ")
        if name.lower() == 'done':
            break
        price = float(input("Enter item price: "))
        quantity = int(input("Enter item quantity: "))
        item = {'name': name, 'price': price, 'quantity': quantity}
        items.append(item)

    # Calculate total bill
    total_bill = calculate_total_bill(items)

    # Generate and print the bill
    generate_bill(items, total_bill)

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
