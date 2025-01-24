#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import libraries and packages
import pandas as pd

# In[2]:


import numpy as np

# In[3]:


#import the df clean data csv file
df = pd.read_csv("/home/node1/Documents/uic/FilesUsed/PD1_services.csv")

# In[4]:


#inspect the shape of the data frame
df.shape

# In[5]:


#explore the data frame
df.info()

# In[6]:


#DUPLICATES
#view duplicates by fields
df.Member_ID.duplicated().any()


# In[7]:


df.Plan_ID.duplicated().all()

# In[8]:


df.Activity_ID.duplicated().all()


# In[9]:


#create new column titled 'Aging_Waiver' that is updated to Yes/1 if e aging_waiver_1 fields is yes.
#df['Aging_Waiver'] = np.where(df['Aging_Waiver_1']=1, 1, 0)


# In[10]:


df['Further_Info_Eval_2_1'].value_counts()          

# In[11]:


#Further_Evaluation
#define function for classifying new field based on any of the service fields being yes
def f(row):
    if row['Further_Info_Eval_2_1']==1:
        val = '1'
    elif row['Further_Info_Eval_2_2']==1:
        val = '1'
    elif row['Further_Info_Eval_2_3']==1:
        val = '1'
    elif row['Further_Info_Eval_2_4']==1:
        val = '1'
    elif row['Further_Info_Eval_2_5']==1:
        val = '1'
    elif row['Further_Info_Eval_2_6']==1:
        val = '1'
    elif row['Further_Info_Eval_2_7']==1:
        val = '1'
    elif row['Further_Info_Eval_2_8']==1:
        val = '1'
    else:
        val = '0'
    return val

#create new column 'Further_Evaluation' using the function above
df['Further_Evaluation'] = df.apply(f, axis=1)

#check value counts of new field
df['Further_Evaluation'].value_counts()

# In[12]:


#Aging_Waiver
#define function for classifying 'Aging_Waiver' based on any of the aging waiver fields is yes
def f(row):
    if row['Aging_Waiver_1']==1:
        val = '1'
    elif row['Aging_Waiver_2']==1:
        val = '1'
    elif row['Aging_Waiver_3']==1:
        val = '1'
    else:
        val = '0'
    return val

#create new column 'Aging_Waiver' using the function above
df['Aging_Waiver'] = df.apply(f, axis=1)

# In[13]:


#check value counts of new field
df['Aging_Waiver'].value_counts()

# In[14]:


#DRS_Waiver
#define function for classifying 'DRS_Waiver' based on any of the DRS waiver fields being yes
def f(row):
    if row['DRS_Waiver_1']==1:
        val = '1'
    elif row['DRS_Waiver_2']==1:
        val = '1'
    elif row['DRS_Waiver_3']==1:
        val = '1'
    elif row['DRS_Waiver_4']==1:
        val = '1'
    elif row['DRS_Waiver_5']==1:
        val = '1'
    elif row['DRS_Waiver_6']==1:
        val = '1'
    elif row['DRS_Waiver_7']==1:
        val = '1'
    elif row['DRS_Waiver_8']==1:
        val = '1'
    elif row['DRS_Waiver_9']==1:
        val = '1'
    elif row['DRS_Waiver_10']==1:
        val = '1'
    elif row['DRS_Waiver_11']==1:
        val = '1'
    else:
        val = '0'
    return val

#create new column 'DRS_Waiver' using the function above
df['DRS_Waiver'] = df.apply(f, axis=1)

#check value counts of new field
df['DRS_Waiver'].value_counts()


# In[15]:


#Mental_Health_Services
#define function for classifying new field based on any of the service fields being yes
def f(row):
    if row['Mental_Health_Services_1']==1:
        val = '1'
    elif row['Mental_Health_Services_2']==1:
        val = '1'
    elif row['Mental_Health_Services_3']==1:
        val = '1'
    elif row['Mental_Health_Services_4']==1:
        val = '1'
    elif row['Mental_Health_Services_5']==1:
        val = '1'
    elif row['Mental_Health_Services_6']==1:
        val = '1'
    elif row['Mental_Health_Services_7']==1:
        val = '1'
    elif row['Mental_Health_Services_8']==1:
        val = '1'
    elif row['Mental_Health_Services_9']==1:
        val = '1'
    elif row['Mental_Health_Services_10']==1:
        val = '1'
    else:
        val = '0'
    return val

#create new column 'Mental_Health_Services' using the function above
df['Mental_Health_Services'] = df.apply(f, axis=1)

#check value counts of new field
df['Mental_Health_Services'].value_counts()

# In[16]:


