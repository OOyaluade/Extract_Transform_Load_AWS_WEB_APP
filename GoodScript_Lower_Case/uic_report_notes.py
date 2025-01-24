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


import warnings
warnings.filterwarnings('ignore')
warnings.simplefilter('ignore')

# In[3]:


os.chdir(r'C:/Users/vwalds/Documents/My Data Sources/')

# In[4]:


# Grab Current Time Before Running the Code
start = time.time()

# In[5]:


#UIC_report_notes

# In[6]:


df = pd.read_excel("UIC_report_notes.xlsx")

# In[7]:


df.info()

# In[8]:


df.columns

# In[9]:


# converting the string to datetime format
df['Note_Date_Created'] = pd.to_datetime(df['Note_Date_Created'])

# In[10]:


# converting the string to datetime format
df['Note_Updated_Date'] = pd.to_datetime(df['Note_Updated_Date'])

# In[11]:


# converting the string to datetime format
df['Note_Date_Updated'] = pd.to_datetime(df['Note_Date_Updated'])

# In[12]:


# converting the string to datetime format
df['Note_Date_Of_Activity'] = pd.to_datetime(df['Note_Date_Of_Activity'])

# In[13]:


df.dtypes

# In[14]:


#export file without index column
df.to_excel("UIC_report_notes.xlsx", index=False)

# In[15]:


# Create a timestamp object
timestamp = pd.Timestamp(datetime.datetime.now())

# Print the timestamp
print(timestamp)

# In[16]:


#the end!

# In[ ]:



