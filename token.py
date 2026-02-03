import nltk
nltk.download('punkt_tab')
text="I Love Pizza!"
tokens=nltk.word_tokenize(text)
print(tokens)