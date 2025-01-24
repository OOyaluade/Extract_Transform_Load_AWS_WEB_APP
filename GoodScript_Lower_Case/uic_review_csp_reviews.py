#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import time
import re
import os
import datetime

# In[2]:


os.chdir(r'C:/Users/vwalds/Documents/My Data Sources/')

# In[3]:


import warnings
warnings.filterwarnings('ignore')
warnings.simplefilter('ignore')

# In[4]:


# Grab Current Time Before Running the Code
start = time.time()

# In[5]:


#UIC_Review_CSP_reviews


# In[6]:


df = pd.read_excel("UIC_Review_CSP_reviews.xlsx")

# In[7]:


df.info()

# In[8]:


df.columns

# In[9]:


# converting the string to datetime format
df['Request_Reviewed_On'] = pd.to_datetime(df['Request_Reviewed_On'])

# In[10]:


# converting the string to datetime format
df['Request_Updated_On'] = pd.to_datetime(df['Request_Updated_On'])

# In[11]:


# converting the string to datetime format
df['Date_of_Review'] = pd.to_datetime(df['Date_of_Review'])

# In[12]:


# converting the string to datetime format
df['Request_Created_On'] = pd.to_datetime(df['Request_Created_On'])

# In[13]:


df.dtypes

# In[14]:


#export file without index column
df.to_excel("UIC_Review_CSP_reviews.xlsx", index=False)

# In[15]:


# Create a timestamp object
timestamp = pd.Timestamp(datetime.datetime.now())

# Print the timestamp
print(timestamp)

# In[16]:


#the end!

# In[ ]:




# In[ ]:



