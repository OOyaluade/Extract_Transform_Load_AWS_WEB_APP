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


#UIC_VW_Assessment_AD6_Rec_All


# In[6]:


df = pd.read_excel("/home/node1/Documents/uic/FilesUsed/UIC_VW_assessment_AD6_Rec_all.xlsx")

# In[7]:


df.info()

# In[8]:


df.columns

# In[9]:


# converting the string to datetime format
df['Info_Date_Assessed'] = pd.to_datetime(df['Info_Date_Assessed'])

# In[10]:


# converting the string to datetime format
df['PPM_Outreach_Activity_Closed_Date'] = pd.to_datetime(df['PPM_Outreach_Activity_Closed_Date'])

# In[11]:


# converting the string to datetime format
df['Summary_Finished_Date'] = pd.to_datetime(df['Summary_Finished_Date'])

# In[12]:


# converting the string to datetime format
df['Summary_Updated_Date'] = pd.to_datetime(df['Summary_Updated_Date'])

# In[13]:


# converting the string to datetime format 
#df['PPM_Assessment_1_Info_Date_Referred']= pd.to_datetime(df['PPM_Assessment_1_Info_Date_Referred'], errors = 'coerce')

# In[14]:


df.dtypes

# In[15]:


df['RIN'].sample(15)

# In[16]:


# Convert RIN to string
df['RIN'] = df['RIN'].astype('str') 

# In[16]:


# Convert RIN to string
df['RIN'] = df['RIN'].astype('str') 

# In[17]:


df['RIN'].sample(15)

# In[18]:


# add leading zeros to Member_RIN
df['RIN'] = df['RIN'].str.zfill(11)

# In[19]:


df['RIN'].sample(15)

# In[20]:


#export file without index column
df.to_excel("UIC_VW_Assessment_AD6_Rec_All.xlsx", index=False)

# In[21]:


# Create a timestamp object
timestamp = pd.Timestamp(datetime.datetime.now())

# Print the timestamp
print(timestamp)

# In[22]:


#the end!

# In[ ]:




# In[ ]:



