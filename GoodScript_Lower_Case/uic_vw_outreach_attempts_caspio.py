#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import numpy as np
import time
import re
import os
import datetime

# In[8]:


import warnings
warnings.filterwarnings('ignore')
warnings.simplefilter('ignore')

# In[9]:


# os.chdir(r'C:/Users/vwalds/Documents/My Data Sources/')

# In[10]:


# Grab Current Time Before Running the Code
start = time.time()

# In[11]:


#UIC_VW_Outreach_Attempts_Caspio


# In[12]:


df = pd.read_excel("/home/node1/Documents/uic/FilesUsed/UIC_VW_Outreach_Attempts_caspio.xlsx")

# In[13]:


df.info()

# In[14]:


df.columns

# In[15]:


# converting the string to datetime format
df['PPM_Outreach_Attempt_Attempt_Date'] = pd.to_datetime(df['PPM_Outreach_Attempt_Attempt_Date'])

# In[16]:


# converting the string to datetime format
df['Outreach_Activity_Date_Started'] = pd.to_datetime(df['Outreach_Activity_Date_Started'])

# In[17]:


# converting the string to datetime format
df['Outreach_Activity_Date_Finished'] = pd.to_datetime(df['Outreach_Activity_Date_Finished'])

# In[18]:


df.dtypes

# In[19]:


df.PPM_Member_RIN.sample(10)

# In[20]:


# Convert RIN to string
df['PPM_Member_RIN'].astype('str')

# In[21]:


df.PPM_Member_RIN.sample(10)

# In[22]:


# add leading zeros to Member_RIN
df['PPM_Member_RIN'] = df['PPM_Member_RIN'].str.zfill(11)

# In[ ]:


df.PPM_Member_RIN.sample(10)

# In[ ]:




# In[ ]:


df.PPM_Member_RIN.sample(10)

# In[ ]:


#export file without index column
df.to_excel("UIC_VW_Outreach_Attempts_Caspio.xlsx", index=False)

# In[ ]:


# Create a timestamp object
timestamp = pd.Timestamp(datetime.datetime.now())

# Print the timestamp
print(timestamp)

# In[ ]:


#the end!

# In[ ]:




# In[ ]:



