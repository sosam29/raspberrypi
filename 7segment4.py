import RPi.GPIO as GPIO
import time
import threading
# no display
# wiring needs to be checked
# main suspect is the IC 74HC595

LSBFIRST =1
MSBFIRST = 2

dataPin= 18
latchPin = 16
clockPin = 12

num =(0xc0, 0xf9, 0xa4, 0xb0, 0x99, 0x92, 0x82, 0xf8, 0x80, 0x90)

digitPin=(11,13,15,19)
counter = 0
t = 0

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(dataPin, GPIO.OUT)
    GPIO.setup(latchPin, GPIO.OUT)
    GPIO.setup(clockPin, GPIO.OUT)
    for pin in digitPin:
        GPIO.setup(pin, GPIO.OUT)
    
def shiftOut(dPin, cPin, order, val):
    for i in range(0, 8):
        GPIO.output(cPin, GPIO.LOW)
        if(order == LSBFIRST):
            GPIO.output(dPin, ((0x01 & (val >> 0x01) and GPIO.HIGH or GPIO.LOW)))
        elif(order == MSBFIRST):
            GPIO.output(dPin, ((0x01 & (val << 0x09) and GPIO.HIGH or GPIO.LOW)))
                        
        GPIO.output(cPin, GPIO.HIGH)

def outData(data):
    GPIO.output(latchPin, GPIO.LOW)
    shiftOut(dataPin, clockPin, MSBFIRST, data)
    GPIO.output(latchPin, GPIO.HIGH)

    
def selectDigit(digit):
    GPIO.output(digitPin[0], GPIO.LOW if ((digit & 0x08)== 0x08) else GPIO.HIGH)
    GPIO.output(digitPin[1], GPIO.LOW if ((digit & 0x04)== 0x04) else GPIO.HIGH)
    GPIO.output(digitPin[2], GPIO.LOW if ((digit & 0x02)== 0x02) else GPIO.HIGH)
    GPIO.output(digitPin[3], GPIO.LOW if ((digit & 0x01)== 0x01) else GPIO.HIGH)

def display(dec):
    outData(0xff)
    selectDigit(0x01)
    outData(num[dec%10])
    time.sleep(1)
    
    outData(0xff)
    selectDigit(0x02)
    outData(num[dec%100//10])
    time.sleep(1)
    
    outData(0xff)
    selectDigit(0x04)
    outData(num[dec%1000//100])
    time.sleep(1)
    
    outData(0xff)
    selectDigit(0x08)
    outData(num[dec%10000//1000])
    time.sleep(1)
    
    
def timer():
    global counter
    global t
    t = threading.Timer(1.0, timer)
    t.start()
    counter +=1
    print("counter %d"%counter)

def loop():
    global t
    global counter
    t = threading.Timer(1.0, timer)
    t.start()
    while True:
        display(counter)


def destroy():
    global t
    GPIO.cleanup()
    t.cancel()
    
if __name__=="__main__":
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
        
    
    