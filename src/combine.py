import pandas as pd

print("🚀 Starting spam dataset merging...")

# ----- Load datasets -----
try:
    df_cleaned = pd.read_csv(r"C:\Users\HP\Desktop\Infosys Springboard\data\Raw Datasets\spam_dataset.csv")
    print("✔ Loaded spam_dataset.csv")
except:
    print("❌ Could not load spam_dataset.csv")
    exit()

try:
    df_emailclass = pd.read_csv(r"C:\Users\HP\Desktop\Infosys Springboard\data\Raw Datasets\emailclass.csv")
    print("✔ Loaded emailclass.csv")
except:
    print("❌ Could not load emailclass.csv")
    exit()


# ----- Rename columns -----
df_cleaned = df_cleaned.rename(columns={'clean_text': 'text', 'target': 'label'})
df_emailclass = df_emailclass.rename(columns={'type': 'label'})
print("✔ Renamed columns")


# ----- Remove duplicate columns if they exist -----
df_cleaned = df_cleaned.loc[:, ~df_cleaned.columns.duplicated()]
df_emailclass = df_emailclass.loc[:, ~df_emailclass.columns.duplicated()]
print("✔ Removed duplicate columns")


# ----- Select only required columns -----
df_cleaned = df_cleaned[['text', 'label']]
df_emailclass = df_emailclass[['text', 'label']]
print("✔ Selected necessary columns")


# ----- Reset index to avoid concat errors -----
df_cleaned.reset_index(drop=True, inplace=True)
df_emailclass.reset_index(drop=True, inplace=True)


# ----- Combine -----
combined = pd.concat([df_cleaned, df_emailclass], ignore_index=True)
print("✔ Combined datasets")


# ----- Remove duplicates & missing -----
combined.drop_duplicates(subset=['text'], inplace=True)
combined.dropna(subset=['text', 'label'], inplace=True)
print("✔ Cleaned final rows")


# ----- Save -----
combined.to_csv("spam_dataset_final.csv", index=False)
print("🎉 Final spam dataset saved as spam_dataset_final.csv")
print("📌 Total rows:", combined.shape[0])
