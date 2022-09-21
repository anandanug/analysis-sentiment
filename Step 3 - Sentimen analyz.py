#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import some libraries

import pandas as pd
pd.options.mode.chained_assignment = None
import numpy as np
seed = 0
np.random.seed(seed)
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style = 'whitegrid')

#!pip install twint
#import twint
import nest_asyncio
nest_asyncio.apply()


import datetime as dt
import re
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

#pip install Sastrawi
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
#from wordcloud import WordCloud

#from keras.preprocessing.text import Tokenizer
#from keras_preprocessing.sequence import pad_sequences
#from sklearn.model_selection import train_test_split
#from sklearn.metrics import accuracy_score
#from keras.models import Sequential
#from keras.layers import Embedding, Dense, Dropout, LSTM
#from keras.optimizers import Adam, RMSprop, SGD
#from keras.callbacks import EarlyStopping
#from keras.wrappers.scikit_learn import KerasClassifier
#from sklearn.model_selection import GridSearchCV
#from mlxtend.plotting import plot_confusion_matrix
#from sklearn.metrics import confusion_matrix


# In[2]:


df = pd.read_csv('cleaned_2019.csv', low_memory = False)


# In[3]:


df= df.iloc[:100,:] 


# In[4]:


# Some functions for preprocessing text

def cleaningText(text):
    text = re.sub(r'@[A-Za-z0-9]+', '', text) # remove mentions
    text = re.sub(r'#[A-Za-z0-9]+', '', text) # remove hashtag
    text = re.sub(r'RT[\s]', '', text) # remove RT
    text = re.sub(r"http\S+", '', text) # remove link
    text = re.sub(r'[0-9]+', '', text) # remove numbers

    text = text.replace('\n', ' ') # replace new line into space
    text = text.translate(str.maketrans('', '', string.punctuation)) # remove all punctuations
    text = text.strip(' ') # remove characters space from both left and right text
    return text

def casefoldingText(text): # Converting all the characters in a text into lower case
    text = text.lower() 
    return text

def tokenizingText(text): # Tokenizing or splitting a string, text into a list of tokens
    text = word_tokenize(text) 
    return text

def filteringText(text): # Remove stopwors in a text
    listStopwords = set(stopwords.words('indonesian'))
    filtered = []
    for txt in text:
        if txt not in listStopwords:
            filtered.append(txt)
    text = filtered 
    return text

def stemmingText(text): # Reducing a word to its word stem that affixes to suffixes and prefixes or to the roots of words
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()
    text = [stemmer.stem(word) for word in text]
    return text

def toSentence(list_words): # Convert list of words into sentence
    sentence = ' '.join(word for word in list_words)
    return sentence


# In[5]:


import swifter


# In[6]:


df['cleaningText'] = df['text'].swifter.apply(cleaningText)


# In[7]:


df['casefoldingText'] = df['cleaningText'].swifter.apply(casefoldingText)


# In[8]:


df['tokenizingText'] = df['casefoldingText'].swifter.apply(tokenizingText)


# In[9]:


df['filteringText'] = df['tokenizingText'].swifter.apply(filteringText)


# In[10]:


df['stemmingText'] = df['filteringText'].swifter.apply(stemmingText)


# In[11]:


df.drop_duplicates(subset = 'text', inplace = True)


# In[12]:


df.head(1)


# # Tentukan Polaritas Sentimen Tweet dengan Indonesia Sentiment Lexicon¶

# In[13]:


# Determine sentiment polarity of tweets using indonesia sentiment lexicon (source : https://github.com/fajri91/InSet)

# Loads lexicon positive and negative data
lexicon_positive = dict()
import csv
with open('lexicon_positive.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        lexicon_positive[row[0]] = int(row[1])

lexicon_negative = dict()
import csv
with open('lexicon_negative.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        lexicon_negative[row[0]] = int(row[1])
        
# Function to determine sentiment polarity of tweets        
def sentiment_analysis_lexicon_indonesia(text):
    #for word in text:
    score = 0
    for word in text:
        if (word in lexicon_positive):
            score = score + lexicon_positive[word]
    for word in text:
        if (word in lexicon_negative):
            score = score + lexicon_negative[word]
    polarity=''
    if (score > 0):
        polarity = 'positive'
    elif (score < 0):
        polarity = 'negative'
    else:
        polarity = 'neutral'
    return score, polarity


# In[14]:


results = df['stemmingText'].swifter.apply(sentiment_analysis_lexicon_indonesia)
results = list(zip(*results))
df['polarity_score'] = results[0]
df['polarity'] = results[1]
print(df['polarity'].value_counts())


# In[17]:


df.head(10)


# In[ ]:




