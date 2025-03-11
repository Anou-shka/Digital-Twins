from wlan import wifi_connect
from ap import wifi_access_point
from test import pico_main_run

## Connecting to Wifi
wifi_connect()

## Creating an access point for pico 
# wifi_access_point()  #Dont need it as of now 

## Blinking the LED light to confirm that main.py ran
pico_main_run()



## Connect to the wifi
## Read and Send the data from the sensors to firebase database
## Figure out the timestamp 
## Sleep for 5 mins and restart the whole thing
## Average lift time per person (5-floor trip): ~47.5 seconds   
## Maximum lift time (full 10-floor trip): ~85.5 seconds
## For your project, use ~45-50 seconds as a reasonable estimate for the average lift time per passenger. 🚀


