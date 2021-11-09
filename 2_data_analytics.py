from extensions.database import collect_data
import pandas as pd
import unicodedata
import unidecode
import numpy as np


# obtain data from the database
df = collect_data()

def strip_accents(text):
    return ''.join(c for c in unicodedata.normalize('NFKD', text) if unicodedata.category(c) != 'Mn')

city_ = []
title_ = []

for city in df['location']:
    city_.append(strip_accents(city)) 
    
for title in df['title']:
    title_.append(strip_accents(title)) 

df['location'] = city_
df['title'] = title_

df = df.drop(df[df['price'] > np.mean(df['price']) + 3*np.std(df['price'])].index)

df

df.to_csv('/database/database_tabular.csv', encoding="utf-8") 