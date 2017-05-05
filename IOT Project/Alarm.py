#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  RGB_LED.py
#
# A short program to control an RGB LED by utilizing
# the PWM functions within the Python GPIO module
#
#  Copyright 2015  Ken Powers
#   
 
# Import the modules used in the script
import random, time
import RPi.GPIO as GPIO
import pygame

# Set GPIO to Broadcom system and set RGB Pin numbers
RUNNING = True
GPIO.setmode(GPIO.BCM)
red = 6
green = 5
blue = 13

# Set pins to output mode
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)
 
Freq = 100 #Hz
 
# Setup all the LED colors with an initial
# duty cycle of 0 which is off
RED = GPIO.PWM(red, Freq)
RED.start(0)
GREEN = GPIO.PWM(green, Freq)
GREEN.start(0)
BLUE = GPIO.PWM(blue, Freq)
BLUE.start(0)

RED.ChangeDutyCycle(100)
GREEN.ChangeDutyCycle(0)
BLUE.ChangeDutyCycle(0)
time.sleep(0.5)


RED.ChangeDutyCycle(0)
GREEN.ChangeDutyCycle(0)
BLUE.ChangeDutyCycle(0)

pygame.mixer.init()
pygame.mixer.music.load("/home/pi/Downloads/Red Alert.wav")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    continue
