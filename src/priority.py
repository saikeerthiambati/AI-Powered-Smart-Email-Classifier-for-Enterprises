import pandas as pd

print("🚀 Adding priority levels...")

# Load dataset created from category + urgency step
df = pd.read_csv("../data/Clean Datasets/spam_with_category_and_urgency.csv")

# Rule-based priority assignment
def assign_priority(cat):
    cat = str(cat).lower()

    if cat == "complaint":
        return "High"
    elif cat == "request":
        return "Medium"
    elif cat == "spam":
        return "None"
    else:
        return "Low"

# Apply priority logic
df["priority"] = df["category"].apply(assign_priority)

# Save final dataset
output_path = "../data/Clean Datasets/final_email_dataset.csv"
df.to_csv(output_path, index=False)

print("✔ Priority added successfully!")
print("\n📊 Priority Distribution:")
print(df["priority"].value_counts())

print(f"\n🎉 Final dataset saved as: {output_path}")
