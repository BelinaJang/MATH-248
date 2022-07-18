#!/usr/bin/env python
# coding: utf-8

# 2. (5 points) Create a Python notebook (or a program) with the name HW1Q2-V00... where the V00... part is your student number. This notebook demonstrates that it is possible to have two float point numbers a and b in Python, such that a>b>100, and a+b is equal to a. (you need to have two variables named a and b, with values such that a>b>100, and a+b==a is true in Python. 

# In[19]:


# This is an example of rounding error with float numbers
a =(2.0**52-1)*1000
b = 0.2 * 1000 #a>b>100
# a+b does not equal to a -> rounding error
a+b == a