#Substance_Use_Services
#define function for classifying new field based on any of the service fields being yes
def f(row):
    if row['Substance_Use_Services_1']==1:
        val = '1'
    elif row['Substance_Use_Services_2']==1:
        val = '1'
    elif row['Substance_Use_Services_3']==1:
        val = '1'
    elif row['Substance_Use_Services_4']==1:
        val = '1'
    elif row['Substance_Use_Services_5']==1:
        val = '1'
    elif row['Substance_Use_Services_6']==1:
        val = '1'
    elif row['Substance_Use_Services_7']==1:
        val = '1'
    elif row['Substance_Use_Services_8']==1:
        val = '1'
    else:
        val = '0'
    return val

#create new column 'Substance_Use_Services' using the function above
df['Substance_Use_Services'] = df.apply(f, axis=1)

#check value counts of new field
df['Substance_Use_Services'].value_counts()

# In[17]:


#Specialty_Providers
#define function for classifying new field based on any of the service fields being yes
def f(row):
    if row['Specialty_Providers_1']==1:
        val = '1'
    elif row['Specialty_Providers_2']==1:
        val = '1'
    elif row['Specialty_Providers_3']==1:
        val = '1'
    elif row['Specialty_Providers_4']==1:
        val = '1'
    elif row['Specialty_Providers_5']==1:
        val = '1'
    elif row['Specialty_Providers_6']==1:
        val = '1'
    elif row['Specialty_Providers_7']==1:
        val = '1'
    elif row['Specialty_Providers_8']==1:
        val = '1'
    elif row['Specialty_Providers_9']==1:
        val = '1'
    elif row['Specialty_Providers_10']==1:
        val = '1'
    elif row['Specialty_Providers_11']==1:
        val = '1'
    elif row['Specialty_Providers_12']==1:
        val = '1'
    elif row['Specialty_Providers_13']==1:
        val = '1'    
    elif row['Specialty_Providers_14']==1:
        val = '1'       
    else:
        val = '0'
    return val

#create new column 'Substance_Use_Services' using the function above
df['Specialty_Providers'] = df.apply(f, axis=1)

#check value counts of new field
df['Specialty_Providers'].value_counts()

# In[18]:


#Psychiatrist
#define function for classifying new field based on any of the service fields being yes
def f(row):
    if row['Specialty_Providers_13']==1:
        val = '1'     
    else:
        val = '0'
    return val

#create new column using the function above
df['Psychiatrist'] = df.apply(f, axis=1)

#check value counts of new field
df['Psychiatrist'].value_counts()

# In[19]:


#Cardiologist
#define function for classifying new field based on any of the service fields being yes
def f(row):
    if row['Specialty_Providers_1']==1:
        val = '1'     
    else:
        val = '0'
    return val

#create new column using the function above
df['Cardiologist'] = df.apply(f, axis=1)

#check value counts of new field
df['Cardiologist'].value_counts()

# In[20]:


#Pain_Management
#define function for classifying new field based on any of the service fields being yes
def f(row):
    if row['Specialty_Providers_11']==1:
        val = '1'     
    else:
        val = '0'
    return val

#create new column using the function above
df['Pain_Management'] = df.apply(f, axis=1)

#check value counts of new field
df['Pain_Management'].value_counts()

# In[21]:


#Pulmonologist
#define function for classifying new field based on any of the service fields being yes
def f(row):
    if row['Specialty_Providers_14']==1:
        val = '1'     
    else:
        val = '0'
    return val

#create new column using the function above
df['Pulmonologist'] = df.apply(f, axis=1)

#check value counts of new field
df['Pulmonologist'].value_counts()

# In[22]:


#Neurologist
#define function for classifying new field based on any of the service fields being yes
def f(row):
    if row['Specialty_Providers_6']==1:
        val = '1'     
    else:
        val = '0'
    return val

#create new column using the function above
df['Neurologist'] = df.apply(f, axis=1)

#check value counts of new field
df['Neurologist'].value_counts()

# In[23]:


#Oncologist
#define function for classifying new field based on any of the service fields being yes
def f(row):
    if row['Specialty_Providers_8']==1:
        val = '1'     
    else:
        val = '0'
    return val

#create new column using the function above
df['Oncologist'] = df.apply(f, axis=1)

#check value counts of new field
df['Oncologist'].value_counts()

# In[24]:


#Other_Specialty
#define function for classifying new field based on any of the service fields being yes
def f(row):
    if row['Other_Specialty_1']==1:
        val = '1'
    elif row['Other_Specialty_2']==1:
        val = '1'
    elif row['Other_Specialty_3']==1:
        val = '1'
    elif row['Other_Specialty_4']==1:
        val = '1'
    elif row['Other_Specialty_5']==1:
        val = '1'
    elif row['Other_Specialty_6']==1:
        val = '1'
    elif row['Other_Specialty_7']==1:
        val = '1'
    else:
        val = '0'
    return val

#create new column using the function above
df['Other_Specialty'] = df.apply(f, axis=1)

