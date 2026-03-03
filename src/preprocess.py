import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re

def clean_text(text):
    text = re.sub(r'[^a-zA-Z]', ' ', text).lower()
    words = text.split()
    return " ".join(words)

if __name__ == "__main__":
    sample = "Hello!!! This is a SPAM email 123."
    print(f"Original: {sample}")
    print(f"Cleaned: {clean_text(sample)}")
