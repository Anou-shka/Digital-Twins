import machine
import utime

PWM_PIN = 10  # GPIO pin connected to the sensor's PWM output
co2_pwm = machine.Pin(PWM_PIN, machine.Pin.IN)

def read_co2_pwm():
    """Reads PWM signal and calculates CO₂ concentration."""
    th_start = utime.ticks_us()
    
    # Wait for LOW to HIGH transition
    while co2_pwm.value() == 0:
        if utime.ticks_diff(utime.ticks_us(), th_start) > 5000000:  # 5-second timeout for warmup
            return None
    th = utime.ticks_us()
    
    # Wait for HIGH to LOW transition (th duration)
    while co2_pwm.value() == 1:
        if utime.ticks_diff(utime.ticks_us(), th) > 5000000:
            return None
    th = utime.ticks_diff(utime.ticks_us(), th) / 1000  # Convert to ms
    
    # Wait for LOW to HIGH transition (tl duration)
    tl_start = utime.ticks_us()
    while co2_pwm.value() == 0:
        if utime.ticks_diff(utime.ticks_us(), tl_start) > 5000000:
            return None
    tl = utime.ticks_diff(utime.ticks_us(), tl_start) / 1000  # Convert to ms
    
    
    # Calculate CO₂ concentration using the formula
    if th > 0:
        co2_ppm = 5000 * (th - 2) / (th + tl - 4)
        print(f"CO2 (PWM): {co2_ppm:.2f} ppm")
        return co2_ppm
    return None

print("Reading CO₂ from PWM... (Stabilizing for 10 seconds)")
utime.sleep(6000)  # Initial 10-minute warm-up period
print("Done")

while True:
    co2_ppm = read_co2_pwm()
    if co2_ppm is None:
        print("Failed to read PWM signal. Check wiring.")
    utime.sleep(15)  # Read every 15 seconds to match environmental response time

