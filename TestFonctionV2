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

    teta = signe * math.atan2(abs(B[1] - A[1]), abs(B[0] - A[0]))
    tetaDegre = math.degrees(teta)

    print(tetaDegre)
    return(tetaDegre)


def virage(img):
    largeur = img.shape[0]
    longueur = img.shape[1]

    # point 1 on le regarde au milieu de l'image: on fixele point à largeur//2
    xFixe = largeur // 2

    bordureG = [xFixe, 0]
    bordureD = [xFixe, 0]

    for y in range(0, longueur - 1):
        if img[xFixe, y] == 255:
            bordureG = [xFixe, y]
            break

    for z in range(longueur - 1, bordureG[1], -1):
        if img[xFixe, z] == 255:
            bordureD = [xFixe, z]
            break

    point = [xFixe, (bordureD[1] + bordureG[1]) / 2]

    angleFinal = angle(point, largeur, longueur)

    # visuel
    for x in range(-15, 15):
        for y in range(-15, 15):
            if point[1] + y > 0 & point[1] + y < 640:

                img[point[0] + x, point[1] + y] = 0

    cv.imshow('image', img)
    return (point, angleFinal)


cap = cv.VideoCapture(1)

# FONCTIONS COULEURS

# Suivi de ligne noire


def noir():
    while(True):
        # Capture des frames
        ret, frame = cap.read(cv.IMREAD_UNCHANGED)

        # Affichages des frames
        cv.imshow('frame', frame)

        height = frame.shape[0]
        width = frame.shape[1]
        channels = frame.shape[2]

        # Gaussian blurring
        frame_blur = cv.GaussianBlur(frame, (5, 5), 0)
        cv.imshow('frame_blur', frame_blur)

        # seuillage
        #ret2, frame_gray=cap.read(cv.IMREAD_GRAYSCALE)
        gray = cv.cvtColor(frame_blur, cv.COLOR_BGR2GRAY)
        _, img_seuil = cv.threshold(gray, 100, 2555, cv.THRESH_BINARY_INV)

        #imgContour, contours, hierarchy = cv.findContours(img_seuil, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        #cv.drawContours(imgContour, contours, -1, (255,255,0), 3)

        #Ouverture = erosion + dilatation
        kernel = np.ones((7, 7), np.uint8)
        erosion = cv.erode(img_seuil, kernel, iterations=1)
        dilatation = cv.dilate(img_seuil, kernel, iterations=1)

        # nettoyage
        ret, labels = cv.connectedComponents(dilatation)
        print(ret)

        cv.imshow('frame_gray', img_seuil)
        # cv.imshow('erosion',erosion)
        cv.imshow('dilatation', dilatation)

        # detection de contours verticaux
        sobelx = cv.Sobel(dilatation, cv.CV_64F, 1, 0, ksize=5)
        #laplacian = cv.Laplacian(dilatation, cv.CV_64F)

        # cv.imshow('contour',sobelx)
        # detectionCourbe(dilatation,width)

        (coordonnees, angleFinal) = virage(dilatation)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break

        return (coordonnees, angleFinal)

    # When everything done, release the capture
    cap.release()
    cv.destroyAllWindows()
