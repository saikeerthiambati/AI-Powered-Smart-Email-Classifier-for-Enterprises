# 🧠 Smart Email Classifier

An AI-powered system designed to clean, categorize, and prepare email datasets for intelligent spam detection and enterprise-level email classification.

This repository currently contains **Milestone 1**, focusing on data cleaning, preprocessing, merging, labeling, and creation of the final ML-ready dataset.

---

## 📁 Project Structure

```
Smart-Email-Classifier/
│
├── data/
│   ├── raw/            # Original unprocessed datasets
│   └── clean/          # Cleaned & transformed datasets
│
├── src/                # Python source scripts
│   ├── combine.py
│   ├── category.py
│   ├── final_dataset.py
│   ├── priority.py
│   └── spam_email.py
│
├── README.md
└── .gitignore
```

---

## 🎯 Milestone 1 — Summary (Completed)

- Cleaned raw email datasets  
- Merged datasets into a unified structure  
- Added spam / general labels  
- Assigned categories using cleaned text  
- Performed text normalization & preprocessing  
- Added feature engineering:
  - text_length  
  - num_words  
  - num_digits  
  - has_url  
- Generated the final ML-ready dataset  

📌 **Final output file:**  
`data/clean/final_dataset.csv`

---

## 🛠 Scripts Overview

| Script Name         | Description |
|---------------------|-------------|
| `combine.py`        | Merges raw datasets into one combined file |
| `category.py`       | Cleans text & assigns categories |
| `final_dataset.py`  | Generates the final dataset with engineered features |
| `priority.py`       | Assigns priority levels to emails |
| `spam_email.py`     | Initial spam-email processing and testing |

---

## 🚀 How to Run the Project

### Step 1 — Navigate to the src folder
```
cd src
```

### Step 2 — Run the final dataset generation script
```
python final_dataset.py
```

This will generate the file:

```
data/clean/final_dataset.csv
```

---

## 📌 Upcoming Milestone 2

- TF-IDF vectorization  
- Logistic Regression & SVM models  
- Performance metrics (Accuracy, Precision, Recall, F1-score)  
- Confusion matrix visualization  
- Save & load trained model  

---

## 📌 Future Enhancements

- Real-time email classification API (FastAPI/Flask)  
- Streamlit web interface  
- Phishing detection using URL-pattern analysis  
- Deep learning (BERT) based classifier  

---

## 👨‍💻 Author

**Sai Keerthi Ambati**  
AI & Machine Learning Enthusiast  
Infosys Springboard Project  

---

