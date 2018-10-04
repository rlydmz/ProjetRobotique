
# coding: utf-8

# In[2]:


import pypot.dynamixel as pd
import time
import math
import keyboard as kb
from sys import exit

KR = 1.339
NTS = 60/1.339

ROBOT_WIDTH = 15.3

PERIMETER = 16.3
RADIUS = PERIMETER/(2*math.pi)

DELTA_T = 0.05 #En secondes

def stop():
    dxl_io.set_moving_speed({1:0})
    dxl_io.set_moving_speed({2:0})

def forward(puissance=10):
    dxl_io.set_moving_speed({1:puissance})
    dxl_io.set_moving_speed({2:-puissance})

def turn_right(distance, speed=10): #speed en cm/s
    #print(distance)
    #print(distance/float(speed))
    value = NTS*speed/PERIMETER
    dxl_io.set_moving_speed({1:value})
    dxl_io.set_moving_speed({2:0})
    time.sleep(distance/float(speed))
    stop()

def turn_left(distance, speed=10): #speed en cm/s
    #print(distance)
    #print(distance/float(speed))
    value = NTS*speed/PERIMETER
    dxl_io.set_moving_speed({1:0})
    dxl_io.set_moving_speed({2:-value})
    time.sleep(distance/float(speed))
    stop()

def turn_both_wheels(leftWheelSpeed, rightWheelSpeed):
    dxl_io.set_moving_speed({1:leftWheelSpeed})
    dxl_io.set_moving_speed({2:-rightWheelSpeed})

def backward(puissance=10):
    dxl_io.set_moving_speed({1:-puissance})
    dxl_io.set_moving_speed({2:puissance})

def signeDe(nombre):
    if nombre >= 0:
        return 1
    else:
        return -1

def degreesToRadian(angle):
    return (angle*2*math.pi/360)

def valueToNTS(value):
    return 1.339*value/60

def valueToRPS(value):
    return valueToNTS(value)*2*math.pi

#####################################################################

def backward_by(distance, speed=10): #speed en cm/s
    value = NTS*speed/PERIMETER
    print(value)
    print(distance/float(speed))
    backward(value)
    print ("Backward_by:", distance, " cm with", speed, "cm/s")
    time.sleep(distance/float(speed))
    stop()


def forward_by(distance, speed=10): #speed en cm/s
    power = NTS*speed/PERIMETER
    #print(power)
    #print(distance/float(speed))
    forward(power)
    print ("Forward_by:", distance, " cm with", speed, "cm/s")
    time.sleep(distance/float(speed))
    stop()


def turn_by (angle, speed=10):
    signe = signeDe(angle)

    # Deal with angles over 360
    if signe == 1:
        angle %= 360
    else:
        angle %= -360

    wheel_dist = ROBOT_WIDTH*(abs(angle)*2*math.pi/360)

    print ("Turn_by:", angle, " degrees with", speed, "cm/s")

    if 0 <= angle <= 180 or -360 < -angle <= -180:
        turn_right (wheel_dist, speed)
    else:
        turn_left (wheel_dist, speed)


######################################################################

def odometry(dxl_io):
    dxl_io.set_joint_mode([1])
    dxl_io.set_joint_mode([2])
    dxl_io.set_wheel_mode([1])
    dxl_io.set_wheel_mode([2])

    last_time = int(round(time.time() * 1000))

    while True:
        if keyboard.is_pressed('s'):
            break
        delta_time = int(round(time.time() * 1000))-last_time
        movingSpeed1 = dxl_io.get_moving_speed([1])
        movingSpeed2 = dxl_io.get_moving_speed([2])
        wheelSpeed1 = movingSpeed1[0]*PERIMETER/NTS
        wheelSpeed2 = movingSpeed2[0]*PERIMETER/NTS
        dw1 = dw1 + wheelSpeed1*delta_time
        dw2 = dw2 + wheelSpeed2*delta_time
        time.sleep(DELTA_T)

    distance = 0
    #CALCUL DE LA DISTANCE
    return distance    

#######################################################################
def start():
    ports = pd.get_available_ports()
    if not ports:
        exit('No port')
    print ("Found ports", ports)

    print('Connecting on the first available port:', ports[0])
    dxl_io = pd.DxlIO(ports[0])

    dxl_io.set_wheel_mode([1])
    dxl_io.set_wheel_mode([2])

    return dxl_io


dxl_io = start()

distance = odometry(dxl_io)

print(distance)

#forward_by(24,10)
#turn(10,10)
#time.sleep(1)
#stop()

# In[28]:


#dxl_io.scan(range(10))
