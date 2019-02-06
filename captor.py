# coding=utf-8

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

Trig = 17
nbPrise = 1000

GPIO.setup(Trig, GPIO.IN)

nb = 0


def take():
    total = 0
    while nb < nbPrise:
        total = total + GPIO.input(Trig)
    return total


while True:
    score = take()
    print(score)


GPIO.cleanup()