import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer


nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

ps = PorterStemmer()

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

# Load model and vectorizer
tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

# Page config
st.set_page_config(page_title="Spam Classifier", layout="centered")


st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    .stApp {
        background-color: #0a0e27;
    }
    
    h1 {
        color: #4A90E2;
        font-weight: 600;
        font-size: 2rem;
    }
    
    .stTextArea textarea {
        background-color: #1a1f3a;
        color: #ffffff;
        border: 1px solid #4A90E2;
        border-radius: 8px;
    }
    
    .stButton>button {
        background-color: #4A90E2;
        color: #ffffff;
        border: none;
        border-radius: 8px;
        padding: 12px;
        font-weight: 600;
        width: 100%;
    }
    
    .stButton>button:hover {
        background-color: #357ABD;
    }
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)


st.title("Email/SMS Spam Classifier")

input_sms = st.text_area("Enter the message", height=150)

if st.button("Predict"):
    if input_sms.strip():
        transformed_sms = transform_text(input_sms)
        vector_input = tfidf.transform([transformed_sms])
        result = model.predict(vector_input)[0]
        
        if result == 1:
            st.error("Spam")
        else:
            st.success("Not Spam")