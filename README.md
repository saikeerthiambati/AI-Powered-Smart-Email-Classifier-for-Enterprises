# 📧 AI Powered Smart Email Classifier for Enterprises

An AI-powered system that automatically classifies enterprise emails and detects urgency to improve response efficiency using NLP and Machine Learning.

---

## 🚀 Project Overview

Enterprises receive thousands of emails daily related to customer complaints, service requests, feedback, and spam.  
Manual email triaging is time-consuming and inefficient, often leading to delayed responses and reduced customer satisfaction.

This project automates:
- Email categorization
- Urgency detection
- Priority assignment

using **Machine Learning and NLP techniques**.

---

## 🎯 Project Objectives

- Automate email classification into multiple categories  
- Reduce manual effort in email triaging  
- Improve response prioritization and efficiency  
- Prepare a foundation for enterprise-level deployment  

---

## 🧠 Features

- 📂 Email Categorization (Complaint, Request, Spam, etc.)
- ⚡ Urgency Detection (High / Medium / Low)
- 🚨 Priority Assignment
- 🖥️ Interactive UI using Streamlit
- 📊 Cleaned & processed datasets
- 🧪 Rule-based + ML-based models

---

## 🗂️ Project Structure

```

AI-Powered-Smart-Email-Classifier-for-Enterprises/
│
├── streamlit_app.py          # Main Streamlit application
├── requirements.txt          # Project dependencies
│
├── src/
│   ├── spam_email.py
│   ├── priority.py
│   ├── urgency_model.py
│   ├── urgency_keywords.py
│   ├── baseline_models.py
│   └── bert_category_model.py
│
├── data/
│   ├── Raw Datasets/
│   └── Clean Datasets/
│
├── dashboard/
│   ├── static/
│   └── templates/
│
├── LICENSE
└── README.md

```
## ✅ Milestone 1 — Data Collection & Preprocessing (Completed)

**Objective:** Prepare a clean and labeled dataset for machine learning.

### Key Achievements
- Cleaned raw email datasets  
- Removed noise (HTML tags, punctuation, stopwords)  
- Normalized text for NLP processing  
- Labeled emails with:
  - Spam / Non-spam  
  - Email categories  
- Engineered features:
  - `text_length`
  - `num_words`
  - `num_digits`
  - `has_url`
- Generated a unified ML-ready dataset  

📌 **Final Output File**
```
data/clean/final_dataset.csv
```

---

## ✅ Milestone 2 — Email Categorization Engine (Completed)

**Objective:** Develop and evaluate an NLP-based email classification system.

### Implemented Features
- TF-IDF based text vectorization  
- Baseline ML models:
  - Logistic Regression  
  - Support Vector Machine (SVM)  
  - Naive Bayes  

### Model Evaluation
- Accuracy  
- Precision  
- Recall  
- F1-score  
- Confusion Matrix  

📌 **Key Script**
```
src/baseline_models.py
```

---

## 🛠 Scripts Overview

| Script Name | Description |
|------------|-------------|
| combine.py | Merges raw datasets into a single dataset |
| category.py | Cleans email text and assigns categories |
| final_dataset.py | Generates the final ML-ready dataset |
| priority.py | Assigns urgency levels to emails |
| spam_email.py | Initial spam classification logic |
| baseline_models.py | Trains and evaluates ML classifiers |

---

## 🚀 How to Run the Project

### Step 1: Navigate to source directory
```bash
cd src
```

### Step 2: Generate the final dataset
```bash
python final_dataset.py
```

### Step 3: Run classification models
```bash
python baseline_models.py
```

---

## 🔮 Future Enhancements
- Urgency prediction model (High / Medium / Low)  
- Deep learning models (BERT / DistilBERT)  
- Real-time email classification API (FastAPI / Flask)  
- Interactive dashboard for enterprise users  
- Cloud deployment (AWS / Azure / GCP)  
- Phishing detection using URL and content analysis  

---

## 👨‍💻 Author

**Sai Keerthi Ambati**  
AI & Machine Learning Enthusiast  
Infosys Springboard Intern
