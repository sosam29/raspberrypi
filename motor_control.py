import RPi.GPIO as GPIO
import time
import smbus

address = 0x48
bus = smbus.SMBus(1)
cmd =0x40

motorPin1= 13
motorPin2 = 11
enablePin=15

def analogRead(chan):
    value = bus.read_byte_data(address, cmd+chan)
    return value

def analogWrite(value):
    bus.write_byte_data(address, cmd , value)

def setup():
    global p
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(motorPin1, GPIO.OUT)
    GPIO.setup(motorPin2, GPIO.OUT)
    GPIO.setup(enablePin, GPIO.OUT)
    
    
    p= GPIO.PWM(enablePin, 1000)
    p.start(0)
    
def mapNUM(value, fromLow, fromHigh, toLow, toHigh):
    return (toHigh- toLow)*(value- fromLow) /(fromHigh - fromLow) + toLow

def motor(ADC):
    value = ADC- 128
    print("In motor driver circuit value is %d" %(value))
    
    if(value > 0):
        GPIO.output(motorPin1, GPIO.HIGH)
        GPIO.output(motorPin2, GPIO.LOW)
        print("turn fwd")
    if(value < 0):
        GPIO.output(motorPin1, GPIO.LOW)
        GPIO.output(motorPin2, GPIO.HIGH)
        print("turn REW")
    else:
        GPIO.output(motorPin1, GPIO.LOW)
        GPIO.output(motorPin2, GPIO.LOW)
        print("STOP")
    
    p.start(mapNUM(abs(value), 0, 128, 0, 100))
    print("PWM duty Cycle %d%%\n" %(abs(value)*100/127))
        
def loop():
    while True:
        value = analogRead(0)
        print("ADC value %d" %(value))
        motor(value)
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
        
