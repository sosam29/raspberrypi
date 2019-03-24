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

ledRedPin= 7
ledGreenPin =11
ledBluePin=13

cmd = 0x40

def setup():
    global p_r, p_g, p_b
    
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledRedPin, GPIO.OUT)
    GPIO.setup(ledGreenPin, GPIO.OUT)
    GPIO.setup(ledBluePin, GPIO.OUT)
    
    GPIO.output(ledRedPin, GPIO.LOW)
    GPIO.output(ledGreenPin, GPIO.LOW)
    GPIO.output(ledBluePin, GPIO.LOW)
    
    p_r = GPIO.PWM(ledRedPin, 1000)
    p_g = GPIO.PWM(ledGreenPin, 1000)
    p_b = GPIO.PWM(ledBluePin, 1000)
    
    p_r.start(0)
    p_g.start(0)
    p_b.start(0)
    


def analogRead(channel):
    bus.write_byte(address, cmd+channel)
    value = bus.read_byte(address)
    value = bus.read_byte(address)
    return value

def analogWrite(value):
    bus.write_byte_data(address, cmd, value)

def loop():
    while True:
        value_r = analogRead(0)
        value_g = analogRead(1)
        value_b = analogRead(2)
        #print(value)
        analogWrite(value_r)
#        voltage = value/255.0 * 3.3 # this is calculated based on vcc
#       print("Digital Value:%.2f",voltage)
            
        print("ADC RED: %d, GREEN: %d, BLUE: %d" %(value_r,value_g, value_b))
        
        p_r.ChangeDutyCycle(value_r*100/255)
        p_g.ChangeDutyCycle(value_g*100/255)
        p_b.ChangeDutyCycle(value_b*100/255)
        
        time.sleep(0.1)

def destroy():
    bus.close()
    
    GPIO.output(ledRedPin, GPIO.LOW)
    GPIO.output(ledGreenPin, GPIO.LOW)
    GPIO.output(ledBluePin, GPIO.LOW)
    
    GPIO.cleanup()

if __name__== "__main__" :
    print("Program Started")
    setup() # do not miss this if you are using previous code
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
