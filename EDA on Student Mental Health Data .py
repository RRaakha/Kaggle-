#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
data = pd.read_csv('C:\\Users\\\'Raakha ALAMUKII\\Downloads\\Student Mental health.csv')
data.head()


# In[19]:


data.shape # to get the amount of columns and rows


# In[3]:


data.info() 


# In[6]:


data.isnull() # to check for null values 


# In[9]:


col = data.columns # to check the column names 
col


# In[12]:


data[col].nunique() # to check amount of unique values for each column 


# In[15]:


data.describe() # to get the statistics summary of the data


# In[16]:


data.duplicated().sum() # to get the count of duplicated values


# In[24]:


data[['Age']].boxplot() # plot a quick boxplot for Age 


# In[22]:


data['What is your course?'].value_counts().head()


# In[ ]:


data['Date'] = pd.to_datetime(data['Timestamp'])
data['Month'] = data['Date'].dt.month
data['Year'] = data['Date'].dt.year
data['Day'] = data['Date'].dt.day


# In[ ]:


data = data.drop('Timestamp',axis=1)


# In[34]:


data.head()


# In[35]:


data['Age'].hist()


# In[37]:


data['Your current year of Study'].unique()


# In[38]:


data['Your current year of Study'].value_counts()


# In[41]:


data['Your current year of Study'] = data['Your current year of Study'].replace('Year 1', 'year 1')


# In[43]:


data['Your current year of Study'].value_counts()


# In[44]:


data['Your current year of Study'] = data['Your current year of Study'].replace('Year 2', 'year 2')


# In[45]:


data['Your current year of Study'].value_counts()


# In[46]:


data['Your current year of Study'] = data['Your current year of Study'].replace('Year 3', 'year 3')


# In[47]:


data['Your current year of Study'].value_counts()


# In[57]:


cols = data.columns
data[cols].nunique()


# In[59]:


data['What is your CGPA?'].value_counts()


# In[60]:


data['What is your CGPA?'] = data['What is your CGPA?'].replace('3.50 - 4.00 ', '3.50 - 4.00')


# In[61]:


data['What is your CGPA?'].value_counts()


# In[66]:


data['Month'].value_counts()


# In[67]:


data['Choose your gender'].value_counts()


# In[77]:


import  matplotlib.pyplot as plt
plt.hist(data['Choose your gender'])


# In[118]:


plt.bar(data['Choose your gender'], data['Do you have Anxiety?'])


# In[84]:


data.groupby('What is your CGPA?')['Age'].mean().plot.bar()


# In[109]:


gender = data.groupby(['Choose your gender']).size().reset_index(name='count')
gender


# In[113]:


plt.bar(gender['Choose your gender'],gender['count'])
plt.show()


# In[114]:


Depression = data.groupby(['Do you have Depression?']).size().reset_index(name='count')
Depression


# In[115]:


plt.bar(Depression['Do you have Depression?'], Depression['count'])
plt.show()


# In[116]:


get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns; sns.set()
sns.pairplot(data)


# In[124]:


Anxiety = data.groupby(['Do you have Anxiety?']).size().reset_index(name='count')
Anxiety


# In[125]:


plt.bar(Anxiety['Do you have Anxiety?'], Anxiety['count'])
plt.show()


# In[140]:


plt.hist(data['What is your course?'])


# In[149]:


plt.hist( data['Marital status'])


# In[150]:


Panic_attack = data.groupby(['Do you have Panic attack?']).size().reset_index(name='count')
Panic_attack


# In[153]:


plt.bar(Panic_attack['Do you have Panic attack?'], Panic_attack['count'])
plt.show()


# In[155]:


Treatment = data.groupby(['Did you seek any specialist for a treatment?']).size().reset_index(name='count')
Treatment


# In[156]:


plt.bar(Treatment['Did you seek any specialist for a treatment?'], Treatment ['count'])
plt.show()


# In[157]:


study_year = data.groupby(['Your current year of Study']).size().reset_index(name='count')
study_year


# In[158]:


plt.bar(study_year['Your current year of Study'], study_year['count'])
plt.show()


# ## Major Findings:
#  - The respondets were mostly female
#  - The respondents Were mostly in year 1
#  - Panic attack(68%:NO, 32%:Yes)
#  - Depression(65%:NO, 35%:Yes)
#  - Anxiety(67%:NO, 33%:Yes)
#  - Seek specialist for treatment (95%:NO, 5%:Yes)

# In[ ]:




