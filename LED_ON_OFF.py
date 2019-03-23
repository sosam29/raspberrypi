import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
for x in range(0,3):
    GPIO.output(7, True)
    print("ON")
    time.sleep(1)
    GPIO.output(7, False)
    GPIO.output(11, True)
    print("OFF")
    time.sleep(1)
    GPIO.output(11, False)
    GPIO.output(13, True)
    time.sleep(1)
    GPIO.output(13, False)
GPIO.cleanup()
    