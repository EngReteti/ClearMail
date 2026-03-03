# ClearMail 📧
**ClearMail** is a globally-focused NLP binary classifier designed to distinguish between "Spam" and "Ham" (legitimate) messages. Built with Python and Scikit-Learn, it features a Flask API for real-time inference.

## 🚀 Features
- **Text Preprocessing:** Tokenization, stop-word removal, and lemmatization via NLTK.
- **Vectorization:** TF-IDF (Term Frequency-Inverse Document Frequency).
- **Classification:** Multinomial Naive Bayes.
- **Web Interface:** A simple Flask API for instant text classification.

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Libraries:** Pandas, Scikit-Learn, NLTK
- **Deployment:** Flask (Web Framework)
- **Environment:** Developed on Android via Termux

## 📂 Project Structure
- `data/`: Raw and processed email datasets.
- `models/`: Saved trained model objects (`.pkl`).
- `src/`: Backend logic and preprocessing functions.
- `app.py`: Flask server entry point.

## 📥 Installation & Setup
1. **Clone the repository:**
   ```bash
   git clone https://github.com/EngReteti/ClearMail.git
   cd ClearMail
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
