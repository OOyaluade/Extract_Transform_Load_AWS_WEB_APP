#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import time
import re
import os
import datetime
import warnings
warnings.filterwarnings('ignore')
warnings.simplefilter('ignore')

# In[2]:


os.chdir(r'C:/Users/vwalds/Documents/My Data Sources/')

# In[3]:


# Grab Current Time Before Running the Code
start = time.time()

# In[4]:


#UIC_report_CAST

# In[5]:


df = pd.read_excel("UIC_report_CAST.xlsx")

# In[6]:


df.info()

# In[7]:


df.columns

# In[8]:


# converting the string to datetime format
df['CAST_Created_On'] = pd.to_datetime(df['CAST_Created_On'])

# In[9]:


# converting the string to datetime format
df['CAST_Updated_Date'] = pd.to_datetime(df['CAST_Updated_Date'])

# In[10]:


# converting the string to datetime format
df['CAST_Updated_On'] = pd.to_datetime(df['CAST_Updated_On'])

# In[11]:


df.dtypes

# In[12]:


#export file without index column
df.to_excel("UIC_report_CAST.xlsx", index=False)

# In[13]:


# Create a timestamp object
timestamp = pd.Timestamp(datetime.datetime.now())

# Print the timestamp
print(timestamp)

# In[14]:


#the end!

# In[ ]:




# In[ ]:



