# Function to check password validity
def is_valid_password(password, min_length):
    if len(password) >= min_length:
        return True
    else:
        return False

# Input from user
password = input("Enter your password: ")
min_length = 8  # You can change the required length

# Check and print result
if is_valid_password(password, min_length):
    print("✅ Password is valid.")
else:
    print(f"❌ Password is too short. Minimum length should be {min_length} characters.")
