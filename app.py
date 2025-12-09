import streamlit as st
import pickle
import string
import numpy as np
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()

# ------------------------------------------------------
# TEXT TRANSFORM FUNCTION
# ------------------------------------------------------
def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

# ------------------------------------------------------
# LOAD MODEL + VECTORIZER
# ------------------------------------------------------
tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

# ------------------------------------------------------
# STREAMLIT UI
# ------------------------------------------------------
st.title("Email / SMS Spam Classifier")

input_sms = st.text_area("Enter your message")

# ------------------------------------------------------
# PREDICT BUTTON
# ------------------------------------------------------
if st.button("Predict"):

    if input_sms.strip() == "":
        st.warning("Please enter a message.")
    else:
        # 1. Preprocess
        transformed_sms = transform_text(input_sms)

        # 2. Extra feature: message length
        num_characters = len(input_sms)

        # 3. Vectorize
        vector_input = tfidf.transform([transformed_sms]).toarray()

        # 4. Add extra feature
        vector_input = np.hstack((vector_input, np.array([[num_characters]])))

        # 5. Predict
        result = model.predict(vector_input)[0]

        # 6. Display result
        if result == 1:
            st.error("**Spam Message Detected!**")     
        else:
            st.success("**This Message is NOT Spam.**")  
