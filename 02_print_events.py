import streamlit as st

# Set the title of the app
st.title("Event Printer")

# Create a form for user input
with st.form("event_form"):
    event_name = st.text_input("Event Name:")
    event_date = st.date_input("Event Date:")
    event_description = st.text_area("Event Description:")
    submit_button = st.form_submit_button("Add Event")

# Initialize session state to store events
if 'events' not in st.session_state:
    st.session_state.events = []

# Add event to the list if the form is submitted
if submit_button:
    event = {
        "name": event_name,
        "date": event_date,
        "description": event_description
    }
    st.session_state.events.append(event)
    st.success("Event added!")

# Display the list of events
if st.session_state.events:
    st.write("### List of Events:")
    for event in st.session_state.events:
        st.write(f"**Name:** {event['name']}")
        st.write(f"**Date:** {event['date']}")
        st.write(f"**Description:** {event['description']}")
        st.write("---")
