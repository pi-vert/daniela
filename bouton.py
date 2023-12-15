# Imports
import time
import RPi.GPIO as GPIO
import sys

# Definition des pins
pinBtn = 21

GPIO.setmode(GPIO.BCM)

# Definition des pins en entree / sortie
GPIO.setup(pinBtn, GPIO.IN, pull_up_down = GPIO.PUD_UP)

# Boucle infinie
while True:
    etat = GPIO.input(pinBtn)

    # etat==0 => bouton appuye => LED allumee
    if (etat == 0) :
        print("Appui detecte")
        sys.exit(0)

    # Temps de repos pour eviter la surchauffe du processeur
    time.sleep(0.3)
