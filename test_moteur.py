
# coding: utf-8

# In[2]:


import pypot.dynamixel as pd
#import keyboard as kb
import time
from sys import exit


def stop():
    dxl_io.set_moving_speed({1:0})
    dxl_io.set_moving_speed({2:0})

def forward(puissance=10):
    dxl_io.set_moving_speed({1:-puissance})
    dxl_io.set_moving_speed({2:puissance})

def backward(puissance=10):
    dxl_io.set_moving_speed({1:puissance})
    dxl_io.set_moving_speed({2:-puissance})

def turn(angle, puissance=10):
    signe = signeDe(angle)
    if angle == 0:
        avance(puissance)
    else:
        dxl_io.set_moving_speed({1:(signe*puissance)})
        dxl_io.set_moving_speed({2:(signe*puissance)})

def signeDe(nombre):
    if nombre >= 0:
        return 1
    else:
        return -1


def connect ():
    ports = pd.get_available_ports()
    if not ports:
        exit ('No port')
        print ("Found ports", ports)

    print('Connecting on the first available port:', ports[0])
    return pd.DxlIO(ports[0])


# In[30]:

def test ():

    dxl_io = connect ()
    dxl_io.set_wheel_mode([1])
    dxl_io.set_wheel_mode([2])

    stop()
    while True:
        avance(10)
        time.sleep(.500)
        recule(10)
        time.sleep(.500)
        tourne(90,10)
        time.sleep(.500)
        stop()
        time.sleep(1)



#stop()
#avance(10)
#recule(10)
#tourne(90,10)

# In[28]:


#dxl_io.scan(range(10))
