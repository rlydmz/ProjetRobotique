# coding utf-8

import pypot.dynamixel as pd
import time
import math
#import keyboard as kb
from sys import exit

from test_moteur import *


DELTA_T = 0.05 #En secondes


######################################################################


def reset_mode(dxl_io):
    dxl_io.set_joint_mode([1])
    dxl_io.set_joint_mode([2])    
    dxl_io.set_wheel_mode([1])
    dxl_io.set_wheel_mode([2])

    
def odometry(dxl_io):
    y1=0
    x1=0
    teta=0
    
    last_time = int(round(time.time() * 1000))

    while True:
        #if kb.is_pressed('s'):
            #break
        delta_time = (int(round(time.time() * 1000))-last_time)/float(1000)
        last_time = int(round(time.time() * 1000))
        movingSpeed1 = dxl_io.get_present_speed([1])
        movingSpeed2 = dxl_io.get_present_speed([2])
        #GAUCHE ID 1 --- DROITE ID 2
        wheelSpeed1 = movingSpeed1[0]*PERIMETER/NTS
        wheelSpeed2 = movingSpeed2[0]*PERIMETER/NTS
        wheelSpeed2 *= -1
        dw1 = wheelSpeed1*delta_time
        dw2 = wheelSpeed2*delta_time
        if (dw1>dw2):
            dTeta = (dw1-dw2)/ROBOT_WIDTH
            X=(ROBOT_WIDTH*dw2)/(dw1-dw2)
            dy=(X+ROBOT_WIDTH/float(2))*math.sin(dTeta)
            dx=(X+ROBOT_WIDTH/float(2))*(1-math.cos(dTeta))
            y1+=dy*math.cos(teta)-math.sin(teta)*dx
            x1+=dy*math.sin(teta)+math.cos(teta)*dx
            teta+=dTeta
        elif (dw2>dw1):
            dTeta = (dw2-dw1)/ROBOT_WIDTH
            X=(ROBOT_WIDTH*dw1)/(dw2-dw1)
            dy=(X+ROBOT_WIDTH/float(2))*math.sin(dTeta)
            dx=(X+ROBOT_WIDTH/float(2))*(1-math.cos(dTeta))
            y1+=dy*math.cos(teta)-math.sin(teta)*dx
            x1+=dy*math.sin(teta)+math.cos(teta)*dx
            teta-=dTeta
        else:
            y1+=math.cos(teta)*dw1
            x1+=dw1*math.sin(teta)

        print("X = ",x1)
        print("Y = ",y1)
        print("ANGLE = ",teta*360/(2*math.pi))
        print ("\n")
        print ("R =",math.sqrt (x1*x1+y1*y1))
        print ("ANGLE POLAIRE =",math.degrees(math.atan2(y1,x1))) 
        
        time.sleep(DELTA_T)

#######################################################################

odometry (dxl_io)
