import streamlit as st
from datetime import datetime

# --------------------------------------------------
# Page Config
# --------------------------------------------------
st.set_page_config(
    page_title="AI Powered Smart Email Classifier",
    page_icon="📧",
    layout="wide"
)

# --------------------------------------------------
# Session State Init
# --------------------------------------------------
if "history" not in st.session_state:
    st.session_state.history = []

if "processed" not in st.session_state:
    st.session_state.processed = 0

if "critical" not in st.session_state:
    st.session_state.critical = 0

if "clear_form" not in st.session_state:
    st.session_state.clear_form = False

# --------------------------------------------------
# Dummy Classification Logic
# --------------------------------------------------
def classify_email(subject, content):
    text = (subject + " " + content).lower()

    spam_words = ["win", "free", "prize", "offer"]
    urgent_words = ["urgent", "asap", "immediately", "critical"]

    is_spam = any(w in text for w in spam_words)
    urgency = "High" if any(w in text for w in urgent_words) else "Low"

    if is_spam:
        category = "Spam"
    elif "complaint" in text:
        category = "Complaint"
    elif "request" in text:
        category = "Request"
    else:
        category = "General"

    return is_spam, category, urgency

# --------------------------------------------------
# Header
# --------------------------------------------------
st.markdown("## 📧 AI Powered Smart Email Classifier for Enterprises")

m1, m2 = st.columns(2)
m1.metric("Processed", st.session_state.processed)
m2.metric("Critical", st.session_state.critical)

tabs = st.tabs(["📨 Email Analysis", "📊 Analytics", "🕘 History"])

# ==================================================
# TAB 1: EMAIL ANALYSIS
# ==================================================
with tabs[0]:
    left, right = st.columns([1.2, 1])

    with left:
        st.subheader("Input Email")

        # ---- FORM (important!) ----
        with st.form("email_form", clear_on_submit=st.session_state.clear_form):
            subject = st.text_input("Subject")
            content = st.text_area("Email Content", height=220)

            c1, c2 = st.columns(2)
            analyze = c1.form_submit_button("🚀 Analyze Email")
            clear = c2.form_submit_button("🧹 Clear")

        if clear:
            st.session_state.clear_form = True
            st.rerun()

        if analyze:
            st.session_state.clear_form = False

            if not subject or not content:
                st.warning("Please enter both subject and content.")
            else:
                spam, category, urgency = classify_email(subject, content)

                st.session_state.processed += 1
                if urgency == "High":
                    st.session_state.critical += 1

                st.session_state.history.append({
                    "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "subject": subject,
                    "category": category,
                    "urgency": urgency
                })

                with right:
                    st.subheader("AI Interpretation")
                    st.success("Email analyzed successfully!")
                    st.write(f"🛑 **Spam:** {'Yes' if spam else 'No'}")
                    st.write(f"📂 **Category:** {category}")
                    st.write(f"⚡ **Urgency:** {urgency}")

# ==================================================
# TAB 2: ANALYTICS
# ==================================================
with tabs[1]:
    st.subheader("Analytics")

    if not st.session_state.history:
        st.info("No analytics data available.")
    else:
        categories = {}
        urgencies = {"High": 0, "Low": 0}

        for h in st.session_state.history:
            categories[h["category"]] = categories.get(h["category"], 0) + 1
            urgencies[h["urgency"]] += 1

        a1, a2 = st.columns(2)
        a1.bar_chart(categories)
        a2.bar_chart(urgencies)

# ==================================================
# TAB 3: HISTORY
# ==================================================
with tabs[2]:
    st.subheader("Session History")

    if not st.session_state.history:
        st.info("No records found.")
    else:
        st.table(st.session_state.history)

        if st.button("🗑 Clear History"):
            st.session_state.history = []
            st.session_state.processed = 0
            st.session_state.critical = 0
            st.rerun()

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.markdown("---")
st.markdown(
    "<center>Built by Sai Keerthi • Infosys Springboard Project</center>",
    unsafe_allow_html=True
)
