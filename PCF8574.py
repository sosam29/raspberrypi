import smbus
import time

class PCF8574_I2C(object):
    OUTPUT = 0
    INPUT= 1
    
    def __init__(self, address):
        self.bus = smbus.SMBus(1)
        self.address = address
        self.currentValue = 0
        self.writeByte(0)
        
    def readByte(self):
        return self.currentValue

    def writeByte(self, value):
        self.currentValue = value
        self.bus.write_byte(self.address, value)
    
    def digitalRead(self, pin):
        value= readByte()
        return (value&(1<<pin)==(1<<pin)) and 1 or 0
    
    def digitalWrite(self, pin, newvalue):
        value= self.currentValue
        if(newvalue == 1):
            value |=(1<<pin)
        elif(newvalue ==0):
            value &= ~(1 <<pin)
        self.writeByte(value)

def loop():
    mcp = PCF8574_I2C(0x27)
    while True:
        mcp.digitalWrite(3,1)
        print('is 0xff? %x'%(mcp.readByte()))
        time.sleep(1)
        mcp.writeByte(0x00)
        print('is 0x00? %x'%(mcp.readByte()))
        time.sleep(1)

class PCF8574_GPIO(object):
    OUT = 0
    IN = 1
    BCM = 0
    BOARD = 0
    
    def __init__(self, address):
        self.chip = PCF8574_I2C(address)
        self.address = address
    def setmode(self, mode):
        pass
    
    def setup(self, pin, mode):
        pass
    
    def input(self, pin):
        return self.chip.digitalRead(pin)
    
    def output(self, pin, value):
        self.chip.digitalWrite(pin, value)

def destroy():
    bus.close()
    
if __name__=="__main__":
    print("program is starting")
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
    
            