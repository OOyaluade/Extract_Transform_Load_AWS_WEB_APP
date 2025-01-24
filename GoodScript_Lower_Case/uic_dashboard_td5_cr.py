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


#UIC_Dashboard_TD5_CR


# In[6]:


df = pd.read_excel("UIC_Dashboard_TD5_CR.xlsx")

# In[7]:


df.info()

# In[8]:


df.columns

# In[9]:


# converting the string to datetime format
df['Review_Request_Date_Identified'] = pd.to_datetime(df['Review_Request_Date_Identified'])

# In[10]:


# converting the string to datetime format
df['Dates_Document_Requested'] = pd.to_datetime(df['Dates_Document_Requested'])

# In[11]:


# converting the string to datetime format
df['Date_All_Document_Recieved'] = pd.to_datetime(df['Date_All_Document_Recieved'])

# In[12]:


# converting the string to datetime format
df['Date_Initial_Summary_Sent_Agent'] = pd.to_datetime(df['Date_Initial_Summary_Sent_Agent'])

# In[13]:


# converting the string to datetime format 
df['Date_Initial_Call_Completed']= pd.to_datetime(df['Date_Initial_Call_Completed'])#, errors = 'coerce')

# In[14]:


# converting the string to datetime format
df['Created_On'] = pd.to_datetime(df['Created_On'])

# In[15]:


# converting the string to datetime format
df['Date_Final_Summary_Sent_Agency'] = pd.to_datetime(df['Date_Final_Summary_Sent_Agency'])

# In[16]:


# converting the string to datetime format
df['Outreach_Activity_Closed_Date'] = pd.to_datetime(df['Outreach_Activity_Closed_Date'])

# In[17]:


# converting the string to datetime format
df['Request_Updated_On'] = pd.to_datetime(df['Request_Updated_On'])

# In[18]:


# converting the string to datetime format
df['Request_Reviewed_On'] = pd.to_datetime(df['Request_Reviewed_On'])

# In[19]:


# converting the string to datetime format
df['Date_30_day_Post_Transition'] = pd.to_datetime(df['Date_30_day_Post_Transition'])

# In[20]:


df.dtypes

# In[21]:


df['Member_RIN'].sample(15)

# In[22]:


# Convert RIN to string
df['Member_RIN'] = df['Member_RIN'].astype('str') 

# In[23]:


df['Member_RIN'] = df['Member_RIN'].str.strip()

# In[24]:


# add leading zeros to Member_RIN
df['Member_RIN'] = df['Member_RIN'].str.zfill(11)

# In[25]:


df['Member_RIN'].sample(15)

# In[26]:


#export file without index column
df.to_excel("UIC_Dashboard_TD5_CR.xlsx", index=False)

# In[27]:


# Create a timestamp object
timestamp = pd.Timestamp(datetime.datetime.now())

# Print the timestamp
print(timestamp)

# In[28]:


#the end!

# In[ ]:




# In[ ]:



