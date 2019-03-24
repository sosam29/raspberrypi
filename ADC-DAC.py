import smbus
import time

address = 0x48
bus= smbus.SMBus(1)

cmd = 0x40

def analogRead(channel):
    value = bus.read_byte_data(address, cmd+channel)
    return value

def analogWrite(value):
    bus.write_byte_data(address, cmd, value)

def loop():
    while True:
        value = analogRead(0)
        print("Analog value %d", value)
        analogWrite(value)
        voltage = value/255.0 * 3.3 # this is calculated based on vcc
        print("Digital Value:%.2f",voltage)
        
        #print("ADC value: %d, Val: %.2f" %(value. voltage))
        time.sleep(0.1)

def destroy():
    bus.close()

if __name__== "__main__" :
    print("Program Started")
    
    try:
        loop()
    except KeyboardInterrupt:
        destroy()