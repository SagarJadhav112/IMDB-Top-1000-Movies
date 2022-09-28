#!/usr/bin/env python
# coding: utf-8

# In[39]:


import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint

headers = {"Accept-Language": "en-US,en;q=0.5"}


movie = []
year = []
time=[]
rating=[]
votes = []
gross = []

pages = np.arange(1,1000,100)
for page in pages:
    page = requests.get("https://www.imdb.com/search/title/?groups=top_1000&sort=user_rating,desc&count=100&start="+str(page)+"&ref_=adv_nxt")
    soup = BeautifulSoup(page.text, 'html.parser')
    movie_data = soup.findAll('div', attrs = {'class': 'lister-item mode-advanced'})
    sleep(randint(3,7))
    for i in movie_data:
        name = store.h3.a.text
        movie.append(name)
        
        year_of_release = i.h3.find('span', class_ = "lister-item-year text-muted unbold").text
        year.append(year_of_release)
        
        runtime = i.p.find("span", class_ = 'runtime').text
        time.append(runtime)
        
        rate = i.find('div', class_ = "inline-block ratings-imdb-rating").text.replace('\n', '')
        rating.append(rate)
        
        
        value = i.find_all('span', attrs = {'name': "nv"})
        
        vote = value[0].text
        votes.append(vote)
    
        grosses = value[1].text if len(value)>1 else 'N/A'
        gross.append(grosses)
        
       
        
        
        


# In[44]:


movies=pd.DataFrame({'Name of Movies':movie,
                     'Release of Year':year,
                     'Watch Time':time,
                     'Rating of Movies':rating,
                     'Votes of movies':votes,
                     'Gross of Movies':gross})


# In[45]:


movies


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[75]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




