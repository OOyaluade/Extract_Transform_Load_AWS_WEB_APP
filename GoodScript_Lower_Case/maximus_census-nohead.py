#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
# import the builtin time module
import time
#regex
import re

# In[2]:


# Grab Currrent Time Before Running the Code
start = time.time()

# In[3]:


will = pd.read_excel('/home/node1/Documents/uic/FilesUsed/Census-Williams.xls')

# In[4]:


colb = pd.read_excel('/home/node1/Documents/uic/FilesUsed/Census-Williams.xls')

# In[5]:


colb.columns

# In[6]:


will.columns

# In[7]:


#add a new column to indicate decree
will.insert(1, "Decree", "Williams")

# In[8]:


#add a new column to indicate decree
colb.insert(1, "Decree", "Colbert")

# In[9]:


#combine the two data frames with pandas concatenate method
df = pd.concat([colb, will])

# In[10]:


df.columns

# In[11]:


# Remove columns 
df = df.drop(['Unnamed: 2', 'Unnamed: 15'], axis=1)

# In[12]:


df.columns

# In[13]:


df.rename(columns = {'Discharge/Transfer/\nDeceased Date':'DTD_Date'}, inplace = True)

# In[ ]:




# In[14]:


df.info()

# In[15]:


df.columns

# In[16]:


# converting the string to datetime format
df['Date of Birth'] = pd.to_datetime(df['Date of Birth'])

# In[17]:


# converting the string to datetime format
df['Submitted Date'] = pd.to_datetime(df['Submitted Date'])

# In[18]:


# converting the string to datetime format
df['Admission Date'] = pd.to_datetime(df['Admission Date'])

# In[19]:


# converting the string to datetime format
df['End Date'] = pd.to_datetime(df['End Date'])

# In[20]:


# converting the string to datetime format
df['Effective Date'] = pd.to_datetime(df['Effective Date'])

# In[21]:


# converting the string to datetime format
df['Determination Date'] = pd.to_datetime(df['Determination Date'])

# In[22]:


# converting the string to datetime format
df['DTD_Date'] = pd.to_datetime(df['DTD_Date'])

# In[23]:


# converting the string to datetime format
df['Processed_date'] = pd.Timestamp.now()

# In[24]:


df['Admission Date'].max()

# In[25]:


# converting the string to datetime format
df['Census_date'] = df['Admission Date'].max()

# In[26]:


df.head()

# In[27]:


#function to fix case of member names
def titlecase(s):
    return re.sub(
        r"[A-Za-z]+('[A-Za-z]+)?",
        lambda word: word.group(0).capitalize(),
        s)

# In[28]:


# Fix capitalization
df['Last Name'] = df['Last Name'].apply(titlecase)

# In[29]:


# Fix capitalization
df['First Name'] = df['First Name'].apply(titlecase)

# In[30]:


# Fix capitalization
#convert text to uppercase
df['Admitting Facility'] = df['Admitting Facility'].str.upper()

# In[31]:


#confirm
df[['Last Name', 'First Name', 'Admitting Facility']].sample(15)

# In[32]:


#check value counts of new field
df['Identification Type'].value_counts().sort_values(ascending=False)

# In[33]:


#find duplicate rows across specific columns
duplicateRows = df[df.duplicated()]

# In[34]:


duplicateRows.info()

# In[35]:


duplicateRows.head()

# In[36]:


df.drop_duplicates(subset=None, keep='first', inplace=True)

# In[37]:


df.drop_duplicates(subset='Identification Number', keep='first', inplace=True)

# In[38]:


#find duplicate rows across specific columns
duplicateRows = df[df.duplicated(['Identification Number'])]

# In[39]:


duplicateRows.head()

# In[40]:


print(duplicateRows.sort_values)

# In[41]:


duplicateRows

# In[42]:


#create new column titled 'RIN'
df['RIN'] = np.where(df['Identification Type']=="Medicaid ID", df['Identification Number'], '')

# In[43]:


df.RIN

# In[44]:


#create new column titled 'SSN'
df['SSN'] = np.where(df['Identification Type']=="Social Security Number", df['Identification Number'], '')

# In[45]:


df.SSN

# In[46]:


#add a new column for facility ID
df.insert(1, "Facility_ID", "")

# In[47]:


df.columns

# In[48]:


# replace space with another character
df.columns = df.columns.str.replace(' ', '_')

# In[49]:


df.sort_values(["Decree", "Admitting_Facility", "Last_Name", "First_Name", "Admission_Date"], 
               axis = 0, ascending = True, 
               inplace = True,
               na_position ='first')

# In[52]:


df.head()

# In[50]:


# Grab Current Time After Running the Code
end = time.time()

#Subtract Start Time from The End Time
total_time = end - start
print("\n"+ str(total_time))

# In[51]:


#export to csv
df.to_csv(r'\\uicfs.server.uic.edu\NURS\1\CCMTP\Database & Reports\Database\Census\output\census.csv', index=False)

# In[ ]:



