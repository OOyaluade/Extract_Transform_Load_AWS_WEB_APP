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


# os.chdir(r'C:/Users/vwalds/Documents/My Data Sources/')

# In[4]:


# Grab Current Time Before Running the Code
start = time.time()

# In[5]:


#UIC_VW_Transitions_Active


# In[6]:


df = pd.read_excel("/home/node1/Documents/uic/FilesUsed/UIC_VW_Transitions_Active.xlsx")

# In[7]:


df.info()

# In[8]:


df.columns

# In[9]:


# converting the string to datetime format
df['Transition_Date'] = pd.to_datetime(df['Transition_Date'])

# In[10]:


# converting the string to datetime format
df['Activity_Closed_Date'] = pd.to_datetime(df['Activity_Closed_Date'])

# In[11]:


# converting the string to datetime format
df['FX_Event_Date'] = pd.to_datetime(df['FX_Event_Date'])

# In[12]:


# converting the string to datetime format
df['Activity_Assigned_QM_Date'] = pd.to_datetime(df['Activity_Assigned_QM_Date'])

# In[13]:


# converting the string to datetime format
df['Activity_Last_QM_Visit_Date'] = pd.to_datetime(df['Activity_Last_QM_Visit_Date'])

# In[14]:


df.dtypes

# In[15]:


df['PPM_Member_RIN'].sample(10)

# In[16]:


# Convert RIN to string
df['PPM_Member_RIN'] = df['PPM_Member_RIN'].astype('str') 

# In[16]:




# In[17]:


df['PPM_Member_RIN'] = df['PPM_Member_RIN'].str.strip()

# In[18]:


# add leading zeros to Member_RIN
df['PPM_Member_RIN'] = df['PPM_Member_RIN'].str.zfill(9)

# In[19]:


df['PPM_Member_RIN'].sample(15)

# In[20]:


#export file without index column
df.to_excel("UIC_VW_Transitions_Active.xlsx", index=False)

# In[21]:


# Create a timestamp object
timestamp = pd.Timestamp(datetime.datetime.now())

# Print the timestamp
print(timestamp)

# In[22]:


#the end!

# In[ ]:



