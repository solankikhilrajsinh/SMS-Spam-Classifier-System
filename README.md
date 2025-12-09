Email/SMS Spam Classification System

This project is a complete Email/SMS Spam Classification System built using Python, FastAPI, and Streamlit. It applies machine learning and text-processing techniques to accurately classify messages as spam or non-spam. The system uses the Kaggle SMS/Email Spam Dataset and integrates multiple preprocessing and modeling libraries to ensure reliable and real-time predictions through an API-driven architecture.


Features
- Classification of SMS and email messages into spam or non-spam
- Preprocessing of text data including cleaning, tokenization, stopword removal, and vectorization
- FastAPI backend serving predictions through REST endpoints
- Streamlit frontend interface for message input and classification output
- Integration of machine learning and NLP models (e.g., Naive Bayes, Logistic Regression, SVM)
- Modular and scalable project structure suitable for deployment


Tech Stack
- Python
- FastAPI (Backend API)
- Streamlit (Frontend UI)
- Pandas, NumPy
- Scikit-learn
- NLTK and text-processing libraries
- Kaggle SMS/Email Spam Dataset


Dataset 
  The system uses the Kaggle SMS/Email Spam Dataset, which contains a collection of labeled messages. Each entry includes:
- Message text
- Spam or non-spam (ham) classification
- Clean and well-structured data suitable for supervised learning tasks


How It Works
1. Text messages are cleaned and preprocessed using NLP techniques.
2. Messages are converted into numerical vectors using TF-IDF or other vectorization methods.
3. A trained machine learning model predicts whether the message is spam or not.
4. FastAPI exposes an endpoint through which the classification model can be accessed.
5. The Streamlit UI sends user input to the API and displays predictions instantly.
