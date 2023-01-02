#!/usr/bin/env python
# coding: utf-8

# # Assignment 1 Submitted by Deepthi Mushini

# ## Q1. Write a Python program to calculate the length of a string

# In[6]:


length = len(input('Write a sentence:   '))
print (length)


# ## Q2. Python program to calculate the square root.

# In[5]:


import math
number = float(input("Enter a number:"))
sqrt = math.sqrt(number)
print(f"The square root of{number}is {sqrt}") 


#  # Q3. Write a python program to convert temperature in celcius to temperature in fahrenheit.

# In[7]:


def celsius_to_fahrenheit(c):
    f = c*9/5+32
c = float(input('temperature in celsius:  '))
f = (celsius_to_fahrenheit(c))
print(f'{c} is {f}')


# # Q4. Write a data type needed for given data.(10,4.5,2+6j) 

# In[12]:


data = (10, 4.5, 2+6j)


# In[15]:


print(type(data))


# In[16]:


a = 10
print(type(a))


# In[17]:


b = 4.5
print(type(b))


# In[18]:


c = 2+6j
print(type(c))

