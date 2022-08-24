#!/usr/bin/env python
# coding: utf-8

# In[59]:


import pandas as pd


# In[60]:


import numpy as np


# In[68]:

class DataHandling:

    
    def read_file(ticker):
        ticker = ticker.upper()
        df = pd.read_csv(f"{ticker}.csv")
        
        return df
    
    
    def clean_data(df):
        df = df.apply(lambda x: x.str.replace(',', ''))
        df = df.drop([0, 28, 29, 66, 67, 96, 97, 98, 99])
        df = df.replace("%","", regex=True)
        df = df.replace("\)","", regex=True)
        df = df.replace("\(","", regex=True)
        df = df.replace("- -", np.nan)
        df = df.set_index("ROIC.AI | AZO")
        df = df.fillna(0)
        
        return df





