#!/usr/bin/env python
# coding: utf-8

# 1. This notebook computes the distance between two points. The coordinates are given by 4 variables, x1, y1, x2, y2, which gives the x and y coordinates of the first and second points, respectively. You can assign any values to the coordinates. The distance should be stored in a variable d. At last, print out the value of d. (Hint, the function to compute the square root is sqrt in the math module, to use it, you need to import the math module, like "import sqrt from math" before using the function)

# In[7]:


# x and y cordinates of the first point
x1 = 1
y1 = 1
# x and y cordinates of the second point
x2 = -1
y2 = -1

from math import sqrt

# distance between x1 and x2
dx = x1 - x2

# distace between y1 and y2
dy = y1 - y2

# distance between first and second points using pythagoras theorem
d = sqrt((dx)**2+(dy)**2)

# print distance between two points
print("d=", d)

