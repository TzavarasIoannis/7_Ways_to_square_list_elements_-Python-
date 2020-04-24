#!/usr/bin/env python
# coding: utf-8

# In[1]:


list1 = [1,2,3,4,5,6,7,8,9,10]


# In[2]:


#first way
newlist1 = []
for i in range(0,len(list1)):
    list1[i]=list1[i]**2
    


# In[13]:


#Seocnd way
def squre_list(l:list):
    for i in range(0,len(l)):
        l[i]=l[i]**2
    return l


# In[4]:


#Third way
list2 = [i**2 for i in list1 ]


# In[5]:


#4th way
list2=list ( filter(lambda x : x**2 ,list1 ))


# In[9]:


#5th way
import numpy as np
print ( np.square(list1))


# In[10]:


#6th way
list2 = list (map ( lambda x : x**2,list1))


# In[12]:


#7th way
newlist= []
for i in list1:
    newlist.append(i**2)


# In[ ]:




