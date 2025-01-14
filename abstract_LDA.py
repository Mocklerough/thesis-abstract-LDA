'''
 # @ File Name: scrape_zotero_abstracts
 # @ Author: Alexander Karl
 # @ Create Time: 2025-01-114
 # @ Description: Clean data andrun LDA on article abstracts
 '''

# 0. Overhead
import pickle
from gensim.corpora.dictionary import Dictionary
# import nltk
# nltk.download('punkt_tab')
# nltk.download('stopwords')
# nltk.download('wordnet')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re
from nltk.stem.wordnet import WordNetLemmatizer
import gensim
from gensim.models.tfidfmodel import TfidfModel

with open('raw_article_data.pkl', 'rb') as handle:
    article_data = pickle.load(handle)    # list of {'title':str, 'abstract=str, doi_url=str, NODOI=int}, len=328

# create a corpus of all article abstracts
abstracts = [article['abstract_content'] for article in article_data]

# remove punctuation and stopwords
abstracts = [re.sub(r'[^a-zA-Z]', ' ', abstract) for abstract in abstracts]
abstracts = [word_tokenize(abstract.lower()) for abstract in abstracts]
abstracts = [[word for word in abstract if word not in stopwords.words('english') and not word.isdigit()] for abstract in abstracts]
# lemmatize
abstracts = [" ".join(WordNetLemmatizer().lemmatize(word) for word in abstract) for abstract in abstracts]
abstracts = [word_tokenize(abstract.lower()) for abstract in abstracts]

# create dictionary of words used in all abstracts
dictionary = Dictionary(abstracts)
dictionary.filter_extremes(no_below=2, keep_n=50000)
corpus = [dictionary.doc2bow(abstract) for abstract in abstracts]

# 2) LDA model & fine-tuning

# run LDA model
# ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics = 3, id2word=dictionary, passes=15)
# check topics
# topics = ldamodel.print_topics(num_words=4)
# for topic in topics:
#     print(topic)
# Topic 0: llm, human, study, ai
# Topic 1: llm, task, science, text
# Topic 2: human, learnig, ai, machine

# that's an ok starting point, lets play around with the num_topics to see what happens
# with open("lda_models_topics.txt", "w") as file:
#     for i in range(2,9): 
#         ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics = i, id2word=dictionary, passes=15)
#         topics = ldamodel.print_topics(num_words=5)
#         file.write(f"Model with {i} Topics\n")
#         for topic_num, topic in topics:
#             words = [word.split("*")[1].strip('"') for word in topic.split(" + ")]
#             formatted_words = ', '.join([f'"{word}"' for word in words])
#             file.write(f"topic {formatted_words}\n")
#         file.write("\n")
# these topics are fairly undifferentiated, especially dominated by terms like "ai", "llm", etc which appear in very nearly every abstract. 
# I'll need to adjust the dict to weight these common terms lower so they don't dominate the results


# 3) tf-idf
# Termfrequency-inversedocumentfrequency can be used to down-weight common words, letting other words have a bigger impact on the LDA

tfidf = TfidfModel(corpus)

tfidf_ldamodel = gensim.models.ldamodel.LdaModel(tfidf, num_topics = 4, id2word=dictionary, passes=15)
tfidf_topics = tfidf_ldamodel.print_topics(num_words=5)
print("YYYYYYYYYYY")
print(tfidf_topics)
for topic_num, topic in tfidf_topics:
    print(topic)
    print("xxxxx------xxxxx")

print('finished')
print('XZZZZZZZZZZZZZ')









