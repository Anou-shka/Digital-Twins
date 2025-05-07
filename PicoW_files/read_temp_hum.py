# This code is for reading temperature and humidity from a DHT22 sensor
# using the Raspberry Pi Pico W. It uses the DHT library to interface with the sensor.
# The code initializes the sensor, reads temperature and humidity values, and converts the temperature from Celsius to Fahrenheit.

from machine import Pin
from time import sleep
import dht 

sensor = dht.DHT22(Pin(22))

def read_temp():
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    temp_f = temp * (9/5) + 32.0
    return temp, temp_f, hum

# while True:
#   try:
#     sleep(2)
#     temp, temp_f, hum = read_temp()
#     print('Temperature: %3.1f C' %temp)
#     print('Temperature: %3.1f F' %temp_f)
#     print('Humidity: %3.1f %%' %hum)
#   except OSError as e:
#     print('Failed to read sensor.', e)


