import RPi.GPIO as GPIO
import smbus
import math
import time


address= 0x48
bus= smbus.SMBus(1)
cmd = 0x40

def analogRead(chan):
    value = bus.read_byte_data(address, cmd+chan)
    return value

def analogWrite(val):
    bus.write_byte_data(address, cmd, val)


def setup():
    GPIO.setmode(GPIO.BOARD)

def loop():
    while True:
        value = analogRead(0)
        voltage = value / 255.0 * 3.3
        res = 10 + voltage/ (3.3 -voltage)
        tempK = 1/(1/(273.25 + 25) + math.log(res/10)/3950.0)
        tempC = tempK - 273.15
        print('ADC Value: %d, voltage: %.2f, Temprature: %.2f' %(value, voltage, tempC))
        time.sleep(1.0)

def destroy():
    GPIO.cleanup()
    
if __name__=="__main__":
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()

