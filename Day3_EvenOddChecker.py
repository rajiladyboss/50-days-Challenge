# Function to check if a number is even or odd
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Check a single number
single_number = int(input("Enter a number to check if it's Even or Odd: "))
print(f"{single_number} is {check_even_odd(single_number)}")

# Check a list of numbers
number_list = [12, 5, 9, 0, 8, 7, 3, 14]  # You can change this list
print("\nChecking a list of numbers:")

for number in number_list:
    result = check_even_odd(number)
    print(f"{number} is {result}")
