import streamlit as st
import math

# --- App Title ---
st.title("🧮 Math Calculation Utility App")
st.markdown("Perform basic math operations like add, subtract, divide, multiply, percentage, and more.")

# --- Input Fields ---
st.header("🔢 Enter Numbers")

num1 = st.number_input("Enter the first number:", value=0.0, format="%.2f")
num2 = st.number_input("Enter the second number (if required):", value=0.0, format="%.2f")

# --- Operation Selection ---
st.header("⚙️ Choose Operation")

operation = st.selectbox("Select an operation:", [
    "Addition (+)",
    "Subtraction (-)",
    "Multiplication (×)",
    "Division (÷)",
    "Percentage (%)",
    "Power (xʸ)",
    "Square Root (√)"
])

# --- Calculation ---
st.header("🧾 Result")

if operation == "Addition (+)":
    result = num1 + num2
    st.success(f"{num1} + {num2} = {result}")

elif operation == "Subtraction (-)":
    result = num1 - num2
    st.success(f"{num1} - {num2} = {result}")

elif operation == "Multiplication (×)":
    result = num1 * num2
    st.success(f"{num1} × {num2} = {result}")

elif operation == "Division (÷)":
    if num2 == 0:
        st.error("❌ Cannot divide by zero!")
    else:
        result = num1 / num2
        st.success(f"{num1} ÷ {num2} = {result}")

elif operation == "Percentage (%)":
    result = (num1 / 100) * num2
    st.success(f"{num1}% of {num2} = {result}")

elif operation == "Power (xʸ)":
    result = math.pow(num1, num2)
    st.success(f"{num1} raised to the power of {num2} = {result}")

elif operation == "Square Root (√)":
    if num1 < 0:
        st.error("❌ Cannot find the square root of a negative number.")
    else:
        result = math.sqrt(num1)
        st.success(f"√{num1} = {result}")
