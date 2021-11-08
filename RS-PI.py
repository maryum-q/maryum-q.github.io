#!/usr/bin/env python
# coding: utf-8

# # PERSONALITY - PREDICTION using IBM-Watson

# ## Installing Dependicies

# In[10]:



# In[9]:


# Importing the Presonality-Insights-library
import ibm_watson
from watson_developer_cloud import PersonalityInsightsV3


# In[10]:


# Importing JSON
import json
import csv

import pandas as pd

# ## Service Generation

# In[11]:


# This url is available from the manage page of the service
url = ''


# In[12]:


# Create this API Key When you create the service
api_key = ''


# In[ ]:


# Create conection to service
service = PersonalityInsightsV3(url=url, version='2020-06-17', iam_apikey=api_key)


# ## Input Text

# In[14]:


with open('quran-en.txt', 'r', encoding='utf-8') as f:
	text = f.read()


profile = service.profile(text, content_type='text/plain').get_result()


# In[16]:


len(profile['warnings'])


# ## Retrived JSON Evaluation 

# In[17]:


print(json.dumps(profile , indent=2))


# In[18]:


profile['personality']


# In[28]:


profile['personality'][0]


# In[20]:


profile['personality'][1]


# In[21]:


profile['personality'][2]


# In[22]:


profile['personality'][3]


# In[23]:


profile['personality'][4]


# In[44]:


print("The BIG FIVE PERSONALITIES ARE :\n")

for i in range(5):
    print("{}. {}".format(i+1,profile['personality'][i]['name']))


# ## Personality Dataset Creation

# In[40]:


big5 = []
subCategory = []
percentage = []
    
for i in range(5):
    for j in range(6):
        big5.append(profile['personality'][i]['name'])
        subCategory.append(profile['personality'][i]['children'][j]['name'])
        percentage.append(profile['personality'][i]['children'][j]['percentile'] * 100)


# In[41]:




df = pd.DataFrame()

df['Category'] = big5
df['Sub-Category'] = subCategory
df['Percentage-Likely'] = percentage


# In[42]:


df


# In[43]:
