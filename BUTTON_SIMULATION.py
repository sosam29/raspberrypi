import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
# Pin 7 as output
GPIO.setup(7, GPIO.OUT)
# Pin 11 as output
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    # infinite loop
    while True:
        if GPIO.input(11)== GPIO.LOW:
            GPIO.output(7, GPIO.HIGH)
            #time.sleep(2)
            print("ON")
        else:
            GPIO.output(7, GPIO.LOW)
            #time.sleep(2)
            print("OFF")
        
except KeyboardInterrupt:
    # turn off if it is ON
    GPIO.output(7, GPIO.LOW )
    
GPIO.cleanup()