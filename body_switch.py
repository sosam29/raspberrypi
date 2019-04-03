import RPi.GPIO as GPIO
import time

ledPin = 11
sensorPin = 7

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.setup(sensorPin, GPIO.IN)
    
    
def loop():
    while True:        
        if GPIO.input(sensorPin)==GPIO.HIGH:
            print("sensed Body")
            GPIO.output(ledPin, GPIO.HIGH)
            print("Turning LED ON")
        else:
            GPIO.output(ledPin, GPIO.LOW)
            print("Turning LED OFF")
        time.sleep(1)

def destroy():
    GPIO.output(ledPin, GPIO.LOW)
    print("In destroy() Turning LED OFF")
    GPIO.cleanup()
    
if __name__ =="__main__":
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
        