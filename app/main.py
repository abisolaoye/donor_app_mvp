
import streamlit as st
from methods.storage import save_donation, load_donations
from methods.user_input import validate_donation
from methods.sentiment import analyze_message

# --- Page config ---
st.set_page_config(
    page_title="Donor App",
    page_icon="🏦",
    layout="wide"
)

# --- Custom Title Styling ---
st.markdown(
    """
    <style>
    .app-title {
        font-size: 40px !important;
        font-weight: 700;
        color: #2c3e50;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown('<h1 class="app-title">Cheerful Giving</h1>', unsafe_allow_html=True)
st.write("Welcome! Make a donation and help others. Your support matters!")

# --- Main Layout ---
col1, col2 = st.columns([1, 2])

# --- Donation Form ---
with col1:
    with st.form("donation_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        amount = st.number_input("Donation Amount ($)", min_value=1, step=1)
        message = st.text_area("Leave a message (optional)")
        submitted = st.form_submit_button("Donate")

        if submitted:
            donation = {
                "name": name,
                "email": email,
                "amount": amount,
                "message": message
            }

            if validate_donation(donation):
                save_donation(donation)

                # --- AI Sentiment Analysis ---
                sentiment = analyze_message(message)
                sentiment_label = sentiment['label'] if sentiment else "No message"

                st.success(f"Thank you {name} for donating ${amount}!")
                if sentiment_label != "No message":
                    st.info(f"💬 Your message sentiment: {sentiment_label}")
            else:
                st.error("⚠️ Please fill in all fields correctly.")

# --- Donation Records & Metrics ---
with col2:
    donations = load_donations()

    if not donations.empty:
         st.subheader("See recent donations (Last 5)")
    # Show only amount and message
         st.dataframe(donations.tail(5)[["amount", "message"]])
    else:
        st.info("No donations recorded yet. Be the first to donate!")
