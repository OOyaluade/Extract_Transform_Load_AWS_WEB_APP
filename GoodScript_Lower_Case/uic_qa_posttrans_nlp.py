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


#UIC_QA_PostTrans_NLP


# In[5]:


df = pd.read_excel("UIC_QA_PostTrans_NLP.xlsx")

# In[6]:


df.info()

# In[7]:


df.columns

# In[8]:


# converting the string to datetime format
df['Not_Proceeding_Created_Date'] = pd.to_datetime(df['Not_Proceeding_Created_Date'])

# In[9]:


# converting the string to datetime format
df['Transition_Discharge_Date'] = pd.to_datetime(df['Transition_Discharge_Date'])

# In[10]:


# converting the string to datetime format
df['FX_Event_Date'] = pd.to_datetime(df['FX_Event_Date'])

# In[11]:


# converting the string to datetime format
df['Activity_Closed_Date'] = pd.to_datetime(df['Activity_Closed_Date'])

# In[12]:


df.dtypes

# In[13]:


#export file without index column
df.to_excel("UIC_QA_PostTrans_NLP.xlsx", index=False)

# In[14]:


# Create a timestamp object
timestamp = pd.Timestamp(datetime.datetime.now())

# Print the timestamp
print(timestamp)

# In[15]:


#the end!

# In[ ]:




# In[ ]:



