# coding: utf-8

###INTEGRATION Fonctions vision et moteur

import time
import TestFonctionV2 as cam
import from_A_to_B as move

vitesse=10

def parcours():
    #Detection de la ligne noire
    while(True):
        debut=time.time()
        (coordonnes,angleFinal)=cam.noir()
        pointSuivant=[coordonnes[0]/float(120),coordonnes[1]/float(116),angleFinal]
        move.go_to(pointSuivant,vitesse)
        fin=time.time()
        duree=fin-debut
        frequence=1/duree
        #print(frequence)
        
    
    
"""
def goTo(xA,yA,angleDegre):
    #envoie le robot au point de coordonnee (xA,yA) avec un angle de angleDegre
    move.go_to(vitesse,[xA,yA,angleDegre])

    
def isAt():
    #a partir du point (0,0,0), decombien le robot s'est déplacé
"""
