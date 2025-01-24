#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
# import the builtin time module
import time
#regex
import re
import os

# In[2]:


import warnings
warnings.filterwarnings('ignore')
warnings.simplefilter('ignore')

# In[3]:


os.chdir(r'C:/Users/vwalds/Documents/My Data Sources/')

# In[4]:


# Grab Currrent Time Before Running the Code
start = time.time()

# In[5]:


df = pd.read_excel("UIC_QA_outreach_all.xlsx")

# In[6]:


df.info()

# In[7]:


df.columns

# In[8]:


# converting the string to datetime format
df['PPM_Outreach_Activity_Date_Started'] = pd.to_datetime(df['PPM_Outreach_Activity_Date_Started'])

# In[9]:


# converting the string to datetime format
df['PPM_Outreach_Activity_Date_Created'] = pd.to_datetime(df['PPM_Outreach_Activity_Date_Created'])

# In[10]:


# converting the string to datetime format
df['PPM_Outreach_Attempt_Attempt_Date'] = pd.to_datetime(df['PPM_Outreach_Attempt_Attempt_Date'])

# In[11]:


# converting the string to datetime format
df['PPM_Outreach_Activity_Closed_Date'] = pd.to_datetime(df['PPM_Outreach_Activity_Closed_Date'])

# In[12]:


# converting the string to datetime format
df['Info_Date_Assessed'] = pd.to_datetime(df['Info_Date_Assessed'])

# In[13]:


# converting the string to datetime format
df['NLP_FX_Event_Date'] = pd.to_datetime(df['NLP_FX_Event_Date'])

# In[14]:


# converting the string to datetime format
df['Transition_Discharge_Date'] = pd.to_datetime(df['Transition_Discharge_Date'])

# In[15]:


# converting the string to datetime format
df['PPM_Member_DOB'] = pd.to_datetime(df['PPM_Member_DOB'])

# In[16]:


df.dtypes

# In[17]:


df.PPM_Member_RIN.sample(10)

# In[20]:


# Convert RIN to string
df['PPM_Member_RIN'] = df['PPM_Member_RIN'].astype('str')

# In[21]:


df.PPM_Member_RIN.sample(10)

# In[22]:


# add leading zeros to Member_RIN
df['PPM_Member_RIN'] = df['PPM_Member_RIN'].str.zfill(11)

# In[23]:


df.PPM_Member_RIN.sample(10)

# In[24]:


#export file without index column
df.to_excel("UIC_QA_outreach_all.xlsx", index=False)

# In[25]:


# Grab Current Time After Running the Code
end = time.time()

#Subtract Start Time from The End Time
total_time = end - start
print("\n"+ str(total_time))

# In[ ]:


#the end!

# In[ ]:



