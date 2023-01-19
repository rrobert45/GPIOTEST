import RPi.GPIO as GPIO
import time

# Set the pin numbers for the 8 pins of the relay
relay_pins = [17, 18, 19, 20, 21, 22, 23, 24]

# Set the duration for the relay to be on (in seconds)
on_duration = 1

# Set up the GPIO pins for output
GPIO.setmode(GPIO.BCM)
for pin in relay_pins:
    GPIO.setup(pin, GPIO.OUT)

while True:
    # Turn on each relay in sequence
    for pin in relay_pins:
        GPIO.output(pin, GPIO.HIGH)
        print(f"Relay {pin} is ON")
        time.sleep(on_duration)

    # Turn off each relay in sequence
    for pin in relay_pins:
        GPIO.output(pin, GPIO.LOW)
        print(f"Relay {pin} is OFF")
        time.sleep(on_duration)
