#!/usr/bin/env python
# coding: utf-8

# In[3]:


#import libraries and packages
import pandas as pd
import numpy as np

# In[ ]:


#import
df = pd.read_excel("/home/node1/Documents/uic/FilesUsed/qry_YER_incidents.xlsx")

# In[3]:


df.shape

# In[4]:


df.columns

# In[5]:


df.info()

# In[6]:


df.Report_Label.value_counts()

# In[19]:


df.groupby(['Class', 'Death_type'],as_index = False).count().pivot('Class', 'Death_type').fillna(0)


# In[21]:


df.groupby(['Class','Incident_Prime'])['Incident_Report_ID'].count().reset_index()

# In[22]:


df.groupby(['Class','Incident_Prime'])['Incident_Report_ID'].count()

# In[26]:


#Substance YN and Incident_Prime
#create a cross-tab
ct = pd.crosstab(df.Incident_Prime, df.Caused_By_Substance_YN, margins=True)
ct

# In[ ]:




# In[7]:


#df.to_csv(r'\\uicfs.server.uic.edu\NURS\1\CCMTP\Database & Reports\Mortality Annual Reports\2023_April Mortality Report\incidents.csv')

# In[ ]:



