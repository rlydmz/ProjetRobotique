# coding: utf-8

###INTEGRATION Fonctions vision et moteur

import time
import TestFonctionV2 as cam
import test_moteur as tt
import go_to as move
import cv2 as cv
from sys import exit

vitesse=10


# Stop
def s ():
    move.stop()
    cam.cap.release()
    cv.destroyAllWindows()


# Parcours
def p (couleur,speed=20):
    if(couleur==0):
        while(True):
            try:
                debut=time.time()
                (coordonnes,angleFinal)=cam.noir()
                print("Coordonnes pointSuivant robot.py: ",coordonnes)
                
                pointSuivant=[(coordonnes[1]-320)*4/480,(480-coordonnes[0])*5.5/640,angleFinal]
            
                tt.turn_both_wheels(angleFinal,speed)
                
                fin=time.time()
                duree=fin-debut
                frequence=1/duree
                
                print ("frequence:", frequence)
                print("\n\n")

            except KeyboardInterrupt:
                s()
                sys.exit()

    if(couleur==1):
        while(True):
            try:
                debut=time.time()
                (coordonnes,angleFinal)=cam.rouge()
                print("Coordonnes pointSuivant robot.py: ",coordonnes)
                
                pointSuivant=[(coordonnes[1]-320)*4/480,(480-coordonnes[0])*5.5/640,angleFinal]
            
                tt.turn_both_wheels(angleFinal,speed)
                
                fin=time.time()
                duree=fin-debut
                frequence=1/duree
                
                print ("frequence:", frequence)
                print("\n\n")

            except KeyboardInterrupt:
                s()
                exit()
