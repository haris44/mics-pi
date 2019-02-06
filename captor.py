# coding=utf-8

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

Trig = 17
nbPrise = 100


GPIO.setup(Trig, GPIO.IN)


def take():
    total = 0
    nb = 0

    while nb < nbPrise:
        time.sleep(0.1)
        total = total + GPIO.input(Trig)
        nb = nb + 1
    return total


while True:
    score = take()
    print(score)


GPIO.cleanup()