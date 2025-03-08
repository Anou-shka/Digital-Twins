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


