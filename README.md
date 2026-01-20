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

## ✅ Milestone 3 — Urgency Detection & Priority Classification (Completed)

**Objective:**
Identify time-sensitive emails and assign appropriate priority levels to enable faster response handling.

**Key Achievements**

- Designed a rule-based urgency detection system
- Created a curated list of urgency keywords (e.g., urgent, immediate, ASAP, critical)
- Implemented urgency scoring logic based on:
         - Keyword frequency
         - Keyword position in email text
- Classified emails into priority levels:
              - High
              - Medium
              - Low
- Integrated urgency detection with category and spam classification outputs

📌 Key Scripts
```
src/urgency_model.py

src/urgency_keywords.py

src/priority.py
```

##✅ Milestone 4 — Application Integration, Deployment & Documentation (Completed)

**Objective:**
Build an interactive user interface, integrate all ML components, and deploy the system for real-world usage.

**Key Achievements**

- Integrated all modules (spam detection, categorization, urgency) into a single pipeline
- Developed a user-friendly Streamlit web application
**Implemented:**
 - Email text input interface
 - “Classify Email” action button
Real-time display of:
         - Spam status
         - Email category
         - Urgency level
- Successfully deployed the application on Streamlit Cloud
- Added complete project documentation and licensing

📌 Key Files & Deliverables
```
streamlit_app.py — Main application entry point

requirements.txt — Deployment-safe dependencies

README.md — Project documentation

LICENSE — MIT License
```

## 🛠 Scripts Overview

| Script Name              | Description                                                                       |
| ------------------------ | --------------------------------------------------------------------------------- |
| `combine.py`             | Merges multiple raw email datasets into a single unified dataset                  |
| `category.py`            | Cleans email text and assigns email categories *(if applicable in earlier phase)* |
| `final_dataset.py`       | Generates the final machine-learning-ready dataset after preprocessing            |
| `priority.py`            | Assigns priority levels (High / Medium / Low) based on urgency analysis           |
| `spam_email.py`          | Implements spam vs non-spam email classification logic                            |
| `baseline_models.py`     | Trains and evaluates baseline ML classifiers using TF-IDF features                |
| `bert_category_model.py` | Implements BERT-based model for advanced email category classification            |
| `urgency_model.py`       | Detects urgency level in emails using keyword-based and scoring logic             |
| `urgency_keywords.py`    | Stores and manages predefined urgency-related keywords                            |
| `streamlit_app.py`       | Main Streamlit application integrating all models with a user interface           |


---

🚀 How to Run the Project
🔹 Prerequisites
Python 3.8 or above
pip package manager

Step 1: Clone the repository
git clone https://github.com/saikeerthiambati/AI-Powered-Smart-Email-Classifier-for-Enterprises.git
cd AI-Powered-Smart-Email-Classifier-for-Enterprises

Step 2: Install dependencies
pip install -r requirements.txt

Step 3: Navigate to source directory
cd src

Step 4: Generate the final dataset
python final_dataset.py
This step:
Cleans raw email data
Extracts features
Produces an ML-ready dataset

Step 5: Train and evaluate baseline models
python baseline_models.py
This step:
Applies TF-IDF vectorization
Trains Logistic Regression, SVM, and Naive Bayes
Evaluates performance using accuracy, precision, recall, and F1-score

Step 6: Run the Streamlit application
Go back to the project root directory:
cd ..
Start the Streamlit app:
streamlit run streamlit_app.py

Step 7: Access the application
Open your browser
Navigate to the URL shown in the terminal (usually):
http://localhost:8501

🎯 Final Output

Interactive web interface for email classification
Displays:
Spam / Non-spam status
Email category
Urgency / priority level

## 👨‍💻 Author

**Sai Keerthi Ambati**  
AI & Machine Learning Enthusiast  
Infosys Springboard Intern
