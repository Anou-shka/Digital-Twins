# This file is part of the PicoW project.
# It contains the main function that runs when the Pico W is powered on.
# It lights up the LED to confirm that main.py has run.
import machine
import time

def pico_main_run():
    led = machine.Pin('LED', machine.Pin.OUT)
    start_time = time.time()  # Get the current time when the loop starts
    while time.time() - start_time < 5:  # Run for 5 seconds
        led.on()
        time.sleep(0.5)
        led.off()
        time.sleep(0.5)
    print("Stopped after 5 seconds")

