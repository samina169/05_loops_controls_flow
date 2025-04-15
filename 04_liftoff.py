import streamlit as st
import time

# Set the title of the app
st.title("Rocket Liftoff Countdown")

# Function to perform the countdown
def countdown(t):
    for i in range(t, 0, -1):
        st.write(f"T-minus {i} seconds")
        time.sleep(1)  # Wait for 1 second
    st.write("Liftoff!")

# Button to start the countdown
if st.button("Start Countdown"):
    countdown(10)  # Countdown from 10 seconds
