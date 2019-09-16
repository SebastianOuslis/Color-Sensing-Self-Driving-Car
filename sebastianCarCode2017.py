import numpy as np
import sys
#print 'sys.path = '
#print(sys.path)
sys.path.append('/usr/local/lib/python2.7/site-packages')
import cv2
sys.path.append('/usr/lib/python2.7/dist-packages')
import RPi.GPIO as GPIO
import argparse
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import os
from Motor import Motor

#set the boardmode of the raspberry pi
GPIO.setmode(GPIO.BOARD)
#variables for direction
GREEN = "left"
RED = "right"
WHITE = "go"
BLUE = ""
BLACK = ""
GREY = "go"

#set the pin numbers
SHUT_OFF_INPUT = 12
GPIO.setup(SHUT_OFF_INPUT,GPIO.IN)
LeftMotor_lsT_A = 40
LeftMotor_lsB_A = 38
LeftMotor_rsT_A = 37
# output 1 I use
LeftMotor_rsB_A = 36


RightMotor_lsT_A = 35
RightMotor_lsB_A = 33
RightMotor_rsT_A = 32
# output 2 I use
RightMotor_rsB_A = 31

#time it takes to turn
TURNING_TIME = 5
#create the motor object
motors = Motor(LeftMotor_lsT_A, LeftMotor_lsB_A, LeftMotor_rsT_A, LeftMotor_rsB_A, RightMotor_lsT_A, RightMotor_lsB_A, RightMotor_rsT_A,  RightMotor_rsB_A, TURNING_TIME)

#turn the motors off
motors.off()
#chose = True
#time it takes to go forwards
FORWARDS_TIME = 6

#values for colors
BLUE_FINDING_VALUE = -0.2
GREEN_FINDING_VALUE = -0.2
RED_FINDING_VALUE = -0.5
ABSOLUTE_DIFFRENCE_VALUE = 0.15

camera = PiCamera()

shutOff = False

# allow the camera to warmup
time.sleep(0.3)

breakVariable = 0

while True:
    try:
        motors.off()
        rawCapture = PiRGBArray(camera)
        # grab an image from the camera
        camera.capture(rawCapture, format="bgr")
        origImage = rawCapture.array
        print( 'Image size = ', origImage.shape[1], ' x ', origImage.shape[0] )
        #take the middle of the screen which is a quarter by a quarter of the origional image
        print "dimensions are " , origImage.shape[0]*3/8 ,"  to ", origImage.shape[0]*5/8, "  and  ", origImage.shape[1]*3/8 , " to ", origImage.shape[1]*5/8

        if GPIO.input(SHUT_OFF_INPUT) == 1:
            print ("yarp")
            shutOff = True
            break


        
        origImage = origImage[origImage.shape[0]*3/8 : origImage.shape[0]*5/8 , origImage.shape[1]*3/8 : origImage.shape[1]*5/8]
        
        print "check 1"
        colors = ("blue", "green", "red")
        NUM_COLOURS = 3
        channels = cv2.split(origImage)
        # create 3 dimensional array of [colors=3,bins,pixel count=1]
        BINS = 3
        hist = np.zeros((NUM_COLOURS,BINS,1))
        colorSum = np.zeros((NUM_COLOURS,BINS,1))
        print "check 2"
        
        for (chan, dimension) in zip(channels, range(NUM_COLOURS)):
            # create a histogram for the current channel
            hist[dimension] = cv2.calcHist([chan], [0], None, [BINS], [0, 256])
            print(colors[dimension])
            #
            # normalize pixel counts
            #
            cv2.normalize(hist[dimension], hist[dimension], 3, 0, cv2.NORM_L1)
            print(hist[dimension])
            colorSum[dimension] = [hist[dimension,0],hist[dimension,1],hist[dimension,2]]

        if GPIO.input(SHUT_OFF_INPUT) == 1:
            print ("yarp")
            shutOff = True
            break
        
        print "check 3"

        time.sleep(3)
        #take the colors values from the histogram
        lowBlue = colorSum[0,0]
        lowGreen = colorSum[1,0]
        lowRed = colorSum[2,0]
        midBlue = colorSum[0,1]
        midGreen = colorSum[1,1]
        midRed = colorSum[2,1]
        highBlue = colorSum[0,2]
        highGreen = colorSum[1,2]
        highRed = colorSum[2,2]
        print "check 4"

        lowSum = lowBlue + lowGreen + lowRed
        midSum = midBlue + midGreen + midRed
        highSum = highBlue + highGreen + highRed
        print "check 5"
        print lowSum
        print midSum
        print highSum
        #check the different values to find the colors
        setting = "test"
        if (highGreen - 2) > (highBlue + highRed):
            print "Its Real Green"
            setting = GREEN
        elif (highBlue - 2) > (highGreen + highRed):
            print "Its Real Blue"
            setting = BLUE
        elif (highRed - 2) > (highBlue + highGreen):
            print "Its Real Red"
            setting = RED
        else:
            print "check 6"
            if lowSum >= 7.3 and (midGreen + highGreen *1.5) > 1.4  :
                print "Black"
                setting = BLACK
	    elif lowSum >= 7 and (midGreen + highGreen *1.5) < 1.4 :
		print 'Black'
		setting = BLACK
            elif midSum >= 4.5:
                print "Grey"
                setting = GREY
            elif highSum >= 4:
                print "White"
                setting = WHITE
            else: 
                print "check 7"
                if ((midGreen + highGreen*1.5) > (midRed + highRed*1.5 + midBlue + highBlue*1.5)*1.1):
                    print "Its Green"
                    setting = GREEN
                elif ((midRed + highRed*1.5) > (midGreen + highGreen*1.5 + midBlue + highBlue*1.5)*1.15):
                    print "Its Red"
                    setting = RED
                elif ((midBlue + highBlue*1.5) > (midRed + highRed*1.5 + midGreen + highGreen*1.5)):
                    print "Its Blue"
                    setting = BLUE
                else:
                    print "nothing Special"

        print "check 8"
        print setting
        if setting == "left":
            #motors.turnLeft()
            getWords = motors.LeftWheelForwards()
            print getWords
            print "left"
        elif setting == "right":
            #motors.turnRight()
            getWords = motors.RightWheelForwards()
            print getWords
            print "right"
        elif setting == "go":
            getWords = motors.forwards()
            print getWords
            print "go"
        # show the output image
        #cv2.imshow("Colour Histogram", origImage)
        #keyValue = cv2.waitKey(0)
        # The q key quits
        #if keyValue == ord('q'):
        #    break;
        if GPIO.input(SHUT_OFF_INPUT) == 1:
            print ("Shut Off Input")
            shutOff = True
            break
        #if the values are not test or blank
        if (setting != "") :
            if (setting != 'test') :   
                time.sleep(FORWARDS_TIME)
                motors.off()
                print "stop"
                
        #time.sleep(0.1)
        if GPIO.input(SHUT_OFF_INPUT) == 1:
            print ("Shut Off Input")
            shutOff = True
            break
        
    except KeyboardInterrupt:
            #if something messes up
            break
        
    #except:
    #    print "somthing went wrong"
    #    break
        
    #finally:

#GPIO.cleanup()
#clean up everything
motors.off()
print "final"
if shutOff :
    #turn off the raspberry pi
    os.system("sudo shutdown -h now")
