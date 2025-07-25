import streamlit as st

def format_phone_number(number):
    num_str = str(number).strip()

    if len(num_str) != 10 or not num_str.isdigit():
        return "❌ Invalid phone number. Please enter exactly 10 digits."
    
    formatted = f"({num_str[:3]}) {num_str[3:6]}-{num_str[6:]}"
    return formatted

# Streamlit App
st.title("📞 Phone Number Formatter")
st.write("Enter a 10-digit number to format it as (XXX) XXX-XXXX")

# Input field
phone_input = st.text_input("Enter 10-digit phone number:")

if phone_input:
    result = format_phone_number(phone_input)
    st.success(f"Formatted Number: {result}")
