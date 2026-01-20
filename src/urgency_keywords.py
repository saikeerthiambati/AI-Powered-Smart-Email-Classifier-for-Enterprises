def keyword_urgency(text):
    text = text.lower()

    high = ["urgent", "asap", "immediately", "not working", "refund", "complaint"]
    medium = ["issue", "delay", "support", "request", "help"]

    for word in high:
        if word in text:
            return "High"

    for word in medium:
        if word in text:
            return "Medium"

    return "Low"
