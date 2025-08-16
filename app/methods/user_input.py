import streamlit as st

def get_user_input():
    """Collect user input for a donor."""
    name = st.text_input("Enter your name")
    email = st.text_input("Enter your email")
    amount = st.number_input("Donation amount", min_value=0.0, format="%.2f")


def validate_donation(donation):
    """Check that donation has valid name, email, and amount."""
    if not donation["name"] or not donation["email"]:
        return False
    if donation["amount"] <= 0:
        return False
    return True


    if st.button("Submit"):
        return {"name": name, "email": email, "amount": amount}
    return None