#check value counts of new field
df['Other_Specialty'].value_counts()

# In[ ]:




# In[25]:


#Physical_Therapy
#define function for classifying new field based on any of the service fields being yes
def f(row):
    if row['Other_Specialty_4']==1:
        val = '1'
    else:
        val = '0'
    return val

#create new column using the function above
df['Physical_Therapy (PT)'] = df.apply(f, axis=1)

#check value counts of new field
df['Physical_Therapy (PT)'].value_counts()

# In[26]:


#Occupational_Therapy
#define function for classifying new field based on any of the service fields being yes
def f(row):
    if row['Other_Specialty_5']==1:
        val = '1'
    else:
        val = '0'
    return val

#create new column using the function above
df['Occupational_Therapy (OT)'] = df.apply(f, axis=1)

#check value counts of new field
df['Occupational_Therapy (OT)'].value_counts()

# In[27]:


#Medication
#define function for classifying new field based on any of the service fields being yes
def f(row):
    if row['Medication_1']==1:
        val = '1'
    elif row['Medication_2']==1:
        val = '1'
    elif row['Medication_3']==1:
        val = '1'
    elif row['Medication_4']==1:
        val = '1'
    elif row['Medication_5']==1:
        val = '1'
    elif row['Medication_6']==1:
        val = '1'
    else:
        val = '0'
    return val

#create new column 'Medication' using the function above
df['Medication'] = df.apply(f, axis=1)

#check value counts of new field
df['Medication'].value_counts()

# In[28]:


#Transportation
#define function for classifying new field based on any of the service fields being yes
def f(row):
    if row['Transportation_1']==1:
        val = '1'
    elif row['Transportation_2']==1:
        val = '1'
    elif row['Transportation_3']==1:
        val = '1'
    else:
        val = '0'
    return val

#create new column 'Transportation' using the function above
df['Transportation'] = df.apply(f, axis=1)

#check value counts of new field
df['Transportation'].value_counts()

# In[29]:


#Other_Services
#define function for classifying new field based on any of the service fields being yes
def f(row):
    if row['Other_Services_1']==1:
        val = '1'
    elif row['Other_Services_2']==1:
        val = '1'
    elif row['Other_Services_3']==1:
        val = '1'
    elif row['Other_Services_4']==1:
        val = '1'
    else:
        val = '0'
    return val

#create new column 'Other_Services' using the function above
df['Other_Services'] = df.apply(f, axis=1)

#check value counts of new field
df['Other_Services'].value_counts()

# In[30]:


#Documentation_Needs
#define function for classifying new field based on any of the service fields being yes
def f(row):
    if row['Documentation_Needs_1']==1:
        val = '1'
    elif row['Documentation_Needs_2']==1:
        val = '1'
    elif row['Documentation_Needs_3']==1:
        val = '1'
    elif row['Documentation_Needs_4']==1:
        val = '1'
    elif row['Documentation_Needs_5']==1:
        val = '1'
    else:
        val = '0'
    return val

#create new column 'Documentation_Needs' using the function above
df['Documentation_Needs'] = df.apply(f, axis=1)

#check value counts of new field
df['Documentation_Needs'].value_counts()

# In[31]:


df.columns

# In[32]:


df['Class'].value_counts()

# In[33]:


#MISSING DATA
#replace all null values with NaN for consistency
#df['Plan_ID'] = df['Plan_ID'].replace('', np.NaN)

# In[34]:


PD1_serv_gp = df[['Member_ID', 'Activity_ID', 'Assessment_ID', 'Class', 'Facility', 'Member_Prime', 'Plan_ID', 'Plan_Date','Aging_Waiver','DRS_Waiver', 
         'Mental_Health_Services', 'Substance_Use_Services','Specialty_Providers', 'Other_Specialty', 'Medication','Transportation',
         'Other_Services', 'Documentation_Needs','Further_Evaluation', 'Pulmonologist', 'Neurologist', 'Oncologist', 'Psychiatrist', 'Cardiologist',
         'Pain_Management','Physical_Therapy (PT)', 'Occupational_Therapy (OT)']].copy(deep=True)

# In[35]:


PD1_serv_gp.info()

# In[36]:


#Plan Status
#define function for classifying new field based on any of the service fields being yes
#def f(row):
    #if row['Plan_ID']==0:
        #val = 'No Plan'
    #else:
        #val = 'FY23 P1 Plan Completed'
    #return val

#create new column 'Documentation_Needs' using the function above
#PD1_services_grouped['Plan_Status'] = df.apply(f, axis=1)

#check value counts of new field
#PD1_services_grouped['Plan_Status'].value_counts()

# In[38]:


#Export data
PD1_serv_gp.to_csv(r'C:/Users/vwalds/Documents/python/dashboard/PD1_serv_gp.csv')

# In[ ]:



