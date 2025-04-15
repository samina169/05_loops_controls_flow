import streamlit as st
import random

# Set the title of the app
st.title("Wholesome Machine")

# List of wholesome quotes
quotes = [
    "You are enough just as you are.",
    "Believe in yourself and all that you are.",
    "You are capable of amazing things.",
    "Your only limit is your mind.",
    "Stay positive, work hard, make it happen.",
    "You are stronger than you think.",
    "Every day may not be good, but there is something good in every day.",
    "You are loved, you are valued, you are important."
]

# Button to get a random quote
if st.button("Get a Wholesome Quote"):
    quote = random.choice(quotes)
    st.write(f"**Wholesome Quote:** {quote}")
