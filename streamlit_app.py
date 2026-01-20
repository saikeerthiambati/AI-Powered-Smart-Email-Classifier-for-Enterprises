import streamlit as st
import sys

# Allow imports from src folder
sys.path.append("src")
from urgency_model import final_urgency


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="AI Powered Smart Email Classifier",
    page_icon="📧",
    layout="centered"
)


# --------------------------------------------------
# Custom CSS
# --------------------------------------------------
st.markdown("""
<style>
.block-container {
    padding-top: 0rem !important;
}

body {
    background-color: #0b0f19;
}

.app-container {
    background: linear-gradient(180deg, #0f172a, #020617);
    padding: 40px;
    border-radius: 18px;
    box-shadow: 0 0 30px rgba(0,0,0,0.6);
    max-width: 900px;
    margin: 20px auto;
}

.title {
    text-align: center;
    font-size: 34px;
    font-weight: 700;
    color: #60a5fa;
    margin-bottom: 6px;
}

.subtitle {
    text-align: center;
    font-size: 15px;
    color: #cbd5e1;
    margin-bottom: 35px;
}

.card {
    padding: 18px;
    border-radius: 12px;
    text-align: center;
    color: white;
    font-weight: 600;
    box-shadow: 0 6px 14px rgba(0,0,0,0.4);
}

.insight {
    background-color: #020617;
    border-left: 4px solid #60a5fa;
    padding: 16px;
    border-radius: 10px;
    color: #e5e7eb;
}
</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# UI Layout
# --------------------------------------------------
st.markdown("<div class='app-container'>", unsafe_allow_html=True)

st.markdown("<div class='title'>📧 AI Powered Smart Email Classifier</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Enterprise Email Categorization & Urgency Detection System</div>", unsafe_allow_html=True)

email = st.text_area(
    "✉️ Enter Email Content",
    height=160,
    placeholder="Paste the email content here...",
    key="email_input"
)

# --------------------------------------------------
# Button (ONLY ONE)
# --------------------------------------------------
clicked = st.button("🚀 Classify Email", key="classify_btn")

if clicked:
    if not email.strip():
        st.warning("⚠️ Please enter email content before classification.")
    else:
        text = email.lower()

        # Category logic
        if "refund" in text or "not working" in text or "complaint" in text:
            category = "Complaint"
        elif "request" in text or "please" in text:
            category = "Request"
        elif "offer" in text or "lottery" in text or "free" in text:
            category = "Spam"
        else:
            category = "General"

        urgency = final_urgency(email)

        st.markdown("### 📊 Classification Result")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown(
                f"<div class='card' style='background:#1e40af'>📂 Category<br><span style='font-size:20px'>{category}</span></div>",
                unsafe_allow_html=True
            )

        with col2:
            st.markdown(
                f"<div class='card' style='background:#be123c'>⚡ Urgency<br><span style='font-size:20px'>{urgency}</span></div>",
                unsafe_allow_html=True
            )

        with col3:
            st.markdown(
                f"<div class='card' style='background:#0f766e'>📏 Length<br><span style='font-size:20px'>{len(email)}</span></div>",
                unsafe_allow_html=True
            )

        st.markdown("### 📈 Email Statistics")
        st.write(f"**Total Words:** {len(email.split())}")

        st.markdown("### 🤖 AI Insight")
        st.markdown(
            f"""
            <div class='insight'>
            This email has been classified as <b>{category}</b> with 
            <b>{urgency}</b> urgency.  
            High-urgency emails should be prioritised for immediate action.
            </div>
            """,
            unsafe_allow_html=True
        )

st.markdown("</div>", unsafe_allow_html=True)


# --------------------------------------------------
# Footer
# --------------------------------------------------
st.markdown(
    "<p style='text-align:center;color:#9ca3af;margin-top:25px;font-size:13px;'>"
    "Built by Sai Keerthi • Infosys Springboard Project"
    "</p>",
    unsafe_allow_html=True
)
