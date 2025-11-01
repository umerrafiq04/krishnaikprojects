
import pandas as pd
import re
import nltk
import numpy as np

# Download stopwords
nltk.download("stopwords")
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# 1. Load and clean dataset
messages = pd.read_csv("nlp_proj\spam.csv", encoding='latin1')
messages.drop(['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], axis=1, inplace=True)
messages.rename(columns={'v1': 'label', 'v2': 'message'}, inplace=True)

# 2. Preprocessing function
ps = PorterStemmer()

def preprocess(text):
    text = re.sub('[^a-zA-Z]', ' ', text)         # Keep only letters
    text = text.lower()
    text = text.split()
    text = [ps.stem(word) for word in text if word not in stopwords.words("english")]
    return " ".join(text)

# 3. Apply preprocessing
corpus = [preprocess(msg) for msg in messages['message']]

# 4. Feature extraction
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=2500, ngram_range=(1,2))
X = cv.fit_transform(corpus).toarray()

# 5. Encode labels
y = pd.get_dummies(messages['label'], drop_first=True).astype(int).iloc[:, 0]  # spam = 1, ham = 0

# 6. Train-test split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

# 7. Model training
from sklearn.naive_bayes import MultinomialNB
spam_detect_model = MultinomialNB().fit(X_train, y_train)

import pickle

# Save the trained model
with open("spam_model.pkl", "wb") as model_file:
    pickle.dump(spam_detect_model, model_file)

# Save the CountVectorizer
with open("vectorizer.pkl", "wb") as vec_file:
    pickle.dump(cv, vec_file)