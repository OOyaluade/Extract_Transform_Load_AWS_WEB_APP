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


#UIC_VW_all_transitions_simple

# In[6]:


df = pd.read_excel("UIC_VW_all_transitions_simple.xlsx")

# In[7]:


df.info()

# In[8]:


df.columns

# In[9]:


# converting the string to datetime format
df['Activity_Closed_Date'] = pd.to_datetime(df['Activity_Closed_Date'])

# In[10]:


# converting the string to datetime format
df['Activity_Date_Started'] = pd.to_datetime(df['Activity_Date_Started'])

# In[11]:


# converting the string to datetime format
df['Transition_Discharge_Date'] = pd.to_datetime(df['Transition_Discharge_Date'])

# In[12]:


# converting the string to datetime format
df['Transition_Finished_Date'] = pd.to_datetime(df['Transition_Finished_Date'])

# In[13]:


df.dtypes

# In[14]:


#export file without index column
df.to_excel("UIC_VW_all_transitions_simple.xlsx", index=False)

# In[15]:


# Create a timestamp object
timestamp = pd.Timestamp(datetime.datetime.now())

# Print the timestamp
print(timestamp)

# In[16]:


#the end!

# In[ ]:



