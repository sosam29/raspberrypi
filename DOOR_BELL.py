import RPi.GPIO as GPIO
#import time
# make sure you connect to Negative and then (-)-----o/o-----GOIP Pin 12
# make connect either LED or Buzzer to GPIO 11 (-)-|220 Ohm|--|LED | >-- GPIO pin 11
buttonPin = 12
buzzerPin = 11

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(buzzerPin, GPIO.OUT)
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    
    
def loop():
    while True:
        if GPIO.input(buttonPin)==GPIO.LOW:
            GPIO.output(buzzerPin, GPIO.HIGH)
            print("It is ON")
        else:
            GPIO.output(buzzerPin, GPIO.LOW)
            print("It is OFF")
        
def destroy():
    GPIO.output(buzzerPin, GPIO.LOW)
    GPIO.cleanup()          
 
if __name__ =="__main__":
    setup()
    
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
        