#Libraries
import sys
import time    #https://docs.python.org/fr/3/library/time.html
from adafruit_servokit import ServoKit    #https://circuitpython.readthedocs.io/projects/servokit/en/latest/
#Constants
nbPCAServo=4
#Parameters
MIN_IMP  =[500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500]
MAX_IMP  =[2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500]
MIN_ANG  =[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
MAX_ANG  =[180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180]
REF_ANG  =[90,90,70,10] 
SPEED = [ 0.001, 0.01, 0.1 ]
#Objects pca=ServoKit(channels=16, address=40)
pca = ServoKit(channels=16)

# Set
def pcaSet(motor,angle):
    angle = angle + REF_ANG[motor]
    if (angle < MIN_ANG[motor]):
        angle = MIN_ANG[motor]
    if (angle > MAX_ANG[motor]):
        angle = MIN_ANG[motor]        
    pca.servo[motor].angle = angle

def pcaStop(motor):
    pca.servo[motor].angle = REF_ANG[motor]
    pca.servo[motor].angle=None #disable channel
        
# Deplacement
def pcaMove(motor,angle1,angle2,speed):
    step = SPEED[speed] 
    angle1 = angle1 + REF_ANG[motor]
    angle2 = angle2 + REF_ANG[motor]
    print ( str(motor)+' '+str(speed)+' '+str(angle1)+' -> '+str(angle2) )
    if (angle1<angle2):
        angle = angle1
        while (angle<angle2):
            pca.servo[motor].angle = angle
            angle = angle + step 
    if (angle1>angle2):
        angle = angle2
        while (angle>angle1):
            pca.servo[motor].angle = angle
            angle = angle - step
            
# function init
def init():
    for i in range(nbPCAServo):
        pca.servo[i].set_pulse_width_range(MIN_IMP[i] , MAX_IMP[i])

def scenario():
    pcaMove(0, 0, 0, 1)
# M3  : commence à 100
    pcaMove(3, 20, 70, 1)
# M3 : descend à 30 lentement
    pcaMove(3, 70, 30, 0)
# M3 : 3 petits mouvements de bas en haut 30 - 60  - se bloque à 60
    pcaMove(3, 30, 60, 1)
    pcaMove(3, 60, 30, 1)
    pcaMove(3, 30, 60, 1)
    pcaMove(3, 60, 30, 1)
    pcaMove(3, 30, 60, 1)
    pcaMove(3, 60, 30, 1)
# M2 : 2 petits mouvements vers la droite donc de 90 à 110 - revient à 90 (centre)
    pcaMove(2, 0, 20, 1)
    pcaMove(2, 20, 0, 1)
    pcaMove(2, 0, 20, 1)
    pcaMove(2, 20, 0, 1)
# M3 : descend à 30 lentement
    pcaMove(3, 40, 30, 0)
# M2 : 2 petits mouvements vers la droite donc de 90 à 110 - revient à 90 (centre)
    pcaMove(2, 0, 20, 1)
    pcaMove(2, 20, 0, 1)
    pcaMove(2, 0, 20, 1)
    pcaMove(2, 20, 0, 1)
# M3  : remonte brusquement à 100
    pcaMove(3, 0, 60, 2)
# M2 : 2 petits mouvements lent de 80 à 110 - revient à 90 (centre)
    pcaMove(2, -10, 20, 0)
    pcaMove(2, 20, -10, 0)
    pcaMove(2, -10, 20, 0)
    pcaMove(2, 20, 0, 0)
# M3 : descend à 45 lentement
    pcaMove(3, 70, 35, 0)
# M1 : 2 petits mouvements 40 - 50 retour au centre 45
    pcaMove(1, -5, 5, 1)
    pcaMove(1, 5, -5, 1)
    pcaMove(1, -5, 0, 1)
# M3 : descend à 35 lentement
    pcaMove(3, 35, 25, 0)
# M1 : 2 petits mouvements 40 - 50 retour au centre 45
    pcaMove(1, -5, 5, 1)
    pcaMove(1, 5, -5, 1)
    pcaMove(1, -5, 5, 1)
    pcaMove(1, 5, -5, 1)
    pcaMove(1, -5, 0, 1)
# M3 : descend à 20 lentement (se pose sur la feuille)
    pcaMove(3, 25, 10, 0)
# M1 : 1 petits mouvements 45 - 50 retour au centre 45
    pcaMove(1, 5, -5, 1)
    pcaMove(1, -5, 0, 1)
# pause
    time.sleep(1)
# M1 : 1 petits mouvements 45 - 50 retour au centre 45
    pcaMove(1, 5, -5, 1)
    pcaMove(1, -5, 0, 1)
# pause
    time.sleep(1)
# M1 : 1 petits mouvements 45 - 50 retour au centre 45
# pause
    time.sleep(1)
# M3 : remonte à 30 brusquement
    pcaMove(3, 20, 50, 2)
# M3 : descend à 20 lentement (se pose sur la feuille)
    pcaMove(3, 50, 20, 0)
# M3 : remonte à 40 brusquement
    pcaMove(3, 20, 50, 2)
# M3 : descend à 30 lentement 
    pcaMove(3, 50, 20, 0)
# M3 : remonte à 60 brusquement
    pcaMove(3, 20, 50, 2)
# M2 : 2 petits mouvements vers la droite donc de 90 à 110 - revient à 90 (centre)
    pcaMove(2, 0, 20, 1)
    pcaMove(2, 20, 0, 1)
    pcaMove(2, 0, 20, 1)
    pcaMove(2, 20, 0, 1)
# M3 : descend à 40 lentement 
    pcaMove(3, 50, 30, 0)
# M2 : 2 petits mouvements vers la droite donc de 90 à 110 - revient à 90 (centre)
    pcaMove(2, 0, 20, 1)
    pcaMove(2, 20, 0, 1)
    pcaMove(2, 0, 20, 1)
    pcaMove(2, 20, 0, 1)
# M3 : descend à 30 lentement 
    pcaMove(3, 50, 20, 0)
# M2 : 2 petits mouvements vers la droite donc de 90 à 110 - revient à 90 (centre)
    pcaMove(2, 0, 20, 1)
    pcaMove(2, 20, 0, 1)
    pcaMove(2, 0, 20, 1)
    pcaMove(2, 20, 0, 1)
# M3 : remonte à 40 brusquement
    pcaMove(3, 20, 30, 2)
# M1: 2 Grand balayement de gauche à droite 35- 55 retour au centre
    pcaMove(1, -10, 10, 1)
    pcaMove(1, 10, -10, 1)
    pcaMove(1, -10, 10, 1)
    pcaMove(1, 10, -10, 1)
    pcaMove(1, -10, 0, 1)
# M3 : remonte à 60 brusquement
    pcaMove(3, 30, 50, 2)
# M1: 2 Grand balayement de gauche à droite 35- 55 retour au centre
    pcaMove(1, -10, 10, 1)
    pcaMove(1, 10, -10, 1)
    pcaMove(1, -10, 10, 1)
    pcaMove(1, 10, -10, 1)
    pcaMove(1, -10, 0, 1)
# M3 : descend à 30 lentement
    pcaMove(3, 60, 30, 0)
# M2 : 2 petits mouvements vers la droite donc de 90 à 110 - revient à 90 (centre)
    pcaMove(2, 0, 20, 1)
    pcaMove(2, 20, 0, 1)
    pcaMove(2, 0, 20, 1)
    pcaMove(2, 20, 0, 1)
# M3 : descend à 20 lentement (se pose sur la feuille)
    pcaMove(3, 20, 10, 0)
# M1 : 1 petits mouvements 45 - 50 retour au centre 45
    pcaMove(1, 0, 5, 1)
    pcaMove(1, 5, 0, 1)
# pause
    time.sleep(1)
# M1 : 1 petits mouvements 45 - 50 retour au centre 45
    pcaMove(1, 0, 5, 1)
    pcaMove(1, 5, 0, 1)
# pause
    time.sleep(1)
# M1 : 1 petits mouvements 45 - 50 retour au centre 45
    pcaMove(1, 0, 5, 1)
    pcaMove(1, 5, 0, 1)
# pause
    time.sleep(1)
# M3 : remonte à 30 brusquement
    pcaMove(3, 10, 20, 1)
# M3 : descend à 20 lentement (se pose sur la feuille)
    pcaMove(3, 20, 10, 0)
# M3 : remonte à 40 brusquement
    pcaMove(3, 10, 30, 2)
# M3 : descend à 30 lentement 
    pcaMove(3, 30, 20, 0)
# M3 : remonte à 60 brusquement
    pcaMove(3, 20, 50, 2)
# M3 : descend à 30 lentement 
    pcaMove(3, 50, 20, 0)
# M2 : 2 petits mouvements vers la droite donc de 90 à 110 - revient à 90 (centre)
    pcaMove(2, 0, 20, 1)
    pcaMove(2, 20, 0, 1)
    pcaMove(2, 0, 20, 1)
    pcaMove(2, 20, 0, 1)
# M3 : remonte à 70 brusquement
    pcaMove(3, 50, 60, 2)
# M3 : descend à 25 lentement 
    pcaMove(3, 60, 15, 0)
# M3 : remonte à 80 brusquement
    pcaMove(3, 15, 70, 2)
# M2 : 2 petits mouvements vers la droite donc de 90 à 110 - revient à 90 (centre)
    pcaMove(2, 0, 20, 1)
    pcaMove(2, 20, 0, 1)
# M1 : 3 petits mouvements 45 - 50 retour au centre 45
    pcaMove(1, -5, 5, 1)
    pcaMove(1, 5, -5, 1)
    pcaMove(1, -5, 5, 1)
    pcaMove(1, 5, -5, 1)
    pcaMove(2, 0, 20, 1)
    pcaMove(2, 20, 0, 1)
    pcaMove(1, -5, 0, 1)
# M3 : descend à 30 lentement 
    pcaMove(3, 70, 20, 0)
# M3 : remonte à 60 brusquement
    pcaMove(3, 20, 50, 2)
# M2 : 2 petits mouvements vers la droite donc de 90 à 110 - revient à 90 (centre)
    pcaMove(2, 0, 20, 1)
    pcaMove(2, 20, 0, 1)
    pcaMove(2, 0, 20, 1)
    pcaMove(2, 20, 0, 1)
# M3 : descend à 30 lentement 
    pcaMove(3, 50, 20, 0)
# M2 : 2 petits mouvements vers la droite donc de 90 à 110 - revient à 90 (centre)
    pcaMove(2, 0, 20, 1)
    pcaMove(2, 20, 0, 1)
    pcaMove(2, 0, 20, 1)
    pcaMove(2, 20, 0, 1)
# M1 : 3 petits mouvements 45 - 50 retour au centre 45
    pcaMove(1, -5, 5, 1)
    pcaMove(1, 5, -5, 1)
    pcaMove(1, -5, 5, 1)
    pcaMove(1, 5, -5, 1)
    pcaMove(1, -5, 0, 1)
# M3 : remonte à 80 brusquement
    pcaMove(3, 20, 70, 2)
# M3 : descend à 40 brusquement
    pcaMove(3, 70, 30, 2)
# M2 : 2 petits mouvements vers la droite donc de 90 à 110 - revient à 90 (centre)
    pcaMove(2, 0, 20, 1)
    pcaMove(2, 20, 0, 1)
    pcaMove(2, 0, 20, 1)
    pcaMove(2, 20, 0, 1)
# M1 : 3 petits mouvements 45 - 50 retour au centre 45
    pcaMove(1, -5, 5, 1)
    pcaMove(1, 5, -5, 1)
    pcaMove(1, -5, 5, 1)
    pcaMove(1, 5, -5, 1)
    pcaMove(1, -5, 0, 1)
# M3 : remonte à 80 brusquement
    pcaMove(3, 30, 70, 2)
# M3 : descend à 30 brusquement
    pcaMove(3, 70, 20, 2)
# M2 : 2 petits mouvements vers la droite donc de 90 à 110 - revient à 90 (centre)
    pcaMove(2, 0, 20, 1)
    pcaMove(2, 20, 0, 1)
    pcaMove(2, 0, 20, 1)
    pcaMove(2, 20, 0, 1)
# M1 : 3 petits mouvements 45 - 50 retour au centre 45
    pcaMove(1, -5, 5, 1)
    pcaMove(1, 5, -5, 1)
    pcaMove(1, -5, 5, 1)
    pcaMove(1, 5, -5, 1)
    pcaMove(1, -5, 0, 1)
# M3 : remonte à 45 brusquement
    pcaMove(3, 20, 35, 2)
# M3 : descend à 30 brusquement
    pcaMove(3, 35, 20, 2)
# M2 : 2 petits mouvements vers la droite donc de 90 à 110 - revient à 90 (centre)
    pcaMove(2, 0, 20, 1)
    pcaMove(2, 20, 0, 1)
    pcaMove(2, 0, 20, 1)
    pcaMove(2, 20, 0, 1)
# M1 : 3 petits mouvements 45 - 50 retour au centre 45
    pcaMove(1, -5, 5, 1)
    pcaMove(1, 5, -5, 1)
    pcaMove(1, -5, 5, 1)
    pcaMove(1, 5, -5, 1)
    pcaMove(1, -5, 5, 1)
    pcaMove(1, 5, -5, 1)
    pcaMove(1, -5, 0, 1)
# M3 : descend à 20 brusquement sur la feuille
    pcaMove(3, 20, 10, 2)
# M1 : 2 petits mouvements 45 - 50 retour au centre 45
    pcaMove(1, -5, 5, 1)
    pcaMove(1, 5, -5, 1)
    pcaMove(1, -5, 5, 1)
    pcaMove(1, 5, -5, 1)
    pcaMove(1, -5, 0, 1)
# pause
    time.sleep(1)
# M1 : 2 grands mouvements 45 - 50 retour au centre 45
    pcaMove(1, -5, 5, 1)
    pcaMove(1, 5, -5, 1)
    pcaMove(1, -5, 5, 1)
    pcaMove(1, 5, -5, 1)
    pcaMove(1, -5, 0, 1)
# M3 : remonte à 30 brusquement
    pcaMove(3, 10, 20, 2)
# M3 : descend à 20 brusquement sur la feuille
    pcaMove(3, 20, 10, 2)
# M1 : 2 petits mouvements 45 - 50 retour au centre 45
    pcaMove(1, -5, 5, 1)
    pcaMove(1, 5, -5, 1)
    pcaMove(1, -5, 5, 1)
    pcaMove(1, 5, -5, 1)
    pcaMove(1, -5, 0, 1)
# pause
    time.sleep(1)
# M1 : 2 grands mouvements 40 - 50 retour au centre 45
    pcaMove(1, -5, 5, 1)
    pcaMove(1, 5, -5, 1)
    pcaMove(1, -5, 5, 1)
    pcaMove(1, 5, -5, 1)
    pcaMove(1, -5, 0, 1)
# M1 : 3 grands mouvements 45 - 55 retour au centre 45
    pcaMove(1, -10, 10, 1)
    pcaMove(1, 10, -10, 1)
    pcaMove(1, -10, 10, 1)
    pcaMove(1, 10, -10, 1)
    pcaMove(1, -10, 10, 1)
    pcaMove(1, 10, -10, 1)
    pcaMove(1, -10, 0, 1)
# M1 : 2 grands mouvements 40 - 50 retour au centre 45
    pcaMove(1, -5, 5, 1)
    pcaMove(1, 5, -5, 1)
    pcaMove(1, -5, 5, 1)
    pcaMove(1, 5, -5, 1)
    pcaMove(1, -5, 0, 1)
# pause
    time.sleep(1)
# M1 : 2 petit mouvements 45 - 50   retour au centre 45
    pcaMove(1, -5, 5, 1)
    pcaMove(1, 5, -5, 1)
    pcaMove(1, -5, 5, 1)
    pcaMove(1, 5, -5, 1)
    pcaMove(1, -5, 0, 1)
# M1 : 2 grands mouvements 40 - 50 retour au centre 45
    pcaMove(1, -10, 10, 1)
    pcaMove(1, 10, -10, 1)
    pcaMove(1, -10, 10, 1)
    pcaMove(1, 10, -10, 1)
    pcaMove(1, -10, 10, 1)
    pcaMove(1, 10, -10, 1)
    pcaMove(1, -10, 0, 1)
# M1 : 3 grands mouvements 45 - 55 retour au centre 45
    pcaMove(1, 0, 10, 1)
    pcaMove(1, 10, 0, 1)
    pcaMove(1, 0, 10, 1)
    pcaMove(1, 10, 0, 1)
    pcaMove(1, 0, 10, 1)
    pcaMove(1, 10, 0, 1)
# M1 : 2 petit mouvements  45 - 50   retour au centre 45
    pcaMove(1, -10, 10, 1)
    pcaMove(1, 10, -10, 1)
    pcaMove(1, -10, 10, 1)
    pcaMove(1, 10, -10, 1)
    pcaMove(1, -10, 0, 1)
# M3 : remonte à 30 brusquement
    pcaMove(3, 0, 20, 2)
# M3 : descend à 20 brusquement sur la feuille
    pcaMove(3, 20, 0, 2)

# function main
def main():
    pcaSet(0,0);
    pcaSet(1,0);
    pcaSet(2,0);
    pcaSet(3,0);
    scenario()
    pcaStop(3);
    pcaStop(2);
    pcaStop(1);
    pcaStop(0);
    
if __name__ == '__main__':
    init()
    main()
