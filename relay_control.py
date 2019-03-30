import RPi.GPIO as GPIO
import time


relayPin = 11
buttonPin = 12
bounceTime = 50

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(relayPin ,GPIO.OUT)
    GPIO.setup(buttonPin, GPIO.IN)
    
def loop():
    relayState = False
    lastChangeTime= round(time.time()*1000)
    buttonState=GPIO.HIGH
    lastButtonState = GPIO.HIGH
    reading= GPIO.HIGH
    while True:
        reading= GPIO.input(buttonPin)
        if reading != lastButtonState:
            lastChangeTime = round(time.time()*1000)
        if((round(time.time()*1000) - lastChangeTime) > bounceTime):
            if reading != buttonState:
                buttonState = reading
                if buttonState ==GPIO.LOW:
                    print("Button is pressed")
                    relayState = not relayState
                    if relayState:
                        print("turn on relay")
                    else:
                        print("Turn off relay")
                else:
                    print("Button is realeased")
        GPIO.output(relayPin, relayState)
        lastButtonState = reading


def destroy():
    GPIO.output(relayPin, GPIO.LOW)
    GPIO.cleanup()
    
if __name__=="__main__":
    setup()
    try:
        loop()
    except  KeyboardInterrupt:
        destroy()
        

                    
                        
                    
                    
            
    