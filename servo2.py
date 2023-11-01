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

# function init
def init():
    for i in range(nbPCAServo):
        pca.servo[i].set_pulse_width_range(MIN_IMP[i] , MAX_IMP[i])

# function main
def main():
    pcaMove(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]));

# function pcaScenario
def pcaMove(motor,angle1,angle2):
    if (angle >= MIN_ANG[motor] and angle <= MAX_ANG[motor]):
        angle=angle1;
        while angle < angle2:
            pca.servo[motor].angle = angle
            angle++
    else:
        pca.servo[motor].angle=None #disable channel

if __name__ == '__main__':
    init()
    main()
