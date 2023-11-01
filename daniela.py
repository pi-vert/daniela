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
    if (angle >= MIN_ANG[motor] and angle <= MAX_ANG[motor]):
        pca.servo[motor].angle = angle
    else:
        pca.servo[motor].angle=None #disable channel
        
# Deplacement
def pcaMove(motor,angle1,angle2):
    if (angle1 < angle2):
        angle = angle1
        while angle < angle2:
            pca.servo[motor].angle = angle
            angle = angle + 1
            time.sleep(0.05)
    else:
        angle = angle2
        while angle > angle1:
            pca.servo[motor].angle = angle
            angle = angle - 1
            time.sleep(0.05)

# function init
def init():
    for i in range(nbPCAServo):
        pca.servo[i].set_pulse_width_range(MIN_IMP[i] , MAX_IMP[i])
    pcaSet(0,90);
    pcaSet(1,90);
    pcaSet(2,70);
    pcaSet(3,90);
    
# function main
def main():
    while true:
        pcaMove(2,70,120);
        pcaMove(2,120,70);

if __name__ == '__main__':
    init()
    main()
