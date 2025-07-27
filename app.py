# app.py
import streamlit as st
import pickle
import re

# loading the model and vectorizer
with open('model/news_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('model/tfidf.pkl', 'rb') as tfidf_file:
    tfidf = pickle.load(tfidf_file)

# function to clean input text
def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+|www\S+|https\S+", '', text)
    text = re.sub(r'\@w+|\#','', text)
    text = re.sub(r'[^a-z\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# UI
st.set_page_config(page_title="News Article Classifier", layout="centered")
st.title("📰 Fake News Detector")

input_text = st.text_area("Paste a news article here...", height=250)

if st.button("Check"):
    if input_text.strip() == "":
        st.warning("Please enter some text.")
    else:
        cleaned = clean_text(input_text)
        vectorized = tfidf.transform([cleaned])
        prediction = model.predict(vectorized)[0]

        if prediction == 1:
            st.success("✅ This article looks **REAL**.")
        else:
            st.error("🚨 This article seems **FAKE**.")
        st.text_area("Cleaned Text", value=cleaned, height=250)