'''
 # @ File Name: scrape_zotero_abstracts
 # @ Author: Alexander Karl
 # @ Create Time: 2025-01-114
 # @ Description: Clean data andrun LDA on article abstracts
 '''

# 0. Overhead
import pickle
from gensim.corpora.dictionary import Dictionary
import nltk
# nltk.download('punkt_tab')
# nltk.download('stopwords')
# nltk.download('wordnet')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
import re
from nltk.stem.wordnet import WordNetLemmatizer

with open('raw_article_data.pkl', 'rb') as handle:
    article_data = pickle.load(handle)    # list of {'title':str, 'abstract=str, doi_url=str, NODOI=int}, len=328

# create a corpus of all article abstracts
abstracts = [article['abstract_content'] for article in article_data]

# remove punctuation and stopwords
abstracts = [re.sub(r'[^a-zA-Z]', ' ', abstract) for abstract in abstracts]
tokenized_abstracts = [word_tokenize(abstract.lower()) for abstract in abstracts]
tokenized_abstracts = [[word for word in abstract if word not in stopwords.words('english') and not word.isdigit()] for abstract in tokenized_abstracts]
# lemmatize
tokenized_abstracts = [" ".join(WordNetLemmatizer().lemmatize(word) for word in abstract.split()) for abstract in abstracts]
# stem words

for i in range(5):
    print("Abstract ", i, ": ", tokenized_abstracts[i][0:100])





# dictionary = Dictionary(tokenized_abstracts)
# corpus = [dictionary.doc2bow(abstract) for abstract in tokenized_abstracts]

print('finished')






