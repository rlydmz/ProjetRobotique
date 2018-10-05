import numpy as np
import cv2 as cv
import math


"""def detectionCourbe(img,width):
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
        
"""
    
"""
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
"""

def angle(point, largeur, longueur):

    B=point
    A=[largeur-1,longueur//2]
    C=[B[0],A[1]]
    signe=1
    
    AB=math.sqrt((B[0]-A[0])**2+(B[1]-A[1])**2)
    
    if((B[1]-A[1])<0):
       signe=-1
       
    teta=signe*math.atan2(abs(B[1]-A[1]),abs(B[0]-A[0]))
    tetaDegre=math.degrees(teta)

    print(tetaDegre)
    return(tetaDegre)

    """
    B=point
    A=[largeur-1,longueur//2]
    C=[0,longueur//2]
    x1=B[0]-A[0]
    y1=B[1]-A[1]
    x2=C[0]-A[0]
    y2=C[1]-A[1]
    d=x2*y1-y2*x1

    print(d)

    angleRadian=math.acos(d/(math.sqrt(x1**2+y1**2)*math.sqrt(x2**2+y2**2)))
    angleDegre=math.degrees(angleRadian)
    
    print(angleDegre)
    #angleRadian=math.arccos(delta/(math.sqrt(v2[0]**2+v2[1]**2)))
    #angleDegre=math.degrees(angleRadian)
    """

def virage(img):
    largeur=img.shape[0]
    longueur=img.shape[1]
    i=0
    
    #point 1 on le regarde au milieu de l'image: on fixele point à largeur//2
    #xFixe=largeur//2
    xMobile
    bordureG=[xMobile,0]
    bordureD=[xMobile,0]

    #bordureG=[xFixe,0]
    #bordureD=[xFixe,0]

    ##Partie Fixe
    """
    for y in range(0,longueur-1):
        if img[xFixe,y]==255:
            bordureG=[xFixe,y]
            break

    for z in range(longueur-1,bordureG[1],-1):
        if img[xFixe,z]==255:
                bordureD=[xFixe,z]
                break
        
    point=[xFixe,(bordureD[1]+bordureG[1])/2]
    """
    
    ##Partie Mobile
     while(bordureG==[xMobile,255] & bordureD==[xMobile,0]):
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
    angleFinal=angle(point, largeur, longueur)

    #visuel
    for x in range(-15,15):
        for y in range(-15,15):
                if point[1]+y>0 & point[1]+y<640:
                   
                    img[point[0]+x,point[1]+y]=0
    
    cv.imshow('image',img)
    return (point,angleFinal)


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
        kernel = np.ones((7,7),np.uint8)
        erosion = cv.erode(img_seuil,kernel,iterations = 1)
        dilatation = cv.dilate(img_seuil,kernel,iterations = 1)

        #nettoyage
        ret,labels=cv.connectedComponents(dilatation)
        print(ret)

        cv.imshow('frame_gray',img_seuil)
        #cv.imshow('erosion',erosion)
        cv.imshow('dilatation',dilatation)

        #detection de contours verticaux
        sobelx = cv.Sobel(dilatation, cv.CV_64F,1,0,ksize=5)
        #laplacian = cv.Laplacian(dilatation, cv.CV_64F)

        #cv.imshow('contour',sobelx)
        #detectionCourbe(dilatation,width)

        (coordonnees,angleFinal)=virage(dilatation)
        

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

        return (coordonnees,angleFinal)

    # When everything done, release the capture
    cap.release()
    cv.destroyAllWindows()

"""
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
"""
