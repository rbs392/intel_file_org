import re

import nltk
from nltk import word_tokenize

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

import pandas as pd
import os
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from gensim.models import LdaModel, Phrases
from gensim.corpora import Dictionary
from pprint import pprint

stop_words = stopwords.words('english')
lemmatizer = WordNetLemmatizer()

docs = []
for f_name in os.listdir("./data/payslips"):
    print(f_name)
    tokens = word_tokenize("".join(pd.read_excel(f"./data/payslips/{f_name}").apply(lambda x: str(x).lower()).values))
    print(tokens)
    lemmatized_tokens = [
        lemmatizer.lemmatize(re.sub("\W", " ", token))
        for token in tokens
        if token not in stop_words
           and len(token) > 1
           and token not in ('nan', 'dtype')
           and (re.search("[0-9]", token) is None)
    ]
    docs.append(lemmatized_tokens)

bigram = Phrases(docs, min_count=2)
for idx in range(len(docs)):
    for token in bigram[docs[idx]]:
        if '_' in token:
            docs[idx].append(token)

# print(docs)
dictionary = Dictionary(docs)
corpus = [dictionary.doc2bow(doc) for doc in docs]

# Set training parameters.
num_topics = 2
chunksize = 2000
passes = 20
iterations = 400
eval_every = None  # Don't evaluate model perplexity, takes too much time.

# Make a index to word dictionary.
temp = dictionary[0]  # This is only to "load" the dictionary.
id2word = dictionary.id2token

model = LdaModel(
    corpus=corpus,
    id2word=id2word,
    chunksize=chunksize,
    alpha='auto',
    eta='auto',
    iterations=iterations,
    num_topics=num_topics,
    passes=passes,
    eval_every=eval_every
)

top_topics = model.top_topics(corpus)

pprint(top_topics)

# print(model.inference([docs[0]]))
