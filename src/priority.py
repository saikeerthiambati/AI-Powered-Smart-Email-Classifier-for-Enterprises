import pandas as pd

df = pd.read_csv("data/Clean Datasets/spam_with_category.csv")

# rule-based priority
def assign_priority(cat):
    cat = str(cat).lower()
    if cat == 'complaint':
        return 'high'
    elif cat == 'request':
        return 'medium'
    elif cat == 'spam':
        return 'none'
    else:
        return 'low'

df['priority'] = df['category'].apply(assign_priority)

df.to_csv("final_email_dataset.csv", index=False)

print("✔ Priority added!")
print(df['priority'].value_counts())
print("🎉 Final dataset saved as final_email_dataset.csv")
