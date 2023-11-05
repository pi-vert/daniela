#Libraries
import sys
import time    #https://docs.python.org/fr/3/library/time.html
from adafruit_servokit import ServoKit    #https://circuitpython.readthedocs.io/projects/servokit/en/latest/
#Constants
nbPCAServo=16
#Parameters
MIN_IMP  =[500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500]
MAX_IMP  =[2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500]
MIN_ANG  =[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
MAX_ANG  =[180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180]
#Objects pca=ServoKit(channels=16, address=40)
pca = ServoKit(channels=16)

# Set
def pcaSet(motor,angle):
    if (angle < MIN_ANG[motor]):
        angle = MIN_ANG[motor]
    if (angle > MAX_ANG[motor]):
        angle = MIN_ANG[motor]        
    pca.servo[motor].angle = angle

def pcaStop(motor):
    pca.servo[motor].angle=None #disable channel
        
# Deplacement
def pcaMove(motor,angle1,angle2,step,sleep):
    if (angle1>angle2):
        angle = angle2
        while (angle<=angle1):
            print ( str(motor)+' '+str(angle) )
            pca.servo[motor].angle = angle
            angle = angle - step
            time.sleep(sleep)
    else:
        angle = angle1
        while (angle<=angle2):
            print ( str(motor)+' '+str(angle) )
            pca.servo[motor].angle = angle
            angle = angle + step
            time.sleep(sleep)

# Deplacement
def pcaRun(motor,angle1,angle2,speed):
    angle = angle1
    while angle < angle2:
        pca.servo[motor].angle = angle
        angle = angle + 0.01
        time.sleep(speed)
    while angle > angle1:
        pca.servo[motor].angle = angle
        angle = angle - 0.01
        time.sleep(speed)

# function init
def init():
    for i in range(nbPCAServo):
        pca.servo[i].set_pulse_width_range(MIN_IMP[i] , MAX_IMP[i])

def scenario():
    step = 0.05 
# M3  : commence à 100
    pcaMove(3, 10, 80, step, 0.001)
# M3 : descend à 30 lentement
    pcaMove(3, 80, 30, step, 0.01)
# M3 : 3 petits mouvements de bas en haut 30 - 60  - se bloque à 60
    pcaMove(3, 30, 60, step, 0.001)
    pcaMove(3, 60, 30, step, 0.001)
    pcaMove(3, 30, 60, step, 0.001)
    pcaMove(3, 60, 30, step, 0.001)
    pcaMove(3, 30, 60, step, 0.001)
# M2 : 2 petits mouvements vers la droite donc de 90 à 110 - revient à 90 (centre)
    pcaMove(2, 90, 110, step, 0.001)
    pcaMove(2, 100, 90, step, 0.001)
    pcaMove(2, 90, 110, step, 0.001)
    pcaMove(2, 100, 90, step, 0.001)
    pcaMove(2, 90, 110, step, 0.001)
    pcaMove(2, 100, 90, step, 0.001)
# M3 : descend à 30 lentement
    pcaMove(3, 60, 30, step, 0.01)
# M2 : 2 petits mouvements vers la droite donc de 90 à 110 - revient à 90 (centre)
    pcaMove(2, 90, 110, step, 0.001)
    pcaMove(2, 100, 90, step, 0.001)
    pcaMove(2, 90, 110, step, 0.001)
    pcaMove(2, 100, 90, step, 0.001)
# M3  : remonte brusquement à 100
    pcaMove(3, 30, 80, step, 0.0001)
# M2 : 2 petits mouvements lent de 80 à 110 - revient à 90 (centre)
    pcaMove(2, 80, 110, step, 0.001)
    pcaMove(2, 110, 80, step, 0.001)
    pcaMove(2, 80, 110, step, 0.001)
    pcaMove(2, 110, 80, step, 0.001)
    pcaMove(2, 80, 90, step, 0.001)
# M3 : descend à 45 lentement
    pcaMove(3, 80, 45, step, 0.001)
# M1 : 2 petits mouvements 40 - 50 retour au centre 45
    pcaMove(1, 40, 50, step, 0.001)
    pcaMove(1, 50, 40, step, 0.001)
    pcaMove(1, 40, 45, step, 0.001)
# M3 : descend à 35 lentement
    pcaMove(3, 45, 35, step, 0.01)
# M1 : 2 petits mouvements 40 - 50 retour au centre 45
    pcaMove(1, 40, 50, step, 0.001)
    pcaMove(1, 50, 40, step, 0.001)
    pcaMove(1, 40, 50, step, 0.001)
    pcaMove(1, 50, 40, step, 0.001)
    pcaMove(1, 40, 45, step, 0.001)
# M3 : descend à 20 lentement (se pose sur la feuille)
    pcaMove(3, 35, 20, step, 0.001)
# M1 : 1 petits mouvements 45 - 50 retour au centre 45
    pcaMove(1, 45, 50, step, 0.001)
    pcaMove(1, 50, 45, step, 0.001)
# pause
    time.sleep(1)
# M1 : 1 petits mouvements 45 - 50 retour au centre 45
# pause
    time.sleep(1)
# M1 : 1 petits mouvements 45 - 50 retour au centre 45
# pause
    time.sleep(1)
# M3 : remonte à 30 brusquement
    pcaMove(3, 20, 30, step, 0.001)
# M3 : descend à 20 lentement (se pose sur la feuille)
    pcaMove(3, 30, 20, step, 0.001)
# M3 : remonte à 40 brusquement
    pcaMove(3, 20, 40, step, 0.001)
# M3 : descend à 30 lentement 
    pcaMove(3, 40, 30, step, 0.1)
# M3 : remonte à 60 brusquement
    pcaMove(3, 30, 60, step, 0.001)
# M2 : 2 petits mouvements vers la droite donc de 90 à 110 - revient à 90 (centre)
    pcaMove(2, 90, 110, step, 0.01)
    pcaMove(2, 110, 90, step, 0.01)
    pcaMove(2, 90, 110, step, 0.01)
    pcaMove(2, 110, 90, step, 0.01)
# M3 : descend à 40 lentement 
    pcaMove(3, 60, 40, step, 0.1)
# M2 : 2 petits mouvements vers la droite donc de 90 à 110 - revient à 90 (centre)
    pcaMove(2, 90, 110, step, 0.01)
    pcaMove(2, 110, 90, step, 0.01)
    pcaMove(2, 90, 100, step, 0.01)
    pcaMove(2, 110, 90, step, 0.01)
# M3 : descend à 30 lentement 
    pcaMove(3, 60, 30, step, 0.1)
# M2 : 2 petits mouvements vers la droite donc de 90 à 110 - revient à 90 (centre)
    pcaMove(2, 90, 110, step, 0.01)
    pcaMove(2, 110, 90, step, 0.01)
    pcaMove(2, 90, 110, step, 0.01)
    pcaMove(2, 110, 90, step, 0.01)
# M3 : remonte à 40 brusquement
    pcaMove(3, 30, 40, step, 0.001)
# M1: 2 Grand balayement de gauche à droite 35- 55 retour au centre
    pcaMove(1, 35, 55, step, 0.01)
    pcaMove(1, 55, 35, step, 0.01)
    pcaMove(1, 35, 55, step, 0.01)
    pcaMove(1, 55, 35, step, 0.01)
# M3 : remonte à 60 brusquement
    pcaMove(3, 40, 60, step, 0.001)
# M1: 2 Grand balayement de gauche à droite 35- 55 retour au centre
    pcaMove(1, 35, 55, step, 0.01)
    pcaMove(1, 55, 35, step, 0.01)
    pcaMove(1, 35, 55, step, 0.01)
    pcaMove(1, 55, 35, step, 0.01)
    pcaMove(1, 35, 45, step, 0.01)
# M3 : descend à 30 lentement
    pcaMove(3, 60, 30, step, 0.1)
# M2 : 2 petits mouvements vers la droite donc de 90 à 110 - revient à 90 (centre)
    pcaMove(2, 90, 110, step, 0.01)
    pcaMove(2, 110, 90, step, 0.01)
    pcaMove(2, 90, 110, step, 0.01)
    pcaMove(2, 110, 90, step, 0.01)
# M3 : descend à 20 lentement (se pose sur la feuille)
    pcaMove(3, 30, 20, step, 0.1)
# M1 : 1 petits mouvements 45 - 50 retour au centre 45
    pcaMove(1, 45, 50, step, 0.01)
    pcaMove(1, 50, 45, step, 0.01)
# pause
    time.sleep(1)
# M1 : 1 petits mouvements 45 - 50 retour au centre 45
    pcaMove(1, 45, 50, step, 0.01)
    pcaMove(1, 50, 45, step, 0.01)
# pause
    time.sleep(1)
# M1 : 1 petits mouvements 45 - 50 retour au centre 45
    pcaMove(1, 45, 50, step, 0.01)
    pcaMove(1, 50, 45, step, 0.01)
# pause
    time.sleep(1)
# M3 : remonte à 30 brusquement
    pcaMove(3, 20, 30, step, 0.001)
# M3 : descend à 20 lentement (se pose sur la feuille)
    pcaMove(3, 30, 20, step, 0.1)
# M3 : remonte à 40 brusquement
    pcaMove(3, 20, 40, step, 0.001)
# M3 : descend à 30 lentement 
    pcaMove(3, 40, 30, step, 0.1)
# M3 : remonte à 60 brusquement
    pcaMove(3, 30, 60, step, 0.001)
# M3 : descend à 30 lentement 
    pcaMove(3, 60, 30, step, 0.1)
# M2 : 2 petits mouvements vers la droite donc de 90 à 110 - revient à 90 (centre)
    pcaMove(2, 90, 110, step, 0.001)
    pcaMove(2, 110, 90, step, 0.001)
    pcaMove(2, 90, 110, step, 0.001)
    pcaMove(2, 110, 90, step, 0.001)
# M3 : remonte à 70 brusquement
    pcaMove(3, 60, 70, step, 0.001)
# M3 : descend à 25 lentement 
    pcaMove(3, 70, 25, step, 0.1)
# M3 : remonte à 80 brusquement
    pcaMove(3, 25, 80, step, 0.001)
# M2 : 2 petits mouvements vers la droite donc de 90 à 110 - revient à 90 (centre)
    pcaMove(2, 90, 110, step, 0.001)
    pcaMove(2, 110, 90, step, 0.001)
# M1 : 3 petits mouvements 45 - 50 retour au centre 45
    pcaMove(1, 45, 50, step, 0.01)
    pcaMove(1, 50, 45, step, 0.01)
    pcaMove(1, 45, 50, step, 0.01)
    pcaMove(1, 50, 45, step, 0.01)
    pcaMove(1, 45, 50, step, 0.01)
    pcaMove(1, 50, 45, step, 0.01)
# M3 : descend à 30 lentement 
    pcaMove(3, 80, 30, step, 0.1)
# M3 : remonte à 60 brusquement
    pcaMove(3, 30, 60, step, 0.001)
# M2 : 2 petits mouvements vers la droite donc de 90 à 110 - revient à 90 (centre)
    pcaMove(2, 90, 110, step, 0.001)
    pcaMove(2, 110, 90, step, 0.001)
    pcaMove(2, 90, 110, step, 0.001)
    pcaMove(2, 110, 90, step, 0.001)
# M3 : descend à 30 lentement 
    pcaMove(3, 60, 30, step, 0.1)
# M2 : 2 petits mouvements vers la droite donc de 90 à 110 - revient à 90 (centre)
    pcaMove(2, 90, 110, step, 0.001)
    pcaMove(2, 110, 90, step, 0.001)
    pcaMove(2, 90, 110, step, 0.001)
    pcaMove(2, 110, 90, step, 0.001)
# M1 : 3 petits mouvements 45 - 50 retour au centre 45
    pcaMove(1, 45, 50, step, 0.01)
    pcaMove(1, 50, 45, step, 0.01)
    pcaMove(1, 45, 50, step, 0.01)
    pcaMove(1, 50, 45, step, 0.01)
    pcaMove(1, 45, 50, step, 0.01)
    pcaMove(1, 50, 45, step, 0.01)
# M3 : remonte à 80 brusquement
    pcaMove(3, 30, 80, step, 0.001)
# M3 : descend à 40 brusquement
    pcaMove(3, 80, 40, step, 0.001)
# M2 : 2 petits mouvements vers la droite donc de 90 à 110 - revient à 90 (centre)
    pcaMove(2, 90, 110, step, 0.001)
    pcaMove(2, 110, 90, step, 0.001)
    pcaMove(2, 90, 110, step, 0.001)
    pcaMove(2, 110, 90, step, 0.001)
# M1 : 3 petits mouvements 45 - 50 retour au centre 45
    pcaMove(1, 45, 50, step, 0.01)
    pcaMove(1, 50, 45, step, 0.01)
    pcaMove(1, 45, 50, step, 0.01)
    pcaMove(1, 50, 45, step, 0.01)
    pcaMove(1, 45, 50, step, 0.01)
    pcaMove(1, 50, 45, step, 0.01)
# M3 : remonte à 80 brusquement
    pcaMove(3, 40, 80, step, 0.001)
# M3 : descend à 30 brusquement
    pcaMove(3, 80, 30, step, 0.001)
# M2 : 2 petits mouvements vers la droite donc de 90 à 110 - revient à 90 (centre)
    pcaMove(2, 90, 110, step, 0.001)
    pcaMove(2, 110, 90, step, 0.001)
    pcaMove(2, 90, 110, step, 0.001)
    pcaMove(2, 110, 90, step, 0.001)
# M1 : 3 petits mouvements 45 - 50 retour au centre 45
    pcaMove(1, 45, 50, step, 0.01)
    pcaMove(1, 50, 45, step, 0.01)
    pcaMove(1, 45, 50, step, 0.01)
    pcaMove(1, 50, 45, step, 0.01)
# M3 : remonte à 45 brusquement
    pcaMove(3, 30, 45, step, 0.001)
# M3 : descend à 30 brusquement
    pcaMove(3, 45, 30, step, 0.001)
# M2 : 2 petits mouvements vers la droite donc de 90 à 110 - revient à 90 (centre)
    pcaMove(2, 90, 110, step, 0.001)
    pcaMove(2, 110, 90, step, 0.001)
    pcaMove(2, 90, 110, step, 0.001)
    pcaMove(2, 110, 90, step, 0.001)
# M1 : 3 petits mouvements 45 - 50 retour au centre 45
    pcaMove(1, 45, 50, step, 0.01)
    pcaMove(1, 50, 45, step, 0.01)
    pcaMove(1, 45, 50, step, 0.01)
    pcaMove(1, 50, 45, step, 0.01)
    pcaMove(1, 45, 50, step, 0.01)
    pcaMove(1, 50, 45, step, 0.01)
# M3 : descend à 20 brusquement sur la feuille
    pcaMove(3, 30, 20, step, 0.001)
# M1 : 2 petits mouvements 45 - 50 retour au centre 45
    pcaMove(1, 45, 50, step, 0.01)
    pcaMove(1, 50, 45, step, 0.01)
    pcaMove(1, 45, 50, step, 0.01)
    pcaMove(1, 50, 45, step, 0.01)
# pause
    time.sleep(1)
# M1 : 2 grands mouvements 45 - 50 retour au centre 45
    pcaMove(1, 45, 50, step, 0.01)
    pcaMove(1, 50, 45, step, 0.01)
    pcaMove(1, 45, 50, step, 0.01)
    pcaMove(1, 50, 45, step, 0.01)
# M3 : remonte à 30 brusquement
    pcaMove(3, 20, 30, step, 0.001)
# M3 : descend à 20 brusquement sur la feuille
    pcaMove(3, 30, 20, step, 0.001)
# M1 : 2 petits mouvements 45 - 50 retour au centre 45
    pcaMove(1, 45, 50, step, 0.01)
    pcaMove(1, 50, 45, step, 0.01)
    pcaMove(1, 45, 50, step, 0.01)
    pcaMove(1, 50, 45, step, 0.01)
# pause
    time.sleep(1)
# M1 : 2 grands mouvements 40 - 50 retour au centre 45
    pcaMove(1, 40, 50, step, 0.01)
    pcaMove(1, 50, 40, step, 0.01)
    pcaMove(1, 40, 50, step, 0.01)
    pcaMove(1, 50, 40, step, 0.01)
# M1 : 3 grands mouvements 45 - 55 retour au centre 45
    pcaMove(1, 45, 55, step, 0.01)
    pcaMove(1, 55, 45, step, 0.01)
    pcaMove(1, 45, 55, step, 0.01)
    pcaMove(1, 55, 45, step, 0.01)
    pcaMove(1, 45, 55, step, 0.01)
    pcaMove(1, 55, 45, step, 0.01)
# M1 : 2 grands mouvements 40 - 50 retour au centre 45
    pcaMove(1, 40, 50, step, 0.01)
    pcaMove(1, 50, 40, step, 0.01)
    pcaMove(1, 40, 50, step, 0.01)
    pcaMove(1, 50, 40, step, 0.01)
# pause
    time.sleep(1)
# M1 : 2 petit mouvements 45 - 50   retour au centre 45
    pcaMove(1, 45, 50, step, 0.01)
    pcaMove(1, 50, 45, step, 0.01)
    pcaMove(1, 45, 50, step, 0.01)
    pcaMove(1, 50, 45, step, 0.01)
# M1 : 2 grands mouvements 40 - 50 retour au centre 45
    pcaMove(1, 40, 50, step, 0.01)
    pcaMove(1, 50, 40, step, 0.01)
    pcaMove(1, 40, 50, step, 0.01)
    pcaMove(1, 50, 40, step, 0.01)
# M1 : 3 grands mouvements 45 - 55 retour au centre 45
    pcaMove(1, 45, 55, step, 0.01)
    pcaMove(1, 55, 45, step, 0.01)
    pcaMove(1, 45, 55, step, 0.01)
    pcaMove(1, 55, 45, step, 0.01)
    pcaMove(1, 45, 55, step, 0.01)
    pcaMove(1, 55, 45, step, 0.01)
# M1 : 2 petit mouvements  45 - 50   retour au centre 45
    pcaMove(1, 45, 50, step, 0.01)
    pcaMove(1, 50, 45, step, 0.01)
    pcaMove(1, 45, 50, step, 0.01)
    pcaMove(1, 50, 45, step, 0.01)
# M3 : remonte à 30 brusquement
    pcaMove(3, 20, 30, step, 0.001)
# M3 : descend à 20 brusquement sur la feuille
    pcaMove(3, 30, 20, step, 0.001)

def stop():
    pcaSet(3,10);
    pcaSet(2,70);
    pcaSet(1,45);
    pcaSet(0,45);
    pcaStop(3);
    pcaStop(2);
    pcaStop(1);
    pcaStop(0);
    
# function main
def main():
    pcaSet(3,10)
    pcaSet(2,70)
    pcaSet(1,45)
    pcaSet(0,45)
    time.sleep(1)
    stop()
    
if __name__ == '__main__':
    init()
    main()
