# Example list
numbers = [45, 12, 78, 34, 89, 23]

# Assume first number is largest initially
largest = numbers[0]

# Loop through the list
for num in numbers:
    if num > largest:
        largest = num

print(f"The largest number is: {largest}")
