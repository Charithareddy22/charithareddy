import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# download required data (run once)
nltk.download('stopwords')

# Task 1: Clean and Process
def clean_and_process(sentence):
    sentence = sentence.lower()
    sentence = re.sub(r'[^a-z\s]', '', sentence)
    tokens = sentence.split()
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    stemmer = PorterStemmer()
    tokens = [stemmer.stem(word) for word in tokens]
    return tokens

# test
print(clean_and_process("NLTK is AMAZING!!! This is a simple test."))
