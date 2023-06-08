#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt 
sns.set(style="white", color_codes=True)


# In[2]:


iris=pd.read_csv("Iris.csv")
iris.head()


# In[5]:


iris[0:9]


# In[6]:


iris["Species"].value_counts


# In[7]:


iris[0:9:3]


# In[8]:


iris[0:40:3]


# In[9]:


iris["Species"].value_counts()


# In[11]:


iris.plot(kind="scatter", x="SepalLengthCm" , y="SepalWidthCm")


# In[14]:


sns.FacetGrid(iris,hue="Species",size=5).map(plt.scatter,"SepalLengthCm", "SepalWidthCm").add_legend()


# In[15]:


sns.boxplot(x="Species",y="PetalLengthCm",data=iris)


# In[17]:


ax=sns.boxplot(x="Species" ,y="PetalLengthCm",data=iris)
ax=sns.stripplot(x="Species" ,y="PetalLengthCm", jitter=True, data=iris,edgecolor="gray")


# In[18]:


sns.violinplot(x="Species" ,y="PetalLengthCm",data=iris,size=6)


# In[19]:


sns.FacetGrid(iris,hue="Species",size=6).map(sns.kdeplot,"PetalLengthCm").add_legend()


# In[ ]:




