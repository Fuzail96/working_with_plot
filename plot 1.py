#!/usr/bin/env python
# coding: utf-8

# # starting with plots
# 

# In[2]:


from matplotlib import pylab
print (pylab.__version__)


# #use numpy to auto generate random data

# In[15]:


import numpy as np

x1=np.linspace(0,10,25)
y1=x+2
x2=np.linspace(0,10,25)
y2=x*x+2
x3=np.linspace(0,10,25)
y3=x*x*x+2
x4=np.linspace(0,10,25)
y4=x*x*x*x+2

print(x1)
print(y1)
print(np.array([x,y]))


# In[19]:


pylab.title("Sample plot")
pylab.xlabel("input")
pylab.ylabel("output")
pylab.plot(x1,y1,'g')


# In[16]:


pylab.subplot(2,2,1)
pylab.plot(x1,y1,'r--')
pylab.subplot(2,2,2)
pylab.plot(x2,y2,'g--')
pylab.subplot(2,2,3)
pylab.plot(x3,y3,'b--')
pylab.subplot(2,2,4)
pylab.plot(x4,y4,'y--')


# In[9]:





# In[ ]:





# In[ ]:




