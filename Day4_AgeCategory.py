# Function to determine the age category
def get_age_category(age):
    if age < 0:
        return "Invalid age"
    elif age <= 12:
        return "Child"
    elif age <= 19:
        return "Teenager"
    elif age <= 59:
        return "Adult"
    else:
        return "Senior"

# Get user input
try:
    age = int(input("Enter your age: "))
    category = get_age_category(age)
    print(f"You are a {category}.")
except ValueError:
    print("Please enter a valid number.")
