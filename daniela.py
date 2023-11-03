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
def pcaMove(motor,angle1,angle2,step,sleep):
    angle = angle1
    while angle < angle2:
        print ( motor+' '+angle )
        pca.servo[motor].angle = angle
        angle = angle + step
        time.sleep(sleep)

# Deplacement
def pcaRun(motor,angle1,angle2,speed):
    angle = angle1
    while angle < angle2:
        pca.servo[motor].angle = angle
        angle = angle + 0.1
        time.sleep(speed)
    while angle > angle1:
        pca.servo[motor].angle = angle
        angle = angle - 0.1
        time.sleep(speed)

# function init
def init():
    for i in range(nbPCAServo):
        pca.servo[i].set_pulse_width_range(MIN_IMP[i] , MAX_IMP[i])
    pcaSet(3,30);
    pcaSet(2,70);
    pcaSet(1,45);
    pcaSet(0,90);
    
# function main
def main():
    # Mouvement hésitation
    pcaMove(3,30,80,0.1,0.005);
    pcaMove(3,30,65,0.1,0.005);
    pcaMove(3,30,50,0.1,0.005);

# Stop: repos
    pcaSet(3,30);
    pcaSet(2,70);
    pcaSet(1,45);
    pcaSet(0,90);
    pcaSet(3,-1);
    pcaSet(2,-1);
    pcaSet(1,-1);
    pcaSet(0,-1);
    
if __name__ == '__main__':
    init()
    main()
