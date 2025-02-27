import time
from wlan import wifi_connect
from wifi_access_point import wifi_access_point


# Connect to WiFi
wifi_connect()

# Connect to Access Point
wifi_access_point()



## Connect to the wifi
## Read and Send the data from the sensors to firebase database
## Figure out the timestamp 
## Sleep for 5 mins and restart the whole thing
## Average lift time per person (5-floor trip): ~47.5 seconds   
## Maximum lift time (full 10-floor trip): ~85.5 seconds
## For your project, use ~45-50 seconds as a reasonable estimate for the average lift time per passenger. 🚀


