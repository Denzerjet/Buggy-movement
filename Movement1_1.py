from adafruit_motorkit import MotorKit
kit = MotorKit()

import RPi.GPIO as IO
import time
import os, sys
from picamera import PiCamera
import cv2
import pygame
from picamera.array import PiRGBArray
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((240, 240))
pygame.display.set_caption('Pi Car')

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))

time.sleep(0.1)


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
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# grab the raw NumPy array representing the image, then initialize the timestamp
	# and occupied/unoccupied text
	image = frame.array
 
	# show the frame
	cv2.imshow("Frame", image)
	key = cv2.waitKey(1) & 0xFF
 
	# clear the stream in preparation for the next frame
	rawCapture.truncate(0)
 
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break
    
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
                #elif event.type == pygame.KEYUP:
                       # if((pygame.key.get_pressed()[pygame.K_w] != 0 and pygame.key.get_pressed()[pygame.K_a] != 0) or (pygame.key.get_pressed()[pygame.K_w] !=0 and pygame.key.get_pressed()[pygame.K_d] != 0)):
                       #         
                       # elif((pygame.key.get_pressed()[pygame.K_s] != 0 and pygame.key.get_pressed()[pygame.K_a] != 0) or (pygame.key.get_pressed()[pygame.K_s] !=0 and pygame.key.get_pressed()[pygame.K_d] != 0)):
                                
                       # elif(pygame.key.get_pressed()[pygame.K_w] != 0):
                        #        throttle=15.1
                        #        steer=14.5
                        #elif(pygame.key.get_pressed()[pygame.K_s] != 0):
                        #        throttle=13.2
                        #        steer=14.5
                        #elif(pygame.key.get_pressed()[pygame.K_a] != 0):
                        #        throttle=14
                        #        steer=11
                        #elif(pygame.key.get_pressed()[pygame.K_d] != 0):
                         #       throttle=14
                         #       steer=18
                        #else:
                          #      throttle=14
                          #      steer=14.5*/
