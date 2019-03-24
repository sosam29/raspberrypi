import RPi.GPIO as GPIO
import time
import math

ledPin = 11
buttonPin = 12

def setup():
    global pwm
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down= GPIO.PUD_UP)
    pwm = GPIO.PWM(ledPin, 1)
    pwm.start(0)
    

def loop():
    while True:
        if GPIO.input(buttonPin)==GPIO.LOW:
            alertMe()
            print("Alert On")
        else:
            stopAlert()
            print("Alert OFF")

def alertMe():
    pwm.start(50)
    for x in range(0.361):
        sinwave = math.sin(x * (math.pi/ 180.0))
        toneVal = 2000 + sinwave *500
        print("ToneVal %d" toneVal)
        pwm.ChangeFrequency(toneVal)
        time.sleep(0.001)
        
        
def stopAlert():
    pwm.stop()
    
    
def destroy():
   GPIO.output(ledPin, GPIO.LOW)
   GPIO.cleanup()
    
if __name__ =="__main__":
    setup()
    
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
        