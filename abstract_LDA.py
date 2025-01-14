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
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
import re

with open('raw_article_data.pkl', 'rb') as handle:
    article_data = pickle.load(handle)    # list of {'title':str, 'abstract=str, doi_url=str, NODOI=int}, len=328

# create a corpus of all article abstracts
abstracts = [article['abstract_content'] for article in article_data]
# remove punctuation and stopwords
abstracts = [re.sub(r'[^a-zA-Z]', ' ', abstract) for abstract in abstracts]
abstracts = " ".join([word for word in abstracts if word not in stopwords.words('english') and not word.isdigit()])
abstracts = ''.join([word for word in abstracts if word not in set(string.punctuation)])


# tokenise to prepare the corpus
tokenized_abstracts = [word_tokenize(abstract.lower()) for abstract in abstracts]


print(tokenized_abstracts[0])
dictionary = Dictionary(tokenized_abstracts)
corpus = [dictionary.doc2bow(abstract) for abstract in tokenized_abstracts]







