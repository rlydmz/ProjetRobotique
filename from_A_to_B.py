
# coding: utf-8

# In[16]:


# Angles are in degrees regarding the funciton arguments and parameters


# In[22]:


import math
import pypot.dynamixel as pd

from test_moteur import *


# In[23]:


def calculate_angle (A, B):
    angleInRadians = math.atan2(B[1] - A[1], B[0] - A[0])
    return math.degrees (angleInRadians)


# In[24]:


# Returns the oblique distance between the two given points
def calculate_distance (A, B):
     return math.sqrt((B[0] - A[0])**2 + (B[1] - A[1])**2)


# In[26]:


def move_by (distance, speed):
    if (distance > 0): 
        forward_by (distance, speed)
    else:
        backward_by (distance, speed)


# In[27]:


def go_to (speed, B=[0,0,0]):
    x1, y1, angle1 = B[0], B[1], B[2]

    angleToTurn = calculate_angle ([0,0], [x1,y1])
    distance = calculate_distance ([0,0], [x1,y1])

    # arrival to destination point
    turn (angleToTurn, speed)
    move_by (distance, speed)
    
    # put the bot on the final desired angle
    finalAngleToTurn = angleToTurn - angle1
    turn (finalAngleToTurn, speed)


# In[ ]:


go_to (B);

