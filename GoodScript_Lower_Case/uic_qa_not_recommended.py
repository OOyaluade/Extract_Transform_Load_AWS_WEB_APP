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


#UIC_QA_Not_Recommended


# In[6]:


df = pd.read_excel("UIC_QA_Not_Recommended.xlsx")

# In[7]:


df.info()

# In[8]:


df.columns

# In[9]:


# converting the string to datetime format
df['Info_Date_Assessed'] = pd.to_datetime(df['Info_Date_Assessed'])

# In[10]:


# converting the string to datetime format
df['Activity_Date_Started'] = pd.to_datetime(df['Activity_Date_Started'])

# In[11]:


# converting the string to datetime format
df['Admission_Date'] = pd.to_datetime(df['Admission_Date'])

# In[12]:


# converting the string to datetime format
df['Not_Proceeding_FX_Event_Date'] = pd.to_datetime(df['Not_Proceeding_FX_Event_Date'])

# In[13]:


# converting the string to datetime format 
#df['PPM_Assessment_1_Info_Date_Referred']= pd.to_datetime(df['PPM_Assessment_1_Info_Date_Referred'], errors = 'coerce')

# In[14]:


df.dtypes

# In[15]:


#export file without index column
df.to_excel("UIC_QA_Not_Recommended.xlsx", index=False)

# In[16]:


# Create a timestamp object
timestamp = pd.Timestamp(datetime.datetime.now())

# Print the timestamp
print(timestamp)

# In[17]:


#the end!

# In[ ]:




# In[ ]:



