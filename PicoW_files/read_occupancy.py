from machine import Pin
import time

# Define sensor and LED pins
e18_sensor = Pin(3, Pin.IN)  # GP3 for IR Proximity Sensor (Signal wire)
led = Pin(2, Pin.OUT) 

# Counters
people_count = 0
occupancy = 0  # Track the number of people currently inside
last_detection_time = time.time()

# Lift timing configurations
average_floor_time = 10  # Time (seconds) for lift to move between floors
door_open_time = 3       # Time (seconds) the door stays open

print("Lift Monitoring Started...")

while True:
    state = e18_sensor.value()

    if state == 0:  # Object detected near buttons (~30cm range)
        print("Object Detected Near Lift Buttons")
        led.value(1)  # Turn LED on

        entry_time = time.time()

        # Wait for the person to cross the sensor
        while e18_sensor.value() == 0:
            time.sleep(0.1)

        exit_time = time.time()
        crossing_time = exit_time - entry_time

        if crossing_time < 1.5:  # Threshold for a single person detection
            if entry_time - last_detection_time < 2:  # Quick re-detection means entry
                people_count += 1
                occupancy += 1
                print(f"Person Entered | Current Occupancy: {occupancy} | Total Entered: {people_count}")
            else:  # Longer interval means exit
                people_count -= 1
                occupancy -= 1
                occupancy = max(0, occupancy)  # Prevent negative values
                print(f"Person Exited | Current Occupancy: {occupancy} | Total Entered: {people_count}")
        
        last_detection_time = time.time()  # Update movement time

    else:
        led.value(0)  # Turn LED off

    # Reset counters if the lift is inactive for too long
    if time.time() - last_detection_time > average_floor_time:
        print("Lift inactive for too long. Resetting occupancy and people count...")
        people_count = 0
        occupancy = 0

    time.sleep(0.5)  # Short delay to avoid redundant readings

