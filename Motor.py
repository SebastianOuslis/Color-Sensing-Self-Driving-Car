import RPi.GPIO as GPIO
import time
class Motor:
# lsT stands for left side top
# lsB stands for left side bottom
# rsT stands for right side top
# rsB stands for right side bottom
    GPIO_PINS_ARRAY = ()

    GPIO_LEFT_MOTOR_LEFT_SIDE_PINS_ARRAY = ()
    GPIO_LEFT_MOTOR_RIGHT_SIDE_PINS_ARRAY = ()
    GPIO_LEFT_MOTOR_TOP_PINS_ARRAY = ()
    GPIO_LEFT_MOTOR_BOTTOM_PINS_ARRAY = ()

    GPIO_RIGHT_MOTOR_LEFT_SIDE_PINS_ARRAY = ()
    GPIO_RIGHT_MOTOR_RIGHT_SIDE_PINS_ARRAY = ()
    GPIO_RIGHT_MOTOR_TOP_PINS_ARRAY = ()
    GPIO_RIGHT_MOTOR_BOTTOM_PINS_ARRAY = ()

    GPIO_TOP_PINS = ()
    GPIO_BOTTOM_PINS = ()

    TOP_OFF = 0
    TOP_ON = 1
    BOTTOM_ON = 0
    BOTTOM_OFF = 1

    timeToTurn = 0

    LeftMotor_lsT_A = 0
    LeftMotor_lsB_A = 0
    LeftMotor_rsT_A = 0
    LeftMotor_rsB_A = 0
    
    RightMotor_lsT_A = 0
    RightMotor_lsB_A = 0
    RightMotor_rsT_A = 0
    RightMotor_rsB_A = 0

    def __init__(self, LeftMotor_lsT, LeftMotor_lsB, LeftMotor_rsT, LeftMotor_rsB, RightMotor_lsT, RightMotor_lsB, RightMotor_rsT, RightMotor_rsB, timeToTurn):
        GPIO.setmode(GPIO.BOARD)
        
        self.GPIO_PINS_ARRAY = (LeftMotor_lsT, LeftMotor_lsB, LeftMotor_rsT, LeftMotor_rsB, RightMotor_lsT, RightMotor_lsB, RightMotor_rsT, RightMotor_rsB)

        self.GPIO_LEFT_MOTOR_LEFT_SIDE_PINS_ARRAY = (LeftMotor_lsT, LeftMotor_lsB)
        self.GPIO_LEFT_MOTOR_RIGHT_SIDE_PINS_ARRAY = (LeftMotor_rsT, LeftMotor_rsB)
        self.GPIO_LEFT_MOTOR_TOP_PINS_ARRAY = (LeftMotor_lsT, LeftMotor_rsT)
        self.GPIO_LEFT_MOTOR_BOTTOM_PINS_ARRAY = (LeftMotor_lsB, LeftMotor_rsB)
        
        self.GPIO_RIGHT_MOTOR_LEFT_SIDE_PINS_ARRAY = (RightMotor_lsT, RightMotor_lsB)
        self.GPIO_RIGHT_MOTOR_RIGHT_SIDE_PINS_ARRAY = (RightMotor_rsT, RightMotor_rsB)
        self.GPIO_RIGHT_MOTOR_TOP_PINS_ARRAY = (RightMotor_lsT, RightMotor_rsT)
        self.GPIO_RIGHT_MOTOR_BOTTOM_PINS_ARRAY = (RightMotor_lsB, RightMotor_rsB)

        self.GPIO_TOP_PINS = (RightMotor_lsT, RightMotor_rsT, LeftMotor_lsT, LeftMotor_rsT)
        self.GPIO_BOTTOM_PINS = (RightMotor_lsB, RightMotor_rsB, LeftMotor_lsB, LeftMotor_rsB)
                
        
        GPIO.setup(self.GPIO_PINS_ARRAY, GPIO.OUT)
        GPIO.output(self.GPIO_TOP_PINS, self.TOP_OFF)
        GPIO.output(self.GPIO_BOTTOM_PINS, self.BOTTOM_OFF)

        self.timeToTurn = timeToTurn

        print self.LeftMotor_lsT_A
        print LeftMotor_lsT
        self.LeftMotor_lsT_A = LeftMotor_lsT
        self.LeftMotor_lsB_A = LeftMotor_lsB
        self.LeftMotor_rsT_A = LeftMotor_rsT
        self.LeftMotor_rsB_A = LeftMotor_rsB
        
        self.RightMotor_lsT_A = RightMotor_lsT
        self.RightMotor_lsB_A = RightMotor_lsB
        self.RightMotor_rsT_A = RightMotor_rsT
        self.RightMotor_rsB_A = RightMotor_rsB

    def off(self):
        #turn everything off
        GPIO.output(self.GPIO_TOP_PINS, self.TOP_OFF)
        GPIO.output(self.GPIO_BOTTOM_PINS, self.BOTTOM_OFF)

    def LeftWheelForwards(self) :
        #move the left wheel forwards
        self.off()

        d = str(self.LeftMotor_lsT_A) + " is set to " + str(self.TOP_ON) + "   and  " + str(self.LeftMotor_rsB_A) + " is set to " + str(self.BOTTOM_ON)
    
        GPIO.output(self.LeftMotor_lsT_A, self.TOP_ON)
        GPIO.output(self.LeftMotor_rsB_A, self.BOTTOM_ON)

        return d

    def RightWheelForwards(self) :
        #move the right wheel forwards
        self.off()

        d = str(self.RightMotor_lsT_A) + " is set to " + str(self.TOP_ON) + "   and  " + str(self.RightMotor_rsB_A) + " is set to " + str(self.BOTTOM_ON)
    
        GPIO.output(self.RightMotor_lsT_A, self.TOP_ON)
        GPIO.output(self.RightMotor_rsB_A, self.BOTTOM_ON)

        return d
    
    def LeftWheelBack(self) :
        #move the left wheel back
        self.off()

        GPIO.output(self.LeftMotor_rsT_A, self.TOP_ON)
        GPIO.output(self.LeftMotor_lsB_A, self.BOTTOM_ON)

    def RightWheelBack(self) :
        #move the right wheel back
        self.off()

        GPIO.output(self.RightMotor_rsT_A, self.TOP_ON)
        GPIO.output(self.RightMotor_lsB_A, self.BOTTOM_ON)

            
    def forwards(self):
        #both wheels forwards
        self.off()

        d = str(self.LeftMotor_lsT_A) + " is set to " + str(self.TOP_ON) + "   and  " + str(self.LeftMotor_rsB_A) + " is set to " + str(self.BOTTOM_ON) + "   and   " + str(self.RightMotor_lsT_A) + " is set to " + str(self.TOP_ON) + "   and  " + str(self.RightMotor_rsB_A) + " is set to " + str(self.BOTTOM_ON)
        
        GPIO.output(self.LeftMotor_lsT_A, self.TOP_ON)
        GPIO.output(self.LeftMotor_rsB_A, self.BOTTOM_ON)
        GPIO.output(self.RightMotor_lsT_A, self.TOP_ON)
        GPIO.output(self.RightMotor_rsB_A, self.BOTTOM_ON)
        
        return d
    
    def back(self):
        #both wheels back
        self.off()

        self.LeftWheelBack()
        self.RightWheelBack()

    def turnLeft(self):
        self.off()

        self.LeftWheelForwards()
        time.sleep(self.timeToTurn)

        self.off()
        
    def turnRight(self):
        self.off()

        self.RightWheelForwards()
        time.sleep(self.timeToTurn)

        self.off()
