import numpy
import cv2 as cv
import math

cap = cv.VideoCapture(1)

###CAPTURE VIDEO


while(True):
    # Capture des frames
    ret, frame = cap.read(cv.IMREAD_UNCHANGED)
    # Our operations on the frame come here
    #gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv.imshow('frame',frame)
    #cv.imshow('frame',gray)

    #seuillage
    ret2, frame_gray=cap.read(cv.IMREAD_GRAYSCALE)
    gray = cv.cvtColor(frame_gray, cv.COLOR_BGR2GRAY)
    _, img_seuil = cv.threshold(gray, 100, 255, cv.THRESH_BINARY);

    height = frame.shape[0]
    width = frame.shape[1]
    channels = frame.shape[2]
    
    cv.imshow('frame_gray',img_seuil)

    #Gaussian blurring
    frame_blur = cv.GaussianBlur(frame_gray,(5,5),0)
    cv.imshow('frame_blur',frame_blur)

    #HSV
    hsv = cv.cvtColor(frame_blur,cv.COLOR_BGR2HSV)
    cv.imshow('hsv',hsv)

    #segmentation couleur
    blue,green,red = cv.split(frame_blur)
    cv.imshow('red',red)
    cv.imshow('blue',blue)
    cv.imshow('green',green)

    #seuillage par couleur
    #Rouge
    #gray = cv.cvtColor(frame_gray, cv.COLOR_BGR2GRAY)
    #_, img_seuilR = cv.threshold(gray, 100, 255, cv.THRESH_BINARY);  
    #cv.imshow('red',img_seuilR)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()


    
