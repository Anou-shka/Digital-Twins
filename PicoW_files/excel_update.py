from machine import Pin
from utime import sleep
import urequests
import network
from wlan import wifi_connect
import wifi_pico_config as wifi
from time

# from read_airflow import read_pressure
from read_co2 import read_temp

# ✅ Connect to WiFi
wifi_connect()

# ✅ Server URL
server_url = wifi.url

while True: 
    try:
        
        wifi_connect()
        # Read temperature, humidity, and pressure values
        temp, temp_f, hum = read_temp()
#         ADC, Voltage, pressure = read_pressure()  # Ensure read_pressure() returns multiple values
        
        # Prepare data for transmission
        data = {
            'temperature_C': temp,
            'temperature_F': temp_f,
            'humidity': hum
#             'ADC': ADC,
#             'Voltage': Voltage,
#             'pressure_hpa': pressure
            }
        
        # Send data to the server
        response = urequests.post(server_url, json=data)
        response.close()
        print('Data sent successfully')

        # ✅ Print sensor readings
        print(f"Temperature: {temp:.3f} °C")
        print(f"Temperature: {temp_f:.3f} °F")
        print(f"Humidity: {hum:.3f} %")
#         print(f"Pressure: {pressure:.3f} hPa")

    except OSError as e:
        print("Error sending data:", e)

    time.sleep(10)  # ✅ Avoid excessive polling



