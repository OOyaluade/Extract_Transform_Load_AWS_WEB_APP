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


#UIC_Dashboard_SP_SPD3


# In[6]:


df = pd.read_excel("UIC_Dashboard_SP_SPD3.xlsx")

# In[7]:


df.info()

# In[8]:


df.columns

# In[9]:


# converting the string to datetime format
df['PPM_P_Comprehensive_Plan_Date'] = pd.to_datetime(df['PPM_P_Comprehensive_Plan_Date'])

# In[10]:


# converting the string to datetime format
df['Plan_Updated_On'] = pd.to_datetime(df['Plan_Updated_On'])

# In[11]:


# converting the string to datetime format
df['PPM_P_Comprehensive_Plan_Updated_Date'] = pd.to_datetime(df['PPM_P_Comprehensive_Plan_Updated_Date'])

# In[12]:


# converting the string to datetime format
df['Activity_Closed_Date'] = pd.to_datetime(df['Activity_Closed_Date'])

# In[13]:


# converting the string to datetime format 
#df['PPM_Assessment_1_Info_Date_Referred']= pd.to_datetime(df['PPM_Assessment_1_Info_Date_Referred'])#, errors = 'coerce')

# In[14]:


# converting the string to datetime format
df['Member_DOB'] = pd.to_datetime(df['Member_DOB'])

# In[15]:


# converting the string to datetime format
df['PPM_P_Comprehensive_Plan_Projected_Transition_Date'] = pd.to_datetime(df['PPM_P_Comprehensive_Plan_Projected_Transition_Date'])

# In[16]:


# converting the string to datetime format
df['PPM_P_Comprehensive_Plan_Transition_Date'] = pd.to_datetime(df['PPM_P_Comprehensive_Plan_Transition_Date'])

# In[17]:


# converting the string to datetime format
df['Secondary_Transition_To_PSH_Date'] = pd.to_datetime(df['Secondary_Transition_To_PSH_Date'])

# In[18]:


df.info()

# In[19]:


#export file without index column
df.to_excel("UIC_Dashboard_SP_SPD3.xlsx", index=False)

# In[20]:


# Create a timestamp object
timestamp = pd.Timestamp(datetime.datetime.now())

# Print the timestamp
print(timestamp)

# In[21]:


#the end!

# In[ ]:




# In[ ]:



