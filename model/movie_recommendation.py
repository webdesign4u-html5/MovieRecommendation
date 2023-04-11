#!/usr/bin/env python
# coding: utf-8

# In[19]:


import numpy as np
import pandas as pd


# In[ ]:





# In[20]:


movies= pd.read_csv('data/movies.csv')
credits= pd.read_csv('data/credits.csv')
movies.head(2)


# In[21]:


dataset = movies.merge(credits, on='title')
dataset.head(2)


# In[22]:


dataset = dataset[['movie_id','title','tagline','overview','genres','keywords','cast','crew','popularity','release_date']]


# In[23]:


dataset.duplicated().sum()
dataset.head(1)


# In[24]:


dataset['release_date']= dataset['release_date'].apply(lambda x: str(x).split("-")[0] if len(str(x).split("-")) >= 3 else "")


# In[25]:


dataset.head(2)


# In[26]:


import ast


# In[27]:


def convert(obj):
    L=[]
    for i in ast.literal_eval(obj):
        L.append(i['name'])
    return L


# In[28]:


dataset['genres']=dataset['genres'].apply(convert)


# In[29]:


popular = dataset[['movie_id','title','genres','release_date','popularity']]


# In[30]:


popular.head()


# In[31]:


popular = popular.sort_values('popularity', ascending=False)


# In[32]:


def byGenres(genre):
    counter=0
    L=[]
    for row in popular.iterrows():
        if counter != 6:
            for gen in row[1].genres:
                if gen ==genre:
                    L.append(row[1].title)
                    counter+=1
                    break
        else:
            break
    return L


# In[33]:


byGenres("Animation")


# In[34]:


popular['genres'] = popular['genres'].apply(lambda x: "$".join(x))


# In[35]:


popular.head()


# In[36]:


import sqlite3
import sqlalchemy
engine = sqlalchemy.create_engine('sqlite:///popular.sqlite')
popular.to_sql('popular', engine)


# In[ ]:


engine = sqlalchemy.create_engine('sqlite:///movies.sqlite')
dataset['genres'] = dataset['genres'].apply(lambda x: "$".join(x))
dataset['keywords'] = dataset['keywords'].apply(lambda x: "$".join(x))
dataset.to_sql('movies', engine)


# In[ ]:


def byYear(year):
    counter=0
    L=[]
    for row in popular.iterrows():
        if row[1].release_date==year:
            if counter!=6:
                L.append(row[1].title)
                counter=counter+1
            else:
                break
    return L
byYear("2018")


# In[ ]:




