import streamlit as st

# Set the title of the app
st.title("Fibonacci Sequence Generator")

# Input for the user to specify how many Fibonacci numbers to generate
num_terms = st.number_input("Enter the number of terms in the Fibonacci sequence:", min_value=1)

# Function to generate Fibonacci sequence
def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Generate and display the Fibonacci sequence when the button is clicked
if st.button("Generate Fibonacci Sequence"):
    fib_sequence = fibonacci(num_terms)
    st.write(f"The first {num_terms} terms of the Fibonacci sequence are: {fib_sequence}")
