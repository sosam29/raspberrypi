import RPi.GPIO as GPIO
import time


LSBFIRST = 1
MSBFIRST = 2
datapin = 11
latchpin = 13
clockpin = 15

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(datapin, GPIO.OUT)
    GPIO.setup(latchpin, GPIO.OUT)
    GPIO.setup(clockpin, GPIO.OUT)

def shiftout(dpin, cpin, order, val):
    for i in range(0,8):
        GPIO.output(cpin, GPIO.LOW)
        
        if (order == LSBFIRST):
            GPIO.output(dpin, (0x01 &(val >>i)==0x01) and GPIO.HIGH or GPIO.LOW)
        elif( order ==MSBFIRST):
            GPIO.output(dpin, (0x01 &(val <<i)==0x01) and GPIO.HIGH or GPIO.LOW)
        
        GPIO.output(cpin,GPIO.HIGH)

def loop():
    while True:
        x = 0x01
        for i in range(0,8):
            print("LSB FIRST")
            GPIO.output(latchpin, GPIO.LOW)
            shiftout(datapin, clockpin, LSBFIRST,x)
            GPIO.output(latchpin, GPIO.HIGH)
            x <<= 1
            print(x)
            time.sleep(.01)
        time.sleep(.01)
        x = 0x80               
        for i in range(0,8):
            print("MSB FIRST")
            GPIO.output(latchpin, GPIO.LOW)
            shiftout(datapin, clockpin, LSBFIRST,x)
            GPIO.output(latchpin, GPIO.HIGH)
            x >>= 1
            print(x)
            time.sleep(0.01)
        time.sleep(.01)
def destroy():
    GPIO.cleanup()
    
if __name__ == "__main__":
    setup()
    
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
    
    
        
    
    