#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cleaningData
import pandas as pd
import numpy as np


# In[2]:


df = cleaningData.DataHandling.read_file('azo')


# df = df.apply(lambda x: x.str.replace(',', ''))
# df = df.drop([0, 28, 29, 66, 67, 96, 97, 98, 99])
# df = df.replace("%","", regex=True)
# df = df.replace("\)","", regex=True)
# df = df.replace("\(","", regex=True)
# df = df.replace("- -", np.nan)
# df = df.set_index("ROIC.AI | AZO")
# df = df.fillna(0)

# In[3]:


df = cleaningData.DataHandling.clean_data(df)


# In[4]:


df


# In[16]:


df.astype(float)


# In[ ]:




