import RPi.GPIO as GPIO
import time


pins= (12,16,18, 22)

CCWSteps= (0x01, 0x02, 0x04, 0x08)

CWSteps= (0x08, 0x04, 0x02, 0x01)

def setup():
    GPIO.setmode(GPIO.BOARD)
    for p in pins:
        GPIO.setup(p, GPIO.OUT)
    

def moveOnePeriod(direction, ms):
    for j in range(0,4,1):
        for i in range(0,4,1):
            if(direction==1):
                GPIO.output(pins[i],((CCWSteps[j]==1 <<i) and GPIO.HIGH or GPIO.LOW))
            else:
                 GPIO.output(pins[i],((CWSteps[j]==1 <<i) and GPIO.HIGH or GPIO.LOW))
        if(ms < 3):
            ms =3
        
        time.sleep(ms * 0.001)
        
        
def moveSteps(direction, ms, steps):
    for i in range(steps):
        moveOnePeriod(direction, ms)
    
def motorStop():
    for i in range(0,4,1):
        GPIO.output(pins[i], GPIO.LOW)


def loop():
    while True:
        moveSteps(1,3,512)
        time.sleep(0.5)
        moveSteps(0,3,315)
        time.sleep(0.5)

def destroy():
    GPIO.cleanup()
    

if __name__=="__main__":
    setup()
    
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
    
