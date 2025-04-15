import streamlit as st
import random

# Set the title of the app
st.title("Guess My Number")

# Generate a random number between 1 and 100
number_to_guess = random.randint(1, 100)

# Create a session state to store the number of attempts
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0

# Input for the user's guess
user_guess = st.number_input("Enter your guess (1-100):", min_value=1, max_value=100)

# Button to submit the guess
if st.button("Submit Guess"):
    st.session_state.attempts += 1
    if user_guess < number_to_guess:
        st.write("Your guess is too low!")
    elif user_guess > number_to_guess:
        st.write("Your guess is too high!")
    else:
        st.write(f"Congratulations! You've guessed the number {number_to_guess} in {st.session_state.attempts} attempts!")
        # Reset the game
        st.session_state.attempts = 0
        number_to_guess = random.randint(1, 100)  # Generate a new number
