import numpy as np
import cv2 as cv
import math


###FONCTIONS COULEURS

cap = cv.VideoCapture(1)

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
        _, img_seuil = cv.threshold(gray, 100, 255, cv.THRESH_BINARY);

        imgContour, contours, hierarchy = cv.findContours(img_seuil, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        cv.drawContours(imgContour, contours, -1, (255,255,0), 3)

        cv.imshow('frame_gray',img_seuil)

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
