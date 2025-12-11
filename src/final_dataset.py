import pandas as pd
import re

print("📁 Creating Final Dataset...")

# Load your merged + categorized dataset
df = pd.read_csv(r"C:\Users\HP\Desktop\Infosys Springboard\Clean Datasets\spam_with_category.csv")

# If original text exists, use clean_text only
df['clean_text'] = df['clean_text'].astype(str)

# Add simple engineered features
df['text_length'] = df['clean_text'].apply(len)
df['num_words'] = df['clean_text'].apply(lambda x: len(x.split()))
df['num_digits'] = df['clean_text'].apply(lambda x: sum(c.isdigit() for c in x))
df['has_url'] = df['clean_text'].apply(lambda x: 1 if 'http' in x or 'www' in x else 0)

# Category cleanup (optional)
df['category'] = df['category'].fillna('general')

# Label cleanup
df['label'] = df['label'].fillna(0).astype(int)

# Drop duplicates
df = df.drop_duplicates(subset=['clean_text'])

# Final column ordering
df = df[['clean_text', 'label', 'category', 'text_length', 'num_words', 'num_digits', 'has_url']]

# Save final dataset
df.to_csv("final_dataset.csv", index=False)

print("🎉 Final Dataset Created Successfully!")
print("Rows:", len(df))
print(df.head())
