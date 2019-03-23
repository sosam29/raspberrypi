import RPi.GPIO as GPIO
import time


ledPins= [11,12,13,15,16,18,22,29,31,32]

def setup():
    print("here we go")
    GPIO.setmode(GPIO.BOARD)
    for pin in ledPins:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)
        
        

def loop():
    while True:
        for pin in ledPins:
            GPIO.output(pin, GPIO.LOW)
            time.sleep(0.1)
            GPIO.output(pin, GPIO.HIGH)
        for pin in ledPins[10:0:-1]:
            GPIO.output(pin, GPIO.LOW)
            time.sleep(0.1)
            GPIO.output(pin, GPIO.HIGH)

def destroy():
    for pin in ledPins:
        GPIO.output(pin, GPIO.LOW)
    GPIO.cleanup()
    
if __name__== "__main__":
    setup()
    
    try:
        loop()
    except KeyboardInterrupt:
        destroy()

            