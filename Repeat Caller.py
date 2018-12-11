
# coding: utf-8

# In[29]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


data = pd.read_csv(r"File Location")


# In[3]:


data.head()


# In[4]:


X=data['RecordWritten']


# In[5]:


X.head()


# In[18]:


plt.hist(X, bins=31,align='mid')
plt.ylabel('Number of Calls')
plt.xlabel('Days in the Month')
plt.title('Histograhm of Number of Repeat Calls Per Day')
plt.show()


# In[12]:


data = pd.read_csv(r"File Location")


# In[13]:


data.head()


# In[14]:


X=data['Time']


# In[15]:


X.head()


# In[17]:


plt.hist(X, bins=12,align='mid')
plt.ylabel('Number of Calls')
plt.xlabel('Time of Day')
mppltl.title('Histograhm of Number of Repeat Calls By Time')
plt.show()


# In[6]:


data = pd.read_csv(r"File Location")


# In[7]:


data.head()


# In[9]:


X=data['Days']


# In[18]:


plt.hist(X, bins=7,align='mid')
plt.ylabel('Number of Calls')
plt.xlabel('Day of Week')
plt.title('Histograhm of Number of Repeat Calls By Days of Week')
plt.show()


# In[24]:


data = pd.read_csv(r"File Location")


# In[25]:


data.head()


# In[26]:


X=data


# In[27]:


from sklearn.cluster import KMeans
myCluster = KMeans(n_clusters=8, n_jobs=-1).fit(data)


# In[42]:


plt.scatter(X.values[:, 1], X.values[:, 0],c=myCluster.labels_)
plt.show()


# In[34]:


data = pd.read_csv(r"File Location")


# In[35]:


data.head()


# In[36]:


X=data


# In[39]:


from sklearn.cluster import KMeans
myCluster = KMeans(n_clusters=24, n_jobs=-1).fit(data)


# In[ ]:


plt.scatter(X.values[:, 1], X.values[:, 0],c=myCluster.labels_)
plt.show()

