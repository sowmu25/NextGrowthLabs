# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 12:28:55 2022

@author: sowmu
"""

import streamlit as st
import pandas as pd
import nltk
nltk.download('all')
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
import re
from textblob import TextBlob
from nltk.corpus import stopwords
#from textblob import Word
from nltk.stem import WordNetLemmatizer

wordnet=WordNetLemmatizer()

st.write("Chrome Review Vs Rating")


def clean_text(a):
    text=re.sub('[^A-za-z0-9]',' ',a)
    text=text.lower()
    text=text.split(' ')
    text = [wordnet.lemmatize(word) for word in text if word not in (stopwords.words('english'))]
    text = ' '.join(text)
    return text

data_file = st.file_uploader("Upload CSV",type=["csv"])
if data_file is not None:
    #file_details = {"filename":data_file.name, "filetype":data_file.type,"filesize":data_file.size}
    #st.write(file_details)
    test = pd.read_csv(data_file,encoding="ISO-8859-1")
    chrome2=test.iloc[0:5000,[0,2,3]]

    
    chrome2['Text'].apply(clean_text)
    chrome2['senti_polar']=chrome2['Text'].apply(lambda x: TextBlob(x).sentiment.polarity )
    chrome2['sentiment'] = chrome2['senti_polar'].apply(lambda x : 'Positive' if x > 0 else ('Negative' if x<0 else 'Neutral'))
    chrome2['sentiment'] = chrome2['sentiment'].replace({'Negative': -1,'Positive': 1, 'Neutral': 0})


    filter=chrome2.loc[(chrome2.senti_polar>0) & (chrome2.Star<3)]
    new = test['ID'].isin(filter['ID'])
    st.write("Success:Semantics of review text that does not match rating")
    st.write(test[new])
  
else:
    st.write("Upload a correct File")
    
