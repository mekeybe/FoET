import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
 
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.IN)

GPIO.output(18, GPIO.input(22))