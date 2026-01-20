from flask import Flask, render_template, request
import sys
sys.path.append("../src")

from urgency_model import final_urgency

app = Flask(
    __name__,
    template_folder="../dashboard/templates",
    static_folder="../dashboard/static"
)

@app.route("/")
def home():
    return render_template("dashboard.html")


@app.route("/predict", methods=["POST"])
def predict():
    email_text = request.form.get("email")

    # -----------------------------
    # Category Prediction (Rule-based for now)
    # -----------------------------
    text = email_text.lower()

    if "refund" in text or "not working" in text or "complaint" in text:
        category = "Complaint"
    elif "request" in text or "please provide" in text:
        category = "Request"
    elif "offer" in text or "lottery" in text or "free money" in text:
        category = "Spam"
    else:
        category = "General"

    # -----------------------------
    # Urgency Prediction (Your ML + Keywords)
    # -----------------------------
    urgency = final_urgency(email_text)

    result = {
        "category": category,
        "urgency": urgency
    }

    return render_template("dashboard.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
