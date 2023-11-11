#!/usr/bin/python
#Libraries
import sys
import time
import math
import re
from adafruit_servokit import ServoKit    
#Constants
nbPCAServo=4
#Parameters
MIN_IMP  =[500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500]
MAX_IMP  =[2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500]
MIN_ANG  =[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
MAX_ANG  =[180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180]
REF_ANG  =[90,90,70,10] 
LST_ANG  =[ 0, 0, 0, 0]
SPEED = [ 0.025, 0.035, 0.05, 0.1, 0.2, 0.3 ]
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
    pca.servo[motor].angle = None #disable channel
        
# Deplacement
def pcaMove(motor,angle1,angle2,speed=1):
    step = SPEED[speed] 
    angle1 = angle1 + REF_ANG[motor]
    angle2 = angle2 + REF_ANG[motor]
    steps = abs(angle2 - angle1)*SPEED[speed]
    if (angle1<angle2):
        angle = angle1
        while (angle<angle2):
            pca.servo[motor].angle = angle
            angle = angle + step 
    if (angle1>angle2):
        angle = angle1
        while (angle>angle2):
            pca.servo[motor].angle = angle
            angle = angle - step

    
# function init
def init():
    for i in range(nbPCAServo):
        pca.servo[i].set_pulse_width_range(MIN_IMP[i] , MAX_IMP[i])

def scenario(name,start,stop):
    file = open(name, "r")
    n = 0
    for line in file.read().splitlines():
        n += 1        
        if n<start:
            continue
        if n>stop:
            break
        Args = re.split(r'\s+', line)
        count = len(Args)
        if (line.find("#")==0):
            print(f"     {line}")
        elif (Args[0] == '.'):
            print(f"{n:4} ...")
            time.sleep(1)
        elif (count>3):
            [ motor, angle1, angle2, speed ] = Args
            s = ">>>"[0:int(speed)+1]
            print(f"{n:4} + [{motor}] {angle1: >4}  {s: <3}  {angle2: >4}")
            motor = int(motor)
            angle1 = int(angle1)
            angle2 = int(angle2)
            # Rattrapage si il y a un ecart avec la derniere position
            #if (angle1!=LST_ANG[motor]):
                #pcaMove(motor,LST_ANG[motor],angle1,int(speed))
            pcaMove(motor,angle1,angle2,int(speed))
            LST_ANG[motor] = angle2
        elif (count>1):
            [ motor, angle ] = Args
            print(f"{n:4} + [{motor}] {angle: >4}")
            motor = int(motor)
            angle = int(angle)
            pcaMove(motor,LST_ANG[motor],angle)
            LST_ANG[motor] = angle
        elif (count>0):
            [ motor ] = Args
            print(f"{n:4} - [{motor}]")
            pcaStop(int(motor))
        else:
            print(f"{n:4} ? {line}")
    file.close()

# function main
def main():
    argn = len(sys.argv)
    if (argn>3):
        stop = int(sys.argv[3])
    else:
        stop = 9999
    if (argn>2):
        start = int(sys.argv[2])
    else:
        start = 1
    if (argn>1):
        filename = sys.argv[1]
    else:
        filename = sys.argv[0].replace("py","txt")

    scenario(filename,start,stop)

if __name__ == '__main__':
    init()
    main()
