import pickle
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

nltk.download("stopwords")

# Load the model and vectorizer
with open("spam_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

with open("vectorizer.pkl", "rb") as vec_file:
    vectorizer = pickle.load(vec_file)

# Define preprocessing (same as used during training)
ps = PorterStemmer()
def preprocess(text):
    text = re.sub('[^a-zA-Z]', ' ', text)
    text = text.lower()
    text = text.split()
    text = [ps.stem(word) for word in text if word not in stopwords.words("english")]
    return " ".join(text)

from flask import Flask,request,render_template
import numpy as np
import pandas as pd



application=Flask(__name__)

app=application

## Route for a home page

@app.route('/')
def index():
    return render_template('home.html') 

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    else:
        email=request.form.get('mail')
        email_processed = preprocess(email)
        email_vector = vectorizer.transform([email_processed]).toarray()
        result = model.predict(email_vector)

        results="Spam" if result[0] else "Ham"
        return render_template('home.html',results=results)
    

if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)        



"#determines entry point"