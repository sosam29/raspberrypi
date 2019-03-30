import RPi.GPIO as GPIO
import smbus
import math
import time


address= 0x48
bus= smbus.SMBus(1)
cmd = 0x10
swPin = 40

def analogRead(chan):
    value = bus.write_byte(address, cmd+chan)
    value = bus.read_byte(address)
    value = bus.read_byte(address)
    return value

def analogWrite(val):
    bus.write_byte(address, cmd, val)


def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(swPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def loop():
    while True:
        val_z= GPIO.input(swPin)
        val_y = analogRead(0)
        val_x = analogRead(1)    
        print('X Value: %d, Y Value: %d, Z value: %d' %(val_x,val_y, val_z))
        time.sleep(0.1)

def destroy():
    bus.close()
    GPIO.cleanup()
    
if __name__=="__main__":
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()

