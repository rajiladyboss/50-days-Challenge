# Get input from the user
n = int(input("Enter a number: "))

# Initialize sum
total = 0

# Loop from 1 to n (inclusive)
for i in range(1, n + 1):
    total += i

# Print the result
print("Sum of numbers from 1 to", n, "is:", total)
