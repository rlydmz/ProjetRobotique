# coding: utf-8

import numpy as np
import cv2 as cv
import math


def angle(point, largeur, longueur):
    B = point
    A = [largeur - 1, longueur // 2]
    C = [B[0], A[1]]
    signe = 1

    AB = math.sqrt((B[0] - A[0])**2 + (B[1] - A[1])**2)

    if((B[1] - A[1]) < 0):
        signe = -1

    CB=math.sqrt((B[0] - C[0])**2 + (B[1] - C[1])**2)
    CA=math.sqrt((A[0] - C[0])**2 + (A[1] - C[1])**2)
    teta = signe * math.atan2(CB, CA)
    tetaDegre = math.degrees(teta)

    return(tetaDegre)


def virage(img):
    largeur = img.shape[0]
    longueur = img.shape[1]

    # point 1 on le regarde au milieu de l'image: on fixele point Ã  largeur//2
    
    xFixe = [largeur//4,largeur // 2]
    points=np.zeros((xFixe[1]-xFixe[0],2))

    bordureG = [xFixe, 0]
    bordureD = [xFixe, 0]
    i=0
    for x in range (xFixe[0],xFixe[1]):
        for y in range(0, longueur - 1):
            if img[x, y] == 255:
                bordureG = [x, y]
                break

        for z in range(longueur - 1, bordureG[1], -1):
            if img[x, z] == 255:
                bordureD = [x, z]
                break
        points[i] = [x, (bordureD[1] + bordureG[1]) / 2]
        i+=1



    yMoy=0
    for a in range (points.shape[0]):
        yMoy=yMoy+points[a][1]
    yMoy=yMoy/(xFixe[1]-xFixe[0])
    print(yMoy)

    point=[(xFixe[1]+xFixe[0])//2,yMoy]
    print(point)
    """

    xMobile=50
    bordureG=[xMobile,0]
    bordureD=[xMobile,255]
    while(bordureD==[xMobile,255] and bordureG==[xMobile,0]):
        xMobile+=1
        for y in range(0,longueur-1):
            if img[xMobile,y]==255:
                bordureG=[xMobile,y]
                break

        for z in range(longueur-1,bordureG[1],-1):
            if img[xMobile,z]==255:
                    bordureD=[xMobile,z]
                    break
     
    point=[xMobile,(bordureD[1]+bordureG[1])/2]
    ####
    print(point)
    """
    #print ("bordureD", bordureD, "bordureG", bordureG)

    #point = [xFixe, (bordureD[1] + bordureG[1]) / 2]

    angleFinal = angle(point, largeur, longueur)
  
    # visuel
    for x in range(-15, 15):
        for y in range(-15, 15):
            if point[1] + y > 0 and point[1] + y <320:
                img[point[0] + x, point[1] + y] = 0
    cv.imshow('image', img)
    
    return (point, angleFinal)


cap = cv.VideoCapture(0)

ret=cap.set(3,320)
ret=cap.set(4,240)
# FONCTIONS COULEURS

# Suivi de ligne noire


def noir():
    # Capture des frames
    ret, frame = cap.read()
                       
    # Affichages des frames
    #cv.imshow('frame', frame)

    height = frame.shape[0]
    width = frame.shape[1]
    channels = frame.shape[2]
 
    # Gaussian blurring
    frame_blur = cv.GaussianBlur(frame, (5, 5), 0)
    #cv.imshow('frame_blur', frame_blur)

    # seuillage
    #ret2, frame_gray=cap.read(cv.IMREAD_GRAYSCALE)
    gray = cv.cvtColor(frame_blur, cv.COLOR_BGR2GRAY)
    cv.imshow("gray",gray)
    _, img_seuil = cv.threshold(gray, 100, 2555, cv.THRESH_BINARY_INV)

    #imgContour, contours, hierarchy = cv.findContours(img_seuil, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    #cv.drawContours(imgContour, contours, -1, (255,255,0), 3)

    #Ouverture = erosion + dilatation
    kernel = np.ones((15, 15), np.uint8)
    erosion = cv.erode(img_seuil, kernel, iterations=1)
    dilatation = cv.dilate(erosion, kernel, iterations=1)
  
    
    #cv.imshow('frame_gray', img_seuil)
    # cv.imshow('erosion',erosion)
#    cv.imshow('dilatation', dilatation)
    cv.waitKey(10)

    # detection de contours verticaux
    sobelx = cv.Sobel(dilatation, cv.CV_64F, 1, 0, ksize=5)
    #laplacian = cv.Laplacian(dilatation, cv.CV_64F)

    # cv.imshow('contour',sobelx)
    # detectionCourbe(dilatation,width)
    (coordonnees, angleFinal) = virage(dilatation)

    print("FONCTION NOIR() ", coordonnees, angleFinal)

    return (coordonnees, angleFinal)


def rouge():
    # Capture des frames
    ret, frame = cap.read()
                           
    # Affichages des frames
    #cv.imshow('frame', frame)

    height = frame.shape[0]
    width = frame.shape[1]
    channels = frame.shape[2]
     
    # Gaussian blurring
    frame_blur = cv.GaussianBlur(frame, (5, 5), 0)

    _,_,red = cv.split(frame_blur)
    #cv.imshow('red',red)
    # seuillage
    #_, img_seuil = cv.threshold(red, 50, 255, cv.THRESH_BINARY_INV)

    seuil=150.0
    ret,img_seuil= cv.threshold(red,seuil,255.0,cv.THRESH_BINARY)
    cv.imshow("seg_red",img_seuil)

    #imgContour, contours, hierarchy = cv.findContours(img_seuil, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    #cv.drawContours(imgContour, contours, -1, (255,255,0), 3)

    #Ouverture = erosion + dilatation
    kernel = np.ones((15, 15), np.uint8)
    erosion = cv.erode(img_seuil, kernel, iterations=1)
    dilatation = cv.dilate(erosion, kernel, iterations=1)
      
        
    #cv.imshow('frame_gray', img_seuil)
    # cv.imshow('erosion',erosion)
    cv.imshow('dilatation', dilatation)
    cv.waitKey(10)

    # detection de contours verticaux
    sobelx = cv.Sobel(dilatation, cv.CV_64F, 1, 0, ksize=5)
    #laplacian = cv.Laplacian(dilatation, cv.CV_64F)

    # cv.imshow('contour',sobelx)
    # detectionCourbe(dilatation,width)
    (coordonnees, angleFinal) = virage(dilatation)

    print("FONCTION ROUGE() ", coordonnees, angleFinal)

    return (coordonnees, angleFinal)


       
