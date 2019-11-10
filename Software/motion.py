import RPi.GPIO as GPIO
import time

PIR_input = 12
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIR_input,GPIO.IN)

while True:
    time.sleep(0.1)
    if(GPIO.input(PIR_input)):
        print("Motion detected")
    else:
        print("No motion detected")

