from adafruit_motorkit import MotorKit
kit = MotorKit()

import RPi.GPIO as IO
import time
import os, sys
import picam
import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((240, 240))
pygame.display.set_caption('Pi Car')


print("w/s: acceleration")
print("a/d: steering")
print("UP/DOWN: tilt")
print("LEFT/RIGHT: pan")
print("esc: exit")

#hostname="google.com"
#response=os.system("ping -c 1 " + hostname)

w=pygame.key.get_pressed()[pygame.K_w]
stop = False
count=0

while (True):
    count=count+1
    time.sleep(.02)
    if stop == True:
        break
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
                if event.key == K_w:
                        kit.motor1.throttle = 1.0
                        kit.motor2.throttle = 1.0
                elif event.key == K_s:
                        kit.motor1.throttle = -1.0
                        kit.motor2.throttle = -1.0
                elif event.key == K_a:
                        kit.motor1.throttle = 1.0
                        kit.motor2.throttle = .5
                elif event.key == K_d:
                        kit.motor1.throttle = .5
                        kit.motor2.throttle = 1.0
                elif event.key == K_ESCAPE:
                        stop = True
        
        elif event.type == pygame.KEYUP:
            if pygame.key.get_pressed()[pygame.K_w] != 0:
                kit.motor1.throttle = 0
                kit.motor2.throttle = 0
                
            elif(pygame.key.get_pressed()[pygame.K_s] != 0):
                kit.motor1.throttle = 0
                kit.motor2.throttle = 0
                    
            elif(pygame.key.get_pressed()[pygame.K_a] != 0):
                kit.motor1.throttle = 0
                kit.motor2.throttle = 0
                        
            elif(pygame.key.get_pressed()[pygame.K_d] != 0):
                kit.motor1.throttle = 0
                kit.motor2.throttle = 0
            else:
                kit.motor1.throttle = 0
                kit.motor2.throttle = 0
