#!/usr/bin/env python
# coding: utf-8

# In[25]:


#import libraries and packages
import pandas as pd
import numpy as np

# In[26]:


#import the df clean data csv file
df = pd.read_csv("/home/node1/Documents/uic/FilesUsed/qry_mort_Incidents_legacy.csv")

# In[27]:


df.shape

# In[28]:


df.columns

# In[29]:


legacy = pd.get_dummies(df, prefix='', prefix_sep='', columns=['App_Type']) 

# In[30]:


legacy.columns

# In[31]:


#add a new column to indicate datasource
legacy.insert(1, "Source", "legacy")

# In[32]:


legacy.columns

# In[33]:


# Remove columns 
legacy = legacy.drop(['App_Type2', 'More'], axis=1)

# In[34]:


legacy.info()

# In[35]:


legacy.Level.value_counts()

# In[36]:


#import the df clean data csv file
file = "/home/node1/Documents/uic/FilesUsed/qry_mort_Incidents_app.csv"
app = pd.read_csv(file)

# In[13]:


app.columns

# In[14]:


#add a new column to indicate datasource
app.insert(1, "Source", "webapp")

# In[15]:


app.info()

# In[16]:


for column in app.columns:
    if app[column].dtype == 'bool':
        app[column] = app[column].astype(np.float64)

# In[17]:


app.info()

# In[18]:


app.Level.value_counts()

# In[19]:


# Applying the condition
app['Level'] = app['Level'].replace(0, 5)

# In[20]:


app.Level.value_counts()

# In[21]:


#combine the two data frames with pandas concatenate method
inc = pd.concat([legacy, app])

# In[22]:


inc.info()

# In[23]:


# converting the string to datetime format
inc['Incident_Date'] = pd.to_datetime(inc['Incident_Date'])

# In[24]:


print(inc['Incident_Date'].head())

# In[25]:


#for column in inc.columns:
    #if inc[column].dtype == 'float64':
        #inc[column] = inc[column].astype(np.int32)

# In[26]:


for column in inc.columns:
    if inc[column].dtype == 'bool':
        inc[column] = inc[column].astype(np.float64)

# In[27]:


inc.info()

# In[30]:


inc.Level.value_counts()

# In[31]:


inc.to_csv(r'\\uicfs.server.uic.edu\NURS\1\CCMTP\Database & Reports\Mortality Annual Reports\2023_April Mortality Report\incidents.csv')

# In[ ]:



