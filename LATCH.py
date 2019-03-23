# this is latch event handling
# state can be changed based on the current state
import RPi.GPIO as GPIO
import time

ledPin = 7
buttonPin = 11
lampState = False

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down= GPIO.PUD_DOWN)


def latchState(mode):
    global lampState
    print('latchState GPIO %d' %mode)
    lampState = not lampState
    
    if lampState:
        print("Turn ON")
    else:
        print("Turn OFF")
        
    GPIO.output(ledPin, lampState)
    

def repeatloop():
    GPIO.add_event_detect(buttonPin, GPIO.FALLING, callback=latchState, bouncetime=300)
    while True:
        pass

def destroy():
    GPIO.output(ledPin, GPIO.LOW)
    GPIO.cleanup()
    
    
if __name__=='__main__':
    setup()
    
    try:
        repeatloop()
    except KeyboardInterrupt:
        destroy()


    