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


#UIC_Report_Dashboard_Pipe_Assess


# In[6]:


df = pd.read_excel("UIC_Report_Dashboard_Pipe_Assess.xlsx")

# In[7]:


df.info()

# In[8]:


df.columns

# In[9]:


# converting the string to datetime format
df['PPM_Assessment_1_Info_Date_Assessed'] = pd.to_datetime(df['PPM_Assessment_1_Info_Date_Assessed'])

# In[10]:


# converting the string to datetime format
df['Pipeline_Dashboard_Date'] = pd.to_datetime(df['Pipeline_Dashboard_Date'])

# In[11]:


# converting the string to datetime format
df['Pipeline_Dashboard_Updated_Date'] = pd.to_datetime(df['Pipeline_Dashboard_Updated_Date'])

# In[12]:


# converting the string to datetime format
df['Summary_DateCreated'] = pd.to_datetime(df['Summary_DateCreated'])

# In[13]:


# converting the string to datetime format
df['Summary_Updated_Date'] = pd.to_datetime(df['Summary_Updated_Date'])

# In[14]:


# converting the string to datetime format
df['Summary_Created_Date'] = pd.to_datetime(df['Summary_Created_Date'])

# In[15]:


# converting the string to datetime format
df['Pipeline_Dashboard_Updated_Date'] = pd.to_datetime(df['Pipeline_Dashboard_Updated_Date'])

# In[16]:


# converting the string to datetime format
df['Pipeline_Dashboard_Created_Date'] = pd.to_datetime(df['Pipeline_Dashboard_Created_Date'])

# In[17]:


# converting the string to datetime format
df['Activity_Closed_Date'] = pd.to_datetime(df['Activity_Closed_Date'])

# In[18]:


# converting the string to datetime format
df['Facility_Admission_Date'] = pd.to_datetime(df['Facility_Admission_Date'])

# In[19]:


# converting the string to datetime format
df['Transition_Delay_Date'] = pd.to_datetime(df['Transition_Delay_Date'])

# In[20]:


# converting the string to datetime format
df['Transition_Date'] = pd.to_datetime(df['Transition_Date'])

# In[21]:


# converting the string to datetime format
df['Assessment_Finished_Date'] = pd.to_datetime(df['Assessment_Finished_Date'])

# In[22]:


# converting the string to datetime format
df['Transition_Delay_Resolved_DT'] = pd.to_datetime(df['Transition_Delay_Resolved_DT'])

# In[23]:


# converting the string to datetime format
df['Member_DOB'] = pd.to_datetime(df['Member_DOB'])

# In[24]:


df.dtypes

# In[25]:


df['Member_RIN'].sample(15)

# In[26]:


# Convert RIN to string
df['Member_RIN'] = df['Member_RIN'].astype('str') 

# In[27]:


df['Member_RIN'].sample(15)

# In[28]:


df['Member_RIN'] = df['Member_RIN'].str.strip()

# In[29]:


# add leading zeros to Member_RIN
df['Member_RIN'] = df['Member_RIN'].str.zfill(9)

# In[30]:


df['Member_RIN'].sample(15)

# In[31]:


df.Pipeline_Dashboard_DaysinPhase.value_counts()                

# In[32]:


#export file without index column
df.to_excel("UIC_Report_Dashboard_Pipe_Assess.xlsx", index=False)

# In[33]:


# Create a timestamp object
timestamp = pd.Timestamp(datetime.datetime.now())

# Print the timestamp
print(timestamp)

# In[34]:


#the end!

# In[ ]:



