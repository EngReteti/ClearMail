# SentinelMail 📧
**SentinelMail** is a lightweight NLP-based binary classifier designed to distinguish between "Spam" and "Ham" (legitimate) emails. Built with Python and Scikit-Learn, it features a Flask API for real-time inference.

## 🚀 Features
- **Text Preprocessing:** Tokenization, stop-word removal, and lemmatization via NLTK.
- **Vectorization:** TF-IDF (Term Frequency-Inverse Document Frequency) approach.
- **Classification:** Multinomial Naive Bayes (optimized for text).
- **Web Interface:** A simple Flask API for instant text classification.

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Libraries:** Pandas, Scikit-Learn, NLTK
- **Deployment:** Flask (Web Framework)
- **Environment:** Developed on Android via Termux

## 📂 Project Structure
- `data/`: Contains the email dataset.
- `models/`: Saved model objects (`.pkl`).
- `src/`: Backend logic and preprocessing functions.
- `app.py`: Flask server.

## 📥 Installation & Setup
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YourUsername/SentinelMail.git](https://github.com/YourUsername/SentinelMail.git)
   cd SentinelMail

