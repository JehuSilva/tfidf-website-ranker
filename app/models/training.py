# packages
import os
import pickle
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# Skip future warnings
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


current_dir = os.path.dirname(os.path.realpath(__file__))
# Reading articles
try:
    print('Loading articles...')
    df1 = pd.read_csv(current_dir+"/data/articles1.csv")
    df2 = pd.read_csv(current_dir+"/data/articles2.csv")
    df3 = pd.read_csv(current_dir+"/data/articles3.csv")
    print('Articles loaded')
except FileNotFoundError:
    raise Exception('Files not found')

# Selecting the articles used for training
df = pd.concat([df1, df2, df3])['content']
# msk = np.random.rand(len(df)) < 0.8
# train = df[msk]
# test = df[~msk]

print(f'The model will be trained with {len(df)} articles')



# tfidf calulation
vectorizer = TfidfVectorizer(
    max_df=0.7,             # drop words that occur in more than X percent of documents (stop words)
    stop_words='english',   # remove stop words
    lowercase=True,         # Convert everything to lower case 
    use_idf=True,           # Use idf
    norm=u'l2',             # Normalization
    smooth_idf=True,        # Prevents divide-by-zero errors
    encoding='utf-8'        # If bytes or files are given to analyze, this encoding is used to decode.
)
print('Training the model...')
tf_idf = vectorizer.fit_transform(df)
print('Model trained')
# Save objects on filesystem
print('Saving objects on filesystem')
pickle.dump(vectorizer, open(current_dir+'/vectorizer', 'wb')) 
pickle.dump(tf_idf, open(current_dir+'/tf_idf', 'wb'))
print('Done!')