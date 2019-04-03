import RPi.GPIO as GPIO
import time

class DHT(object):
    DHTLIB_OK= 0
    DHTLIB_ERROR_CHKSUM = -1
    DHTLIB_ERROR_TIMEOUT = -2
    DHTLIB__INVALID_VALUE = -999
    
    DHTLIB_DHT11_WAKEUP = 0.020  # 0.018  18 ms
    DHTLIB_TIMEOUT = 0.0001
    
    humidity = 0
    temp = 0
    
    def __init__(self, pin):
        self.pin = pin
        self.bits = [0,0,0,0,0]
        GPIO.setmode(GPIO.BOARD)
        
    def readSensor(self, pin, wakeupDelay):
        print("in readSensor()")
        mask = 0x80
        idx = 0
        self.bits =[0,0,0,0,0]
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)
        time.sleep(wakeupDelay)
        GPIO.output(pin, GPIO.HIGH)
        GPIO.setup(pin, GPIO.IN)
        
        loopcnt = self.DHTLIB_TIMEOUT
        t = time.time()
        
        while(GPIO.input(pin)==GPIO.LOW):
            if((time.time() - t) > loopcnt):
                return self.DHTLIB_ERROR_TIMEOUT
        t = time.time()
        
        while(GPIO.input(pin)==GPIO.HIGH):
            if((time.time() - t) > loopcnt):
                return self.DHTLIB_ERROR_TIMEOUT
        
        for i in range(0,40,1):
            t= time.time()  
        
            while(GPIO.input(pin)==GPIO.LOW):
                if((time.time() - t) > loopcnt):
                    return self.DHTLIB_ERROR_TIMEOUTHT
            
            t= time.time()          
            while(GPIO.input(pin)==GPIO.HIGH):
                if((time.time() - t) > loopcnt):
                    return self.DHTLIB_ERROR_TIMEOUTHT
            if ((time.time() - t) > 0.000):
                self.bits[idx] |= mask
            
            mask >>=1
            
            if(mask == 0):
                mask = 0x80
                idx+=1
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.HIGH)
        return self.DHTLIB_OK
        
    def readDHT11(self):
        print(self.pin)
        rv= self.readSensor(self.pin, self.DHTLIB_DHT11_WAKEUP)
        print("reading>>")
        if(rv is not self.DHTLIB_OK):
            self.humidity = self.DHTLIB__INVALID_VALUE
            self.temp = self.DHTLIB__INVALID_VALUE
            return rv
        self.humidity = self.bits[0]
        self.temp = self.bits[2] + self.bits[3]*0.1
        sumChk= ((self.bits[0] + self.bits[1] + self.bit[2] + self.bits[3]) & 0xFF)
        if(self.bits[4] is not sumChk):
            return self.DHTLIB_ERROR_CHKSUM
        
        return self.DHTLIB_OK
def loop():
    dht = DHT(11)
    sumCnt = 0
    okCnt = 0
    while True:
        sumCnt += 1
        chk = dht.readDHT11()
        if (chk is 0):
            okCnt +=1
        okRate = 100.0 * okCnt/sumCnt
        print("sumCnt: %d \t okRate: %.2f%%" %(sumCnt, okRate))
        print("chk: % d, \t Humidity: %.2f, \t Temp: %.2f "%(chk, dht.humidity, dht.temp))
        time.sleep(3)

if __name__=="__main__":
    try:
        loop()
    except KeyboardInterrupt :
        pass
        exit()
            
        
            
            
        
            
                
    