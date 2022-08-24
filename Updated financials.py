#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cleaningData
import pandas as pd
import numpy as np


# In[2]:


ticker = input()


# In[3]:


df = cleaningData.DataHandling.read_file(ticker)


# In[4]:


df = cleaningData.DataHandling.clean_data(df)


# In[5]:


df


# In[ ]:




