import RPi.GPIO as GPIO
import time
import random

pins= {'pin_R': 11, 'pin_G': 12,'pin_B': 15}
def setup():
    global r, g, b
    GPIO.setmode(GPIO.BOARD)
    for p in pins:
        GPIO.setup(pins[p], GPIO.OUT)
        GPIO.output(pins[p], GPIO.HIGH)
    r = GPIO.PWM(pins['pin_R'], 2000)
    g = GPIO.PWM(pins['pin_G'], 2000)
    b = GPIO.PWM(pins['pin_B'], 2000)
    
    r.start(0)
    g.start(0)
    b.start(0)
    
def setColor(r_val, g_val, b_val):
    r.ChangeDutyCycle(r_val)
    g.ChangeDutyCycle(g_val)
    b.ChangeDutyCycle(b_val)
    
def loop():
    while True:
        r_sel = random.randint(0, 100)
        g_sel = random.randint(0, 100)
        b_sel = random.randint(0, 100)
        setColor(r_sel, g_sel, b_sel)
        time.sleep(0.5)
def destroy():
    r.stop()
    g.stop()
    b.stop()
    
if __name__ =="__main__":
    setup()
    
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
        