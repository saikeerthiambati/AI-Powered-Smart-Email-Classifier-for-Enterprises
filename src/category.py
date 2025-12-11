import pandas as pd
import re

print("📁 Adding category...")

df = pd.read_csv(r"data/Clean Datasets/spam_dataset_cleaned_encoded.csv")

email = pd.read_csv(r"data/Raw Datasets/emailclass.csv")

# clean email text too (same cleaning!)
def clean(text):
    text = str(text).lower()
    text = re.sub(r"http\S+|www.\S+", "", text)
    text = re.sub(r"<.*?>", "", text)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

email['clean_text'] = email['text'].apply(clean)

# rename type -> category
email = email.rename(columns={'type': 'category'})

# merge on clean_text instead of text
df = df.merge(email[['clean_text', 'category']], on='clean_text', how='left')

# for spam emails, set category as spam
df.loc[df['label']==1, 'category'] = 'spam'

# fill missing
df['category'] = df['category'].fillna('general')

df.to_csv("spam_with_category.csv", index=False)

print("✔ Category fixed using clean_text")
print(df['category'].value_counts())
print("🎉 Saved as spam_with_category.csv")
print("✅ Category addition complete!")
