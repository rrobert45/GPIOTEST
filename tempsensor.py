import Adafruit_DHT

# Set the sensor type and Raspberry Pi pin number
sensor = Adafruit_DHT.DHT22
pin = 4

# Try to get a reading from the sensor
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

# If a valid reading was taken, display the temperature and humidity
if humidity is not None and temperature is not None:
    print("Temperature: {:.1f} C".format(temperature))
    print("Humidity: {:.1f}%".format(humidity))
else:
    print("Failed to get reading from sensor.")