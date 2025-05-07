# This code is for the Raspberry Pi Pico W
# It reads temperature, humidity, and CO2 data from sensors and update it on google sheets 
# using urequests
from machine import Pin
from utime import sleep
import urequests
import network
from wlan import wifi_connect
import wifi_pico_config as wifi
import time

# from read_airflow import read_pressure
from read_temp_hum import read_temp_hum
from read_co2 import read_co2


# ✅ Connect to WiFi
wifi_connect()

# ✅ Server URL
server_url = wifi.url

while True: 
    try:
        
        # Read temperature, humidity, and pressure values
        temp, temp_f, hum = read_temp_hum()
        co2 = read_co2()
#         ADC, Voltage, pressure = read_pressure()  # Ensure read_pressure() returns multiple values
        
        # Prepare data for transmission
        data = {
            'temperature_C': temp,
            'temperature_F': temp_f,
            'humidity': hum,
            'co2' : co2
#             'ADC': ADC,
#             'Voltage': Voltage,
#             'pressure_hpa': pressure
            }
        
        # Send data to the server
        response = urequests.post(server_url, json=data)
        print("Server response:", response.status_code, response.text)
        response.close()
        print('Data sent successfully')

        # ✅ Print sensor readings
        print(f"Temperature: {temp:.3f} °C")
        print(f"Temperature: {temp_f:.3f} °F")
        print(f"Humidity: {hum:.3f} %")
        print(f"Co2 Concentration: {co2} ppm")
#         print(f"Pressure: {pressure:.3f} hPa")

    except OSError as e:
        print("Error sending data:", e)
        

    time.sleep(10)  # ✅ Avoid excessive polling



