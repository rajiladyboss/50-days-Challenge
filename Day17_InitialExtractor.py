# Initial Extractor: Extract initials from a full name

def extract_initials(full_name):
    name_parts = full_name.strip().split()
    initials = ''.join([part[0].upper() for part in name_parts])
    print(f"Initials: {initials}")


if __name__ == "__main__":
    user_input = input("Enter your full name: ")
    extract_initials(user_input)
