#!/usr/bin/env python
# coding: utf-8

# In[5]:


import requests 


# In[6]:


response=requests.get('https://api.covid19api.com/summary').text


# In[9]:


response


# In[10]:


import json


# In[11]:


response_info = json.loads(response)


# In[181]:


response_info


# In[12]:


type(response_info)


# In[13]:


response_info.keys()


# In[14]:


response_info.values()


# In[18]:


INFO_list = list(response_info.keys())
print(INFO_list)


# In[34]:



   


# In[29]:





# In[ ]:




