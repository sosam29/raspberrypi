import RPi.GPIO as GPIO
import time
import DHT_read as DHT

dhtPin =11
def loop():
    dht= DHT.DHT(dhtPin)
    sumCnt = 0
    while (True):
        sumCnt +=1
        chk  =dht.readDHT11()
        print("The sumcnt is : %d \t chk: %d" %(sumCnt, chk))
        
        if (chk is dht.DHTLIB_OK):
            print("DHT11  OK!!")
        elif (chk is dht.DHTLIB_ERROR_CHKSUM):
            print("DHTLIB_ERROR_CHKSUM")
        elif (chk is dht.DHTLIB_ERROR_TIMEOUT):
            print("Check sum Error")
        else:
            print("Other error")
        
        print("Humidity: %.2f, \t Temprature: %.2f \n" %(dht.humidity, dht.temp))
        time.sleep(2)

if __name__ =="__main__":
    try:
        loop()
    except KeyboardInterrupt:
        GPIO.cleanup()
        exit()