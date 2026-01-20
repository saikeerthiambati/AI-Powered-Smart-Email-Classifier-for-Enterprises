import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

# Load dataset
df = pd.read_csv("data/Clean Datasets/spam_with_category_and_urgency.csv")

# Remove rows with missing text or urgency
df = df.dropna(subset=['clean_text', 'urgency'])


X = df['clean_text']
y = df['urgency']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# TF-IDF
vectorizer = TfidfVectorizer(stop_words='english', max_features=3000)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Model
model = LogisticRegression(max_iter=1000)
model.fit(X_train_vec, y_train)

# Predictions
y_pred = model.predict(X_test_vec)

# Evaluation
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))
from urgency_keywords import keyword_urgency

def final_urgency(text):
    keyword_result = keyword_urgency(text)

    if keyword_result == "High":
        return "High"

    vec = vectorizer.transform([text])
    return model.predict(vec)[0]
print(final_urgency("This is urgent, my service is not working"))
print(final_urgency("Need support regarding my request"))
