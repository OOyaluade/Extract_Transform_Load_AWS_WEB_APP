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


#UIC_Dashboard_Pipeline_PD7_CAST2


# In[6]:


df = pd.read_excel("UIC_Dashboard_Pipeline_PD7_CAST2.xlsx")

# In[7]:


df.info()

# In[8]:


df.columns

# In[9]:


# converting the string to datetime format
df['PPM_Member_DOB'] = pd.to_datetime(df['PPM_Member_DOB'])

# In[10]:


# converting the string to datetime format
df['Request_Created_On'] = pd.to_datetime(df['Request_Created_On'])

# In[11]:


# converting the string to datetime format
df['PPM_C_Review_Request_Date_All_Document_Recieved'] = pd.to_datetime(df['PPM_C_Review_Request_Date_All_Document_Recieved'])

# In[12]:


# converting the string to datetime format
df['PPM_C_Review_Request_Initial_Review_Date'] = pd.to_datetime(df['PPM_C_Review_Request_Initial_Review_Date'])

# In[13]:


# converting the string to datetime format
df['Request_Reviewed_On'] = pd.to_datetime(df['Request_Reviewed_On'])

# In[14]:


# converting the string to datetime format
df['Request_Updated_On'] = pd.to_datetime(df['Request_Updated_On'])

# In[15]:


# converting the string to datetime format
df['Activity_Closed_Date'] = pd.to_datetime(df['Activity_Closed_Date'])

# In[16]:


df.dtypes

# In[17]:


#export file without index column
df.to_excel("UIC_Dashboard_Pipeline_PD7_CAST2.xlsx", index=False)

# In[18]:


# Create a timestamp object
timestamp = pd.Timestamp(datetime.datetime.now())

# Print the timestamp
print(timestamp)

# In[19]:


#the end!

# In[ ]:




# In[ ]:



