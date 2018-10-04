angle = 250

if angle >= 0:
    angle %= 360
else:
    angle %= -360

print(angle)