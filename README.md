# News-Article-Classifier

This project uses machine learning to classify news articles as either **fake** or **real** based on their content.  
It was built as part of an internship project to explore how Natural Language Processing (NLP) and text classification work.

# Tools Used
- Python
- Pandas
- Scikit-learn
- NLTK
- Streamlit

# How It Works
1. Loaded and labeled a dataset of real and fake news articles.
2. Cleaned the text (lowercase, removed links/symbols).
3. Converted the text into TF-IDF vectors.
4. Trained a Logistic Regression model (achieved ~98.6% accuracy).
5. Built a Streamlit web app where users can paste any article and get a fake/real prediction.
