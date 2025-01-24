#!/usr/bin/env python
# coding: utf-8

# In[88]:


import pandas as pd
import numpy as np
import time
import re
import os
import datetime

# In[89]:


import warnings
warnings.filterwarnings('ignore')
warnings.simplefilter('ignore')

# In[90]:


# os.chdir(r'C:/Users/vwalds/Documents/My Data Sources/')

# In[91]:


# Grab Current Time Before Running the Code
start = time.time()

# In[92]:


#UIC_VW_Transitions_Housingtype



# In[93]:


df = pd.read_excel("../WebApp/uploads/uic_vw_transitions_housingtype.xlsx")

# In[94]:


# df.info()

# In[95]:


df.columns

# In[96]:


# converting the string to datetime format
df['Transition_Discharge_Date'] = pd.to_datetime(df['Transition_Discharge_Date'])

# In[97]:


# converting the string to datetime format
# df['Activity_Closed_Date'] = pd.to_datetime(df['Activity_Closed_Date'])

# In[98]:


# converting the string to datetime format
df['Activity_Date_Started'] = pd.to_datetime(df['Activity_Date_Started'])

# In[99]:


# converting the string to datetime format
df['Transition_Finished_Date'] = pd.to_datetime(df['Transition_Finished_Date'])

# In[100]:


df.dtypes

# In[101]:


df['RIN'].sample(10)

# In[102]:


# Convert RIN to string
df['RIN'] = df['RIN'].astype('str') 

# In[103]:


df['RIN'] = df['RIN'].str.strip()

# In[104]:


df['RIN'].sample(5)

# In[105]:


# add leading zeros to Member_RIN
df['RIN'] = df['RIN'].str.zfill(9)

# In[106]:


# df['RIN'].sample(10)

# In[ ]:


from pathlib import Path
script_path = Path.cwd().parent
output_dir = script_path / "WebApp" / "processed"
output_dir.mkdir(parents=True, exist_ok=True)
output_file = output_dir / "UIC_VW_Transitions_Housingtype.xlsx".lower()
df.to_excel(output_file, index=False)

# In[ ]:


# Create a timestamp object
timestamp = pd.Timestamp(datetime.datetime.now())



# In[22]:




# In[ ]:



