import datetime
import streamlit as st
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# MongoDB Atlas connection details (replace with your actual credentials)
load_dotenv()

mongo_url=os.getenv("Mongo_url")
# MongoDB connection
client = MongoClient(f"mongodb+srv://{mongo_url}")
db = client["CampusGuard"]  # Replace with your database name
collection = db["neuralgo"]  # Replace with your collection name

# Feedback categories
feedback_categories = ["Cancellation", "Flight Reschedule", "Flight Refund Related", "Flight Delay Complaint", "Staff Behavior Complaint", "Miscellaneous"]

# Title and introduction
st.markdown("<h1 style='text-align: center; font-size: 3.5em;'>Customer Feedback</h1>", unsafe_allow_html=True)
st.markdown(
    """
    <div style="padding: 20px;">
        <p style="font-weight: bold;">We appreciate your feedback! Please take a moment to share your experience with us.</p>
        <p style="font-weight: bold;">Your feedback helps us improve our services. Thank you for your time!</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Feedback form
with st.form("feedback_form"):
    # Customer name
    customer_name = st.text_input("Your Name")

    # Customer rating
    call_rating = st.slider("Call Rating (1-5)", min_value=1, max_value=5)

    # Feedback category selection
    feedback_category = st.selectbox("Feedback Category", feedback_categories)

    # Feedback details
    feedback_details = st.text_area("Feedback Details")

    # Agent handled ID
    agent_id = st.text_input("Agent ID")

    # Complaint ID
    complaint_id = st.text_input("Complaint ID")

    # Submit button
    submit_button = st.form_submit_button("Submit Feedback")

# Handling form submission
if submit_button:
    # Insert feedback data into MongoDB collection
    feedback_data = {
        "customer_name": customer_name,
        "call_rating": call_rating,
        "feedback_category": feedback_category,
        "feedback_details": feedback_details,
        "agent_id": agent_id,
        "complaint_id": complaint_id,
        "timestamp": datetime.datetime.now()
    }
    collection.insert_one(feedback_data)

    st.success("Thank you for your feedback!")
