
# coding: utf-8

# In[16]:


# Angles are in degrees regarding the funciton arguments and parameters


# In[1]:


import math
import pypot.dynamixel as pd

from test_moteur import *


# In[4]:



def calculate_angle(B, A, C):
    signe = 1

    AB = math.sqrt((B[0] - A[0])**2 + (B[1] - A[1])**2)

    if((B[1] - A[1]) > 0):
        signe = -1

    CB=math.sqrt((B[0] - C[0])**2 + (B[1] - C[1])**2)
    CA=math.sqrt((A[0] - C[0])**2 + (A[1] - C[1])**2)
    teta = signe * math.atan2(CB, CA)
    tetaDegre = math.degrees(teta)

    return(tetaDegre)

# In[6]:


# Returns the oblique distance between the two given points
def calculate_distance (A, B):
     return math.sqrt((B[0] - A[0])**2 + (B[1] - A[1])**2)


# In[7]:


def move_by (distance, speed):
    if (distance > 0):
        forward_by (distance, speed)
    else:
        backward_by (distance, speed)


# In[22]:


# Go to B =[x,y,finalAngle]] and speed in cm/s
def go_to (B, speed=10):
    x1, y1, angle1 = B[0], B[1], B[2]

    angleToTurn = calculate_angle ([x1,y1], [0,0], [0,y1])
    distance = calculate_distance ([0,0], [x1,y1])

    # arrival to destination point
    turn_by (angleToTurn, speed)
    move_by (distance, speed)

    # put the bot on the final desired angle
    finalAngleToTurn = angle1 - angleToTurn
    turn_by (finalAngleToTurn, speed)
