# coding: utf-8

###INTEGRATION Fonctions vision et moteur

import time
import TestFonctionV2 as cam
import test_moteur as tt
import from_A_to_B as move
import cv2 as cv
from sys import exit

vitesse=10


def s ():
    move.stop()
    cam.cap.release()
    cv.destroyAllWindows()


def p():


    #Detection de la ligne noire
    while(True):
        try:
            debut=time.time()
            (coordonnes,angleFinal)=cam.noir()
            print("Coordonnes pointSuivant robot.py: ",coordonnes)
            pointSuivant=[(coordonnes[1]-320)*4/480,(480-coordonnes[0])*5.5/640,angleFinal]
            #move.go_to(pointSuivant,vitesse)
            #tt.forward()
            tt.turn_both_wheels(angleFinal)
            
            fin=time.time()
            duree=fin-debut
            frequence=1/duree
            
            print ("frequence:", frequence)
            print("\n\n")

        except KeyboardInterrupt:
            s()
            sys.exit()


"""
def goTo(xA,yA,angleDegre):
    #envoie le robot au point de coordonnee (xA,yA) avec un angle de angleDegre
    move.go_to(vitesse,[xA,yA,angleDegre])


def isAt():
    #a partir du point (0,0,0), decombien le robot s'est déplacé
"""

