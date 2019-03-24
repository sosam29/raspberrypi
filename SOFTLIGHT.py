import smbus
import RPi.GPIO as GPIO
import time
#make sure you are connecting potentiometer with (-)(1)--variable to (2) and last point to (+)
# wiring is crucial as sometimes pin numbers may be confusing

# I was not able to detect i2C due to wiring error.
# need to retake look and after correcting pot wiring I was
# able to detect $> i2cdetect -y 1 at 0X48


address = 0x48
bus= smbus.SMBus(1)
ledPin = 11
cmd = 0x40

def setup():
    global p
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.output(ledPin, GPIO.LOW)
    p = GPIO.PWM(ledPin, 1000)
    p.start(0)
    


def analogRead(channel):
    value = bus.read_byte_data(address, cmd+channel)
    return value

def analogWrite(value):
    bus.write_byte_data(address, cmd, value)

def loop():
    while True:
        value = analogRead(0)
        print(value)
        analogWrite(value)
#        voltage = value/255.0 * 3.3 # this is calculated based on vcc
#       print("Digital Value:%.2f",voltage)
            
        #print("ADC value: %d, Val: %.2f" %(value. voltage))
        p.ChangeDutyCycle(value*100/255)
        time.sleep(0.1)

def destroy():
    bus.close()
    GPIO.cleanup()

if __name__== "__main__" :
    print("Program Started")
    setup() # do not miss this if you are using previous code
    try:
        loop()
    except KeyboardInterrupt:
        destroy()