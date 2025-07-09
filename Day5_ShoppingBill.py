# Function to calculate total cost with tax
def calculate_total_with_tax(item1, item2, item3, tax_percent):
    subtotal = item1 + item2 + item3
    tax_amount = subtotal * (tax_percent / 100)
    total = subtotal + tax_amount
    return total

# Get input from user
item1 = float(input("Enter price of item 1: "))
item2 = float(input("Enter price of item 2: "))
item3 = float(input("Enter price of item 3: "))
tax_percent = float(input("Enter tax percentage (%): "))

# Calculate and display result
total_cost = calculate_total_with_tax(item1, item2, item3, tax_percent)
print(f"\nTotal cost including {tax_percent}% tax: ₹{total_cost:.2f}")
