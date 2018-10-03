import numpy as np
import cv2 as cv
import math

def detectionCourbe(img,width):
    couloir=100
    zone=100
    ligneD=0
    ligneG=0
    for i in range(zone,0,-1):
        ligneD+=img[len(img)-zone,width//2+couloir]
        ligneG+=img[len(img)-zone,width//2-couloir]
    if (ligneD>5*255):
        print("Tourner a droite")
    elif (ligneG>5*255):
        print("Tourner a gauche")
    else:
        print ("Aller tout droit")
        
    

###FONCTIONS AUXILIAIRES

def det(A,B,C):
    x1=B[0]-A[0]
    y1=B[1]-A[1]
    x2=C[0]-A[0]
    y2=C[1]-A[1]
    d=x1*y2-y1*x2
    return d

def detectionParcours(frame,width):
    #positionRegard = len(frame)//3
    pointA = [0,0]
    pointB = [len(frame)//2,0]
    pointC = [len(frame)-1,0]
    while ((pointA[1]<width-1) & (frame[pointA[0],pointA[1]] == 0 )):
        pointA[1]+=1
    while ((pointB[1]<width-1) & (frame[pointB[0],pointB[1]] == 0 )):
           pointB[1]+=1
    while ((pointC[1]<width-1) & (frame[pointC[0],pointC[1]] == 0 )):
           pointC[1]+=1
    delta = det(pointA,pointB,pointC)
    print (delta)
    if frame[0,width//2]!=0:
        print('Aller tout droit')
    else:
        print('Attention,virage !')


cap = cv.VideoCapture(1)

###FONCTIONS COULEURS

##Suivi de ligne noire
def noir():
    while(True):
        # Capture des frames
        ret, frame = cap.read(cv.IMREAD_UNCHANGED)
        
        # Affichages des frames
        cv.imshow('frame',frame)

        height = frame.shape[0]
        width = frame.shape[1]
        channels = frame.shape[2]
        
        #Gaussian blurring
        frame_blur = cv.GaussianBlur(frame,(5,5),0)
        cv.imshow('frame_blur',frame_blur)
        
        #seuillage
        #ret2, frame_gray=cap.read(cv.IMREAD_GRAYSCALE)
        gray = cv.cvtColor(frame_blur, cv.COLOR_BGR2GRAY)
        _, img_seuil = cv.threshold(gray, 100, 2555, cv.THRESH_BINARY_INV);


        #imgContour, contours, hierarchy = cv.findContours(img_seuil, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        #cv.drawContours(imgContour, contours, -1, (255,255,0), 3)

        #Ouverture = erosion + dilatation
        kernel = np.ones((5,5),np.uint8)
        erosion = cv.erode(img_seuil,kernel,iterations = 1)
        dilatation = cv.dilate(img_seuil,kernel,iterations = 1)

        cv.imshow('frame_gray',img_seuil)
        #cv.imshow('erosion',erosion)

        #detection de contours verticaux
        sobelx = cv.Sobel(dilatation, cv.CV_64F,1,0,ksize=5)
        #laplacian = cv.Laplacian(dilatation, cv.CV_64F)

        cv.imshow('contour',sobelx)
        detectionCourbe(dilatation,width)


        """
        nbDivisions = 3
        Divisions = np.zeros((nbDivisions,nbDivisions))
        iter =0
        while (iter < nbDivisions):
            for i in range(iter*height//nbDivisions,height//nbDivisions+iter*height//nbDivisions):
                for j in range(iter

            iter++
        """

        """
        tabSeuil = [0,0,0]
        
        seuilSplit = np.split(img_seuil, 3)
        for index in range(len(seuilSplit)):
            tmpMatrix = seuilSplit[index]
            for i in range(len(tmpMatrix)):
                tabSeuil[index] += sum(tmpMatrix[i])
                     

        print(tabSeuil[0])
        print(tabSeuil[1])
        print(tabSeuil[2])
        """
            
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv.destroyAllWindows()

##Suivi de ligne rouge
def rouge():
    while(True):
        # Capture des frames
        ret, frame = cap.read(cv.IMREAD_UNCHANGED)
        # Affichages des frames
        cv.imshow('frame',frame)

        #Gaussian blurring
        frame_blur = cv.GaussianBlur(frame,(5,5),0)
        cv.imshow('frame_blur',frame_blur)

        #segmentation couleur
        blue,green,red = cv.split(frame_blur)
        cv.imshow('red',red)
    
        #seuillage
        #redFilter = cv.cvtColor(red, cv.COLOR_BGR2GRAY)
        _, img_seuilR = cv.threshold(red, 100, 255, cv.THRESH_BINARY);

        cv.imshow('red',img_seuilR)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv.destroyAllWindows()
