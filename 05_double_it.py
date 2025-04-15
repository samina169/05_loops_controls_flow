import streamlit as st

# Set the title of the app
st.title("Double It!")

# Input for the user to enter a number
user_input = st.number_input("Enter a number:", value=0)

# Button to double the number
if st.button("Double It!"):
    doubled_value = user_input * 2
    st.write(f"The doubled value is: {doubled_value}")
