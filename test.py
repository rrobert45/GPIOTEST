import RPi.GPIO as GPIO

# Set the GPIO mode to BCM (Broadcom SOC channel)
GPIO.setmode(GPIO.BCM)

# Set individual pins as output pins
pin17 = 17
pin18= 18
pin19 = 19
pin20 = 20
pin21 = 21
pin22 = 22
pin23 = 23
pin24 = 24
GPIO.setup(pin17, GPIO.OUT)
GPIO.setup(pin18, GPIO.OUT)
GPIO.setup(pin19, GPIO.OUT)
GPIO.setup(pin20, GPIO.OUT)
GPIO.setup(pin21, GPIO.OUT)
GPIO.setup(pin22, GPIO.OUT)
GPIO.setup(pin23, GPIO.OUT)
GPIO.setup(pin24, GPIO.OUT)


#GPIO.output(pin17, GPIO.LOW)
GPIO.output(pin18, GPIO.LOW)
GPIO.output(pin19, GPIO.LOW)
GPIO.output(pin20, GPIO.LOW)
GPIO.output(pin21, GPIO.LOW)
GPIO.output(pin22, GPIO.LOW)
GPIO.output(pin23, GPIO.LOW)
GPIO.output(pin24, GPIO.LOW)

# Cleanup and exit
GPIO.cleanup()