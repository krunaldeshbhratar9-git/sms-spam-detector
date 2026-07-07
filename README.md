# SMS Spam Classifier

A machine learning-based SMS spam detection system that identifies spam messages with high accuracy using Natural Language Processing (NLP) and the Naive Bayes algorithm.

---

## 📋 Project Overview

This project demonstrates a complete end-to-end machine learning pipeline — from raw data processing to web deployment. It trains a classifier on labeled SMS messages to automatically detect spam, then deploys it as an interactive web application where users can test any message in real-time.

**Key Features:**
- Text preprocessing using NLTK (tokenization, stemming, stopword removal)
- TF-IDF feature extraction for numerical representation
- Naive Bayes classification algorithm
- Interactive web interface using Streamlit
- Pre-trained model ready for instant predictions

---

## 🎯 How It Works

### **Training Phase** (smsspamdetection.ipynb)
1. **Load Data**: SMS messages from `spam.csv` (labeled as spam/ham)
2. **Preprocess**: Clean text using lowercase conversion, tokenization, and stemming
3. **Vectorize**: Convert text to numerical features using TF-IDF
4. **Train**: Naive Bayes learns patterns distinguishing spam from legitimate messages
5. **Evaluate**: Test accuracy on unseen data
6. **Save**: Export trained model and vectorizer as `.pkl` files

### **Deployment Phase** (app.py)
1. **Load Model**: Import pre-trained model and vectorizer
2. **User Input**: Accept message via Streamlit web interface
3. **Process**: Apply same cleaning pipeline as training
4. **Predict**: Model outputs spam (1) or not spam (0)
5. **Display**: Show result instantly on screen

---

## 📁 Project Files

| File | Purpose |
|------|---------|
| `app.py` | Streamlit web application for making predictions |
| `smsspamdetection.ipynb` | Jupyter notebook with training code and data exploration |
| `model.pkl` | Trained Naive Bayes classifier (binary) |
| `vectorizer.pkl` | Fitted TF-IDF vectorizer for text conversion |
| `spam.csv` | Dataset of labeled SMS messages (training data) |
| `requirements.txt` | Python dependencies |
| `README.md` | Project documentation |

---

## 🛠️ Tech Stack

**Libraries & Tools:**
- **Python** - Programming language
- **NLTK** - Natural Language Processing (tokenization, stemming, stopword removal)
- **Scikit-learn** - Machine Learning (TF-IDF, Naive Bayes, model evaluation)
- **Streamlit** - Web application framework
- **Pandas** - Data manipulation
- **Pickle** - Model serialization

---

## 📊 Dataset

**Source**: SMS Spam Collection  
**Size**: ~5,500 SMS messages  
**Labels**: 
- Spam (unwanted promotional/scam messages)
- Ham (legitimate messages)

**Data Split**: 80% training, 20% testing

---

## 🚀 Installation & Usage

### **Prerequisites**
- Python 3.7+
- pip (Python package manager)

### **Step 1: Clone/Download Repository**
```bash
git clone https://github.com/yourusername/sms-spam-detector.git
cd sms-spam-detector
```

### **Step 2: Install Dependencies**
```bash
pip install -r requirements.txt
```

### **Step 3: Run the Web App**
```bash
streamlit run app.py
```

### **Step 4: Access the Application**
- Opens automatically in browser at `http://localhost:8501`
- Type any SMS message in the text box
- Click "Predict" to get spam/not spam classification

---

## 📈 Model Performance

- **Accuracy**: ~97% on test data
- **Precision**: High precision ensures few false positives
- **Algorithm**: Naive Bayes (simple, fast, effective for text classification)

---

## 🔄 Text Preprocessing Pipeline

Every message goes through this cleaning process:

```
Raw Input: "CONGRATULATIONS!!! You WON $1000!!!"
    ↓
Lowercase: "congratulations!!! you won $1000!!!"
    ↓
Tokenize: ['congratulations', '!!!', 'you', 'won', '$1000', '!!!']
    ↓
Remove Punctuation: ['congratulations', 'you', 'won']
    ↓
Remove Stopwords: ['congratulations', 'won']
    ↓
Stemming: ['congratul', 'won']
    ↓
Final Output: "congratul won"
```

---

## 💡 Key Concepts

**TF-IDF (Term Frequency-Inverse Document Frequency)**
- Assigns numerical scores to words based on importance
- Common words get lower scores, distinctive words get higher scores
- Converts text into vectors the model can process

**Naive Bayes**
- Probabilistic classifier based on Bayes' theorem
- Learns: "Which words are associated with spam vs. legitimate messages?"
- Fast, interpretable, and effective for text classification

**Tokenization & Stemming**
- Tokenization: Breaking sentences into individual words
- Stemming: Reducing words to root form (e.g., "running" → "run")
- Both help normalize text and reduce feature dimensionality

---

## 🎓 Learning Outcomes

This project demonstrates:
1. Complete ML pipeline from data to deployment
2. Text preprocessing and NLP fundamentals
3. Feature engineering with TF-IDF
4. Classification model training and evaluation
5. Model serialization and reuse
6. Web app deployment with Streamlit
7. Handling real-world messy text data

---

## 📝 Example Predictions

| Input Message | Prediction | Confidence |
|---|---|---|
| "Win free money now!" | SPAM | High |
| "Meeting at 2pm tomorrow" | NOT SPAM | High |
| "Click here for free prize!!!" | SPAM | High |
| "Your order is confirmed" | NOT SPAM | High |

---

## 🔧 Improvements & Future Work

Possible enhancements:
- Multi-language support with language detection
- Confidence scores showing prediction probability
- Display which words triggered spam classification
- Deploy to cloud (Heroku, AWS, Google Cloud)
- Try advanced algorithms (Random Forest, SVM, Deep Learning)
- Handle edge cases (URLs, phone numbers, emojis)
- Message history and batch processing

---

## 📚 Project Structure

```
sms-spam-detector/
├── app.py                      # Streamlit web application
├── smsspamdetection.ipynb      # Training notebook
├── model.pkl                   # Trained model
├── vectorizer.pkl              # TF-IDF vectorizer
├── spam.csv                    # Dataset
├── requirements.txt            # Dependencies
└── README.md                   # This file
```

---

## 📖 How to Understand This Project

1. **Start with README.md** (this file) for overview
2. **Run app.py** to see it in action
3. **Study app.py** line-by-line to understand deployment
4. **Open smsspamdetection.ipynb** to see training process
5. **Understand the 10-point workflow** for complete clarity

---

## ✍️ Author

**Krunal Deshbhratar** - B.Tech Chemical Engineering, NIT Warangal  
AI/ML Learner | Python Developer | Data Science Enthusiast

---

## 📄 License

This project is open source and available under the MIT License.

---

## 🙏 Acknowledgments

- NLTK documentation and community
- Scikit-learn for ML algorithms
- Streamlit for easy web deployment
- SMS Spam Collection Dataset creators

---

## 📞 Contact & Questions

For questions or suggestions:
- GitHub: [@krunal-dashbharat9](https://github.com/krunal-dashbharat9)


---
**Status**: Active & Maintained
