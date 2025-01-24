#!/usr/bin/env python
# coding: utf-8

# In[24]:


#import libraries and packages
import pandas as pd

# In[25]:


import numpy as np

# In[26]:


#import the df clean data csv file
df = pd.read_csv("/home/node1/Documents/uic/FilesUsed/PD1_services.csv")

# In[27]:


#inspect the shape of the data frame
df.shape

# In[28]:


#explore the data frame
df.info()

# In[29]:


#DUPLICATES
#view duplicates by fields
df.Member_ID.duplicated().any()


# In[30]:


df.Plan_ID.duplicated().all()

# In[31]:


df.Activity_ID.duplicated().all()


# In[32]:


df.rename(columns = {'Mental_Health_Services_1':'ACT'}, inplace = True)

# In[33]:


df.rename(columns = {'Mental_Health_Services_2':'CST'}, inplace = True)

# In[34]:


#Substance_Use_Services
#define function for classifying new field based on any of the service fields being yes
def f(row):
    if row['Substance_Use_Services_1']==1:
        val = 'TRUE'
    elif row['Substance_Use_Services_2']==1:
        val = 'TRUE'
    elif row['Substance_Use_Services_3']==1:
        val = 'TRUE'
    elif row['Substance_Use_Services_4']==1:
        val = 'TRUE'
    elif row['Substance_Use_Services_5']==1:
        val = 'TRUE'
    elif row['Substance_Use_Services_6']==1:
        val = 'TRUE'
    elif row['Substance_Use_Services_7']==1:
        val = 'TRUE'
    elif row['Substance_Use_Services_8']==1:
        val = 'TRUE'
    else:
        val = 'FALSE'
    return val

#create new column 'Substance_Use_Services' using the function above
df['Substance_Use_Services'] = df.apply(f, axis=1)

#check value counts of new field
df['Substance_Use_Services'].value_counts()

# In[35]:


df.columns

# In[36]:


df['Class'].value_counts()

# In[37]:


PD1_serv = df[['Member_Prime','Class', 'Facility','Member_ID', 'Activity_ID', 'Member_Last_Name', 'Member_First_Name', 'MinOfInfo_Date_Assessed', 'MaxOfInfo_Date_Assessed', 
               'First_Plan','Plan_Date','ACT', 'CST', 'Substance_Use_Services', 'N_Plans', 'Dashboard_Status', 'Pipeline_Dashboard_DaysinPhase']].copy(deep=True)

# In[38]:


PD1_serv.info()

# In[39]:


PD1_serv.rename(columns = {'MinOfInfo_Date_Assessed':'Date_First_Assess'}, inplace = True)

# In[40]:


PD1_serv.rename(columns = {'MaxOfInfo_Date_Assessed':'Date_Most_Recent_Assess'}, inplace = True)

# In[41]:


PD1_serv.rename(columns = {'First_Plan':'Date_First_Plan'}, inplace = True)

# In[42]:


PD1_serv.rename(columns = {'Plan_Date':'Date_Most_Recent_Plan'}, inplace = True)

# In[43]:


PD1_serv.rename(columns = {'Pipeline_Dashboard_DaysinPhase':'DaysinPhase'}, inplace = True)

# In[44]:


PD1_serv.columns

# In[45]:


PD1_serv.sort_values(["Member_Prime", "Class", "Facility", "Member_Last_Name", "Member_First_Name"], 
               axis = 0, ascending = True, 
               inplace = True,
               na_position ='first')

# In[ ]:


#Export data
# PD1_serv.to_csv('/home/node1/Documents/uic/FilesUsed/PD1_serv_2023-0629.csv')

# In[ ]:



