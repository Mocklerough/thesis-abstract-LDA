'''
 # @ File Name: scrape_zotero_abstracts
 # @ Author: Alexander Karl
 # @ Create Time: 2025-01-114
 # @ Description: Clean data andrun LDA on article abstracts
 '''

# 0. Overhead
import pickle
from gensim.corpora.dictionary import Dictionary
from nltk.tokenize import word_tokenize

with open('raw_article_data.pkl', 'rb') as handle:
    article_data = pickle.load(handle)    # list of {'title':str, 'abstract=str, doi_url=str, NODOI=int}, len=328

# create a corpus of all article abstracts
abstract_list = [article['abstract_content'] for article in article_data]
for i in range(5):
    print(abstract_list[i][0:30])