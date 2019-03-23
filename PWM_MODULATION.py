import RPi.GPIO as GPIO
import time

ledPin = 12

def setup():
    global pwm
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.output(ledPin, GPIO.LOW)
    
    pwm = GPIO.PWM(ledPin, 100)
    pwm.start(0)  # param set %duty cycle with set value

def loop():
    while True:
        for cyc in range(0, 101, 1):
            pwm.ChangeDutyCycle(cyc)
            time.sleep(0.01)
        time.sleep(1)
        
        for cyc in range(100, -1, -1):
            pwm.ChangeDutyCycle(cyc)
            time.sleep(0.01)
        time.sleep(1)

def destroy():
    pwm.stop()
    GPIO.output(ledPin, GPIO.LOW)
    GPIO.cleanup()


    
if __name__== "__main__":
    setup()
    
    try:
        loop()
    except KeyboardInterrupt:
        destroy()


            