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


#PPM_NF_Activity_Log

# In[6]:


df = pd.read_excel("PPM_NF_Activity_Log.xlsx")

# In[ ]:


#inspect the shape of the data frame
df.shape

# In[ ]:


df.info()

# In[ ]:


df.columns

# In[ ]:


# converting the string to datetime format
df['Log_Admit_Date'] = pd.to_datetime(df['Log_Admit_Date'])

# In[ ]:


# converting the string to datetime format
df['Created_Date'] = pd.to_datetime(df['Created_Date'])

# In[ ]:


# converting the string to datetime format
df['Last_Updated_Date'] = pd.to_datetime(df['Last_Updated_Date'])

# In[ ]:


#view updated type of each column
print(df.dtypes)

# In[ ]:


#export file without index column
df.to_excel("PPM_NF_Activity_Log.xlsx", index=False)

# In[32]:


# Create a timestamp object
timestamp = pd.Timestamp(datetime.datetime.now())

# Print the timestamp
print(timestamp)

# In[33]:


#the end!

# In[ ]:



