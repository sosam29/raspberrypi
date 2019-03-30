import RPi.GPIO as GPIO
import time

# this is to set up pin and configuration
LSBFIRST = 1
MSBFIRST = 2
datapin = 11
latchpin = 13
clockpin = 15

num = [0xc0, 0xf9, 0xb0, 0x99, 0x92, 0x82, 0xf8, 0x80, 0x90, 0x88, 0x83, 0xc6, 0xa1, 0x86, 0x8e]
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
            GPIO.output(dpin, (0x01 &(val <<i)==0x80) and GPIO.HIGH or GPIO.LOW)
        
        GPIO.output(cpin,GPIO.HIGH)

def loop():
    while True:
        x = 0x01
        for i in range(0,len(num)):
            print(num[i])
            GPIO.output(latchpin, GPIO.LOW)
            shiftout(datapin, clockpin, MSBFIRST,num[i])
            GPIO.output(latchpin, GPIO.HIGH)          
            time.sleep(0.5)
        #time.sleep(.01)
        #x = 0x80               
        for i in range(0,len(num)):
            print(num[i]&0x7f)
            GPIO.output(latchpin, GPIO.LOW)
            shiftout(datapin, clockpin, MSBFIRST,num[i]&0x7f)
            GPIO.output(latchpin, GPIO.HIGH)
            time.sleep(0.5)
        
def destroy():
    GPIO.cleanup()
    
if __name__ == "__main__":
    setup()
    
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
    
    
        
    
    