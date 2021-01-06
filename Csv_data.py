#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests 


# In[2]:


response=requests.get('https://api.covid19api.com/summary').text


# In[3]:


response


# In[4]:


import json


# In[5]:


response_info = json.loads(response)


# In[6]:


response_info


# In[7]:


type(response_info)


# In[8]:


response_info['Countries']


# In[10]:


country_list = []
for country_info in response_info['Countries']:
    country_list.append([country_info['Country'], country_info['TotalConfirmed']])


# In[11]:


country_list


# In[12]:


import pandas as pd
country_df = pd.DataFrame(data=country_list, columns=['Country', 'Total_Confirmed'])
country_df.head(100)


# In[13]:


country_df.to_csv('Country')

