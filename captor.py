# coding=utf-8

import RPi.GPIO as GPIO
import time
import datetime
import requests
import json
import pytz

local_tz = pytz.timezone('Europe/Paris')

GPIO.setmode(GPIO.BCM)

Trig = 17
nbPrise = 100


GPIO.setup(Trig, GPIO.IN)

def utc_to_local(utc_dt):
    local_dt = utc_dt.replace(tzinfo=pytz.utc).astimezone(local_tz)
    return local_tz.normalize(local_dt)

def aslocaltimestr(utc_dt):
    return utc_to_local(utc_dt).strftime('%Y-%m-%d %H:%M:%S')

def take():
    total = 100
    nb = 0

    while nb < nbPrise:
        time.sleep(0.01)
        input = GPIO.input(Trig)
        total = total - input
        nb = nb + 1
    return total


while True:
    score = take()
    url = 'http://51.158.78.254:8080/measurements/'
    payload = {'value': score, 'room' : 100, 'captorName' : 'soundOfSilence', 'date' : aslocaltimestr(datetime.datetime.now()) }
    headers = {'content-type': 'application/json'}
    response = requests.post(url, data=json.dumps({'measurement' : payload}), headers=headers)
    print(json.dumps({'measurment' :payload}))
    print(response)
GPIO.cleanup()
