
# coding: utf-8

# In[2]:


import pypot.dynamixel as pd
import time
import math
from sys import exit

KR = 1.339
NTS = 60/1.339

ROBOT_WIDTH = 15.3

PERIMETER = 16.3
RADIUS = PERIMETER/(2*math.pi)

def stop():
    dxl_io.set_moving_speed({1:0})
    dxl_io.set_moving_speed({2:0})

def forward(puissance=10):
    dxl_io.set_moving_speed({1:puissance})
    dxl_io.set_moving_speed({2:-puissance})

def forward_by(distance, speed): #speed en cm/s
    value = NTS*speed/PERIMETER
    print(value)
    print(distance/float(speed))
    forward(value)
    time.sleep(distance/float(speed))
    stop()

def turn_by(distance, speed): #speed en cm/s
    print(distance)
    print(distance/float(speed))
    value = NTS*speed/PERIMETER
    dxl_io.set_moving_speed({1:value})
    dxl_io.set_moving_speed({2:0})
    time.sleep(distance/float(speed))
    stop()

def backward(puissance=10):
    dxl_io.set_moving_speed({1:-puissance})
    dxl_io.set_moving_speed({2:puissance})

def backward_by(distance, speed): #speed en cm/s
    value = NTS*speed/PERIMETER
    print(value)
    print(distance/float(speed))
    backward(value)
    time.sleep(distance/float(speed))
    stop()

def turn(angle, puissance=10):
    signe = signeDe(angle)
    if angle == 0:
        forward(puissance)
        time.sleep(0.5)
    else:
        print(angle*2*math.pi/360)
        wheel_dist = ROBOT_WIDTH*(angle*2*math.pi/360)
        print(puissance)
        turn_by(wheel_dist, puissance)

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


ports = pd.get_available_ports()
if not ports:
    exit('No port')
print ("Found ports", ports)

print('Connecting on the first available port:', ports[0])
dxl_io = pd.DxlIO(ports[0])

dxl_io.set_wheel_mode([1])
dxl_io.set_wheel_mode([2])


#forward_by(24,10)
#turn(10,10)
#time.sleep(1)
#stop()

# In[28]:


#dxl_io.scan(range(10))
