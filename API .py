#!/usr/bin/env python
# coding: utf-8

# In[64]:


#Importing Libraries 

import requests
import pandas as pd


# In[65]:


#Acess keys
api_key = {'Authorization': 'Bearer 16RiWJdrb9X6mleqeDrF'}
api_url = 'https://the-one-api.dev/v2/movie'


# In[66]:


# making the API call and storing the json file in a variable
response = requests.get(api_url, headers = api_key)
lor_data = response.json()


# In[78]:


#Inspecting the data

lor_data.keys()


# In[77]:


lor_data['docs']


# In[80]:


# Converting lor_data['docs'] into a dataframe

df = pd.DataFrame(lor_data['docs'])

df

