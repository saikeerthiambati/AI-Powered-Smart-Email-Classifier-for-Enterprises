import pandas as pd
import re

print("🚀 Preparing spam dataset...")

# -------------------------------------------------
# 1️⃣ Load dataset (combined dataset from previous step)
# -------------------------------------------------
df = pd.read_csv(r"C:\Users\HP\Desktop\Infosys Springboard\data\Clean Datasets\spam_dataset_final.csv")
print("✔ Loaded spam_dataset_final.csv")

# -------------------------------------------------
# 2️⃣ Clean text
# -------------------------------------------------
def clean(text):
    text = str(text).lower()                      # lowercase
    text = re.sub(r"http\S+|www.\S+", "", text)   # remove URLs
    text = re.sub(r"<.*?>", "", text)             # remove HTML
    text = re.sub(r"[^a-zA-Z\s]", "", text)       # remove punctuation & numbers
    text = re.sub(r"\s+", " ", text).strip()      # clean spaces
    return text

df['clean_text'] = df['text'].apply(clean)
print("✔ Text cleaned")


# -------------------------------------------------
# 3️⃣ Fix label values
# -------------------------------------------------
# Convert to string
df['label'] = df['label'].astype(str).str.strip()

# if label == '1' keep 1, else make it 0
df['label'] = df['label'].apply(lambda x: 1 if x=='1' else 0)

print("✔ Labels fixed (1 = spam, 0 = ham)")


# -------------------------------------------------
# 4️⃣ Save final cleaned+encoded version
# -------------------------------------------------

output_path = "../data/Clean Datasets/spam_dataset_cleaned_encoded.csv"
df.to_csv(output_path, index=False)

print("🎉 Saved as spam_dataset_cleaned_encoded.csv")
print("📌 Total rows:", len(df))
print("📌 Spam rows:", df['label'].sum())
print("📌 Ham rows:", len(df) - df['label'].sum())
print("📌 Spam percentage: {:.2f}%".format((df['label'].sum() / len(df)) * 100))
print("📌 Ham percentage: {:.2f}%".format(((len(df) - df['label'].sum()) / len(df)) * 100))
print("✅ Spam dataset preparation complete!")