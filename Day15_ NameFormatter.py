# Name Formatter Tool

def format_name(full_name):
    # Remove extra spaces and capitalize properly
    name_parts = full_name.strip().title().split()

    if len(name_parts) < 2:
        print("Please enter at least a first and last name.")
        return

    first_name = name_parts[0]
    last_name = name_parts[-1]
    initials = "".join([part[0].upper() for part in name_parts])

    print("\nDifferent Name Formats:")
    print(f"1. First Last: {first_name} {last_name}")
    print(f"2. Last, First: {last_name}, {first_name}")
    print(f"3. Initials: {initials}")
    print(f"4. Full Name (Title Case): {' '.join(name_parts)}")
    print(f"5. Last Name Only: {last_name}")
    print(f"6. First Name Only: {first_name}")


# Input from user
if __name__ == "__main__":
    full_name = input("Enter your full name: ")
    format_name(full_name)
