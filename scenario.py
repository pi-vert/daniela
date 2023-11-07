#Libraries
import sys
import time    #https://docs.python.org/fr/3/library/time.html
##from adafruit_servokit import ServoKit    #https://circuitpython.readthedocs.io/projects/servokit/en/latest/
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
##pca = ServoKit(channels=16)

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

def scenario(name,startm,stop):
    file = open(name, "r")
    n = 1
    for line in file:
        Args = line.rstrip().split("\t")
        count = len(Args)
        print "--" +line.find("#")
        if (line.find("#")):
            print str(n) + " >" + line
        elif (Args[0] == '.'):
            print ( "Pause" )
            time.sleep(1)
        elif (count>3):
            [ motor, speed, angle1, angle2 ] = Args
            print ( str(motor)+' '+str(speed)+' '+str(angle1)+' -> '+str(angle2) )        
        n = n + 1        
    file.close()

# function main
def main():
    argn = len(sys.argv)
    if (argn>3):
        stop = int(sys.argv[3])
    else:
        stop = 10000
    if (argn>2):
        start = int(sys.argv[2])
    else:
        start = 10000
    if (argn>1):
        filename = sys.argv[1]
    else:
        filename = sys.argv[0].replace("py","txt")

    scenario(filename,start,stop)

if __name__ == '__main__':
##    init()
    main()
