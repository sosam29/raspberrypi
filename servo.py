import RPi.GPIO as GPIO
import time


servoPin =11
OFFSET_DUTY = 0.5
SERVO_MIN_DUTY = 2.5 + OFFSET_DUTY
SERVO_MAX_DUTY = 12.5+ OFFSET_DUTY

def map(val, fromLow, fromHigh, toLow, toHigh):
    retval= (toHigh - toLow) *(val -fromLow) /(fromHigh -fromLow) + toLow
    print("map value %d" %(retval))
    return  retval #(toHigh - toLow) *(val -fromLow) /(fromHigh -fromLow) + toLow

def setup():
    global p
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(servoPin, GPIO.OUT)
    GPIO.output(servoPin, GPIO.LOW)
    p = GPIO.PWM(servoPin, 50)
    p.start(0)
    
def writeServo(val):
    if(val <0):
        val = 0
    elif(val > 180):
        val = 180
        
    duty= map(val, 0,180, SERVO_MIN_DUTY, SERVO_MAX_DUTY)
    print("Duty Cycle Mapping: %d "%(duty))
    p.ChangeDutyCycle(map(val,0, 180, SERVO_MIN_DUTY, SERVO_MAX_DUTY ))
    
def loop():
    while True:
        for dc in range(0, 181, 1):
            print("be FWD Direction")
            print(dc)
            writeServo(dc)
            time.sleep(.05)
        time.sleep(0.5)
        
        for dc in range(180, -1, -1):
            print("reverse Direction")
            print(dc)
            writeServo(dc)
            time.sleep(.05)
        time.sleep(0.5)
    
def destroy():
    GPIO.output(servoPin, GPIO.LOW)
    GPIO.cleanup()
    

if __name__=="__main__":
    setup()
    
    try:
        loop()
    except KeyboardInterrupt:
        destroy()


        