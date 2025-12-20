AI Powered Smart Email Classifier for Enterprises

An AI-powered system designed to automatically clean, categorize, and analyze enterprise email datasets for intelligent spam detection, email categorization, and priority assignment using Natural Language Processing (NLP) and Machine Learning techniques.

📌 Project Overview

Enterprises receive thousands of emails daily related to customer complaints, service requests, feedback, and spam. Manual email triaging is time-consuming and inefficient, often leading to delayed responses and reduced customer satisfaction.

This project focuses on building an AI-powered Smart Email Classifier that automates email categorization and supports intelligent decision-making by leveraging NLP and machine learning models.

🎯 Project Objectives

Automate email classification into multiple categories

Reduce manual effort in email triaging

Improve response prioritization and efficiency

Prepare the foundation for enterprise-level deployment

AI-Powered-Smart-Email-Classifier-for-Enterprises/
│
├── data/
│   ├── raw/                    # Original unprocessed datasets
│   └── clean/                  # Cleaned & ML-ready datasets
│
├── src/
│   ├── combine.py              # Dataset merging
│   ├── category.py             # Text cleaning & category labeling
│   ├── final_dataset.py        # Final dataset creation
│   ├── priority.py             # Email priority assignment
│   ├── spam_email.py           # Initial spam processing
│   └── baseline_models.py      # Milestone 2 classification models
│
├── README.md
├── LICENSE
└── .gitignore

✅ Milestone 1 — Data Collection & Preprocessing (Completed)

Objective: Prepare a clean and labeled dataset for machine learning.

Key Achievements

Cleaned raw email datasets

Removed noise (HTML tags, punctuation, stopwords)

Normalized text for NLP processing

Labeled emails with:

Spam / Non-spam

Email categories

Engineered useful features:

text_length

num_words

num_digits

has_url

Generated a unified ML-ready dataset

📌 Final Output File:

data/clean/final_dataset.csv

✅ Milestone 2 — Email Categorization Engine (Completed)

Objective: Develop and evaluate an NLP-based email classification system.

Implemented Features

TF-IDF based text vectorization

Baseline machine learning models:

Logistic Regression

Support Vector Machine (SVM)

Naive Bayes (for comparison)

Model evaluation using:

Accuracy

Precision

Recall

F1-score

Confusion matrix visualization for performance analysis

Comparative analysis of classifiers

📌 Key Script:

src/baseline_models.py

🛠 Scripts Overview
Script Name	Description
combine.py	Merges raw datasets into a single dataset
category.py	Cleans email text and assigns categories
final_dataset.py	Generates the final ML-ready dataset
priority.py	Assigns urgency levels to emails
spam_email.py	Initial spam classification logic
baseline_models.py	Trains and evaluates ML classifiers
🚀 How to Run the Project
Step 1: Navigate to the source directory
cd src

Step 2: Generate the final dataset
python final_dataset.py


This will create:

data/clean/final_dataset.csv

Step 3: Run Milestone 2 classification models
python baseline_models.py


This will:

Train ML models

Display evaluation metrics

Visualize confusion matrices

📌 Future Enhancements

Urgency prediction model (High / Medium / Low)

Deep learning models (BERT / DistilBERT)

Real-time email classification API (FastAPI / Flask)

Interactive dashboard for enterprise users

Cloud deployment (AWS / Azure / GCP)

Phishing detection using URL and content analysis

👨‍💻 Author

Sai Keerthi Ambati
AI & Machine Learning Enthusiast
Infosys Springboard Intern
