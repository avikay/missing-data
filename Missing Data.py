#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


#lets create a dataframe using a dictionary that contains null values in it
d = {'A':[1,2,np.nan],'B':[5,np.nan,np.nan],'C':[6,7,8]}


# In[3]:


df = pd.DataFrame(d)


# In[5]:


df#lets see what've we got here in the dataframe


# ##### dropna

# In[8]:


#the dropna function is going to get rid off the null values by removing the whole row that contains null value as:
df.dropna()#now we are left with a single row 0 that did not had any null values 1 & 2 were removed as they had null values


# In[10]:


df#the change made by dropna was not permanent as the inplace value is still 0


# In[11]:


#to use dropna for columns instead of rows we must set axis=1 as:
df.dropna(axis=1)


# In[12]:


#we can set a threshold parameter for a row or a column to not get droped untill the null value in that particular row or column
#exceeds the threshold value as:
df.dropna(thresh=2)


# #### fillna

# In[13]:


#filling the missing value with a string
df.fillna(value='Fill')


# In[17]:


#filling the missing value by replacing it with the mean of the column
df['A'].fillna(value=df['A'].mean())


# In[ ]:




