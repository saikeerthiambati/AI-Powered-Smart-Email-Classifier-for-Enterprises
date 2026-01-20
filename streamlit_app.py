import streamlit as st
import pandas as pd
import re

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Powered Smart Email Classifier",
    page_icon="📧",
    layout="centered"
)

# -----------------------------
# Helper Functions
# -----------------------------
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"http\S+|www\S+", "", text)
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def detect_category(text):
    text = text.lower()

    if any(word in text for word in ["refund", "complaint", "issue", "not working", "problem"]):
        return "Complaint"
    elif any(word in text for word in ["request", "support", "help", "please"]):
        return "Request"
    elif any(word in text for word in ["offer", "win", "free", "click", "buy now"]):
        return "Spam"
    else:
        return "General"

def detect_urgency(text):
    text = text.lower()

    high_keywords = ["urgent", "asap", "immediately", "critical", "not working"]
    medium_keywords = ["soon", "priority", "follow up", "by tomorrow"]

    if any(word in text for word in high_keywords):
        return "High"
    elif any(word in text for word in medium_keywords):
        return "Medium"
    else:
        return "Low"

def detect_priority(category, urgency):
    if category == "Complaint" and urgency == "High":
        return "High"
    elif urgency == "Medium":
        return "Medium"
    else:
        return "Low"

# -----------------------------
# UI
# -----------------------------
st.markdown(
    """
    <h1 style='text-align:center; color:#4da3ff;'>📧 AI Powered Smart Email Classifier</h1>
    <p style='text-align:center; color:gray;'>
    Enterprise Email Categorization & Urgency Detection System
    </p>
    """,
    unsafe_allow_html=True
)

st.markdown("### ✉️ Enter Email Content")
email_text = st.text_area(
    "",
    placeholder="Paste the email content here...",
    height=180
)

# -----------------------------
# Prediction Button
# -----------------------------
if st.button("🚀 Classify Email", key="classify_btn"):
    if email_text.strip() == "":
        st.warning("Please enter email content.")
    else:
        cleaned = clean_text(email_text)

        category = detect_category(cleaned)
        urgency = detect_urgency(cleaned)
        priority = detect_priority(category, urgency)

        st.markdown("---")
        st.subheader("📊 Classification Result")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Category", category)

        with col2:
            st.metric("Urgency", urgency)

        with col3:
            st.metric("Priority", priority)

# -----------------------------
# Footer
# -----------------------------
st.markdown(
    """
    <hr>
    <p style='text-align:center; color:gray; font-size:13px;'>
    Built by Sai Keerthi • Infosys Springboard Project
    </p>
    """,
    unsafe_allow_html=True
)
