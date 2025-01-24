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


#UIC_QA_NLP_Death_Discharge



# In[5]:


df = pd.read_excel("UIC_QA_NLP_Death_Discharge.xlsx")

# In[6]:


df.info()

# In[7]:


df.columns

# In[8]:


# converting the string to datetime format
df['NLP_Date'] = pd.to_datetime(df['NLP_Date'])

# In[9]:


# converting the string to datetime format
df['Log_Facility_Admission_Date'] = pd.to_datetime(df['Log_Facility_Admission_Date'])

# In[10]:


df.dtypes

# In[11]:


df['RIN'].sample(15)

# In[12]:


# Convert RIN to string
df['RIN'] = df['RIN'].astype('str') 

# In[13]:


df['RIN'] = df['RIN'].str.strip()

# In[14]:


# add leading zeros to Member_RIN
df['RIN'] = df['RIN'].str.zfill(11)

# In[15]:


df['RIN'].sample(15)

# In[16]:


df.dtypes

# In[17]:


#export file without index column
df.to_excel("UIC_QA_NLP_Death_Discharge.xlsx", index=False)

# In[18]:


# Create a timestamp object
timestamp = pd.Timestamp(datetime.datetime.now())

# Print the timestamp
print(timestamp)

# In[19]:


#the end!

# In[ ]:




# In[ ]:



