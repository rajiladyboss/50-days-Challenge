import streamlit as st
import math

# Area functions
def area_circle(radius):
    return math.pi * radius ** 2

def area_rectangle(length, width):
    return length * width

def area_triangle(base, height):
    return 0.5 * base * height

# Streamlit App UI
st.title("📐 Area Calculator")

shape = st.selectbox("Choose a shape to calculate area:", ["Circle", "Rectangle", "Triangle"])

if shape == "Circle":
    radius = st.number_input("Enter radius (cm):", min_value=0.0, format="%.2f")
    if st.button("Calculate Area"):
        result = area_circle(radius)
        st.success(f"Area of Circle: {result:.2f} cm²")

elif shape == "Rectangle":
    length = st.number_input("Enter length (cm):", min_value=0.0, format="%.2f")
    width = st.number_input("Enter width (cm):", min_value=0.0, format="%.2f")
    if st.button("Calculate Area"):
        result = area_rectangle(length, width)
        st.success(f"Area of Rectangle: {result:.2f} cm²")

elif shape == "Triangle":
    base = st.number_input("Enter base (cm):", min_value=0.0, format="%.2f")
    height = st.number_input("Enter height (cm):", min_value=0.0, format="%.2f")
    if st.button("Calculate Area"):
        result = area_triangle(base, height)
        st.success(f"Area of Triangle: {result:.2f} cm²")
