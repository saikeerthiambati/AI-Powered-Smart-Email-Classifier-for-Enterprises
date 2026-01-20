import pandas as pd
import torch
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
from sklearn.preprocessing import LabelEncoder

print("🚀 Running DistilBERT inference for email categorization...")

# Load dataset
df = pd.read_csv("../data/Clean Datasets/spam_with_category_and_urgency.csv")
df = df.dropna(subset=["clean_text", "category"])

# Encode labels
label_encoder = LabelEncoder()
df["label"] = label_encoder.fit_transform(df["category"])

num_labels = len(label_encoder.classes_)

# Load tokenizer & model
tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-uncased")
model = DistilBertForSequenceClassification.from_pretrained(
    "distilbert-base-uncased",
    num_labels=num_labels
)

model.eval()

# Take small sample for fast inference
sample_texts = df["clean_text"].sample(10, random_state=42).tolist()
true_labels = df.loc[df["clean_text"].isin(sample_texts), "category"].tolist()

# Tokenize
inputs = tokenizer(
    sample_texts,
    truncation=True,
    padding=True,
    return_tensors="pt"
)

# Inference
with torch.no_grad():
    outputs = model(**inputs)
    predictions = torch.argmax(outputs.logits, dim=1)

predicted_labels = label_encoder.inverse_transform(predictions.numpy())

# Display results
print("\n📊 Sample Predictions (Transformer Inference):\n")
for i in range(len(sample_texts)):
    print(f"Email {i+1}:")
    print(f"Predicted Category: {predicted_labels[i]}")
    print("-" * 50)

print("\n✅ DistilBERT inference completed successfully!")
