
# coding: utf-8

# In[2]:


import pypot.dynamixel as pd


# In[3]:


ports = pd.get_available_ports()
if not ports:
    exit('No port')
print ("Found ports", ports)

print('Connecting on the first available port:', ports[0])
dxl_io = pd.DxlIO(ports[0])


# In[30]:


dxl_io.set_wheel_mode([1])
dxl_io.set_wheel_mode([2])
dxl_io.set_moving_speed({1:0})
dxl_io.set_moving_speed({2:0})

# In[28]:


#dxl_io.scan(range(10))



def avance(puissance=10):
    dxl_io.set_moving_speed({1:-puissance})
    dxl_io.set_moving_speed({2:puissance})

def recule(puissance=10):
    dxl_io.set_moving_speed({1:puissance})
    dxl_io.set_moving_speed({2:-puissance})

def tourne(puissance, angle):
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