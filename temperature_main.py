from bmp180 import BMP180
from machine import I2C, Pin
import machine
from utime import sleep
import utime as time
from dht import DHT11, InvalidChecksum

#BMP180
i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=400000) 
bmp180 = BMP180(i2c)
#PICO SENSOR
sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)
#DHT11
pin = Pin(28, Pin.OUT, Pin.PULL_DOWN)
sensor = DHT11(pin)

while True:
    sleep(1)
    #BMP180
    BMP180_TEMP = bmp180.temperature
    pression = bmp180.pressure/1000.0
    #PICO SENSOR
    reading = sensor_temp.read_u16() * conversion_factor 
    PICO_TEMP = 27 - (reading - 0.706)/0.001721
    #DHT11
    DHT11_TEMP  = (sensor.temperature)
    DHT11_HUMIDITY = (sensor.humidity)
   
    print("BMP180 Temperature: {:.2f} °C\nDHT11  Temperature: {:.2f} °C\nPICO   Temperature: {:.2f} °C".format(BMP180_TEMP , DHT11_TEMP,PICO_TEMP))
    print("-------------------------");
    sleep(1)
