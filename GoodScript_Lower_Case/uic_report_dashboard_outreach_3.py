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


#UIC_Report_Dashboard_Outreach_3

# In[6]:


df = pd.read_excel("UIC_Report_Dashboard_Outreach_3.xlsx")

# In[7]:


df.info()

# In[8]:


df.columns

# In[9]:


# converting the string to datetime format
df['Activity_Date_Created'] = pd.to_datetime(df['Activity_Date_Created'])

# In[10]:


# converting the string to datetime format
df['Attempt_Creation_Date'] = pd.to_datetime(df['Attempt_Creation_Date'])

# In[11]:


# converting the string to datetime format
df['Activity_Date_Started'] = pd.to_datetime(df['Activity_Date_Started'])

# In[12]:


# converting the string to datetime format
df['Attempt_Date'] = pd.to_datetime(df['Attempt_Date'])

# In[13]:


# converting the string to datetime format 
df['PPM_Outreach_Activity_Closed_Date']= pd.to_datetime(df['PPM_Outreach_Activity_Closed_Date'])#, errors = 'coerce')

# In[14]:


# converting the string to datetime format
df['PPM_Member_DOB'] = pd.to_datetime(df['PPM_Member_DOB'])

# In[15]:


df.dtypes

# In[16]:


df.PPM_Member_RIN.sample(10)

# In[17]:


#export file without index column
df.to_excel("UIC_Report_Dashboard_Outreach_3.xlsx", index=False)

# In[18]:


# Create a timestamp object
timestamp = pd.Timestamp(datetime.datetime.now())

# Print the timestamp
print(timestamp)

# In[19]:


#the end!

# In[ ]:




# In[ ]:



