# -*- coding: utf-8 -*-
"""
Created on Mon May 11 20:01:34 2020

@author: prana
"""


import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

buttonPin = 25
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
  buttonState = GPIO.input(buttonPin)
  if buttonState == False:
    print 'button pushed'
  else:
    print 'not yet'