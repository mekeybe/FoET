import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17
single = 3.3/2**8

GPIO.setmode(GPIO.BCM)

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def decimal2binary(decimal):
    return [int(i) for i in bin(decimal)[2:].zfill(8)]

def adc():
    k = 0
    for i in range(7, -1, -1):
        k += 2**i
        GPIO.output(dac, decimal2binary(k))
        time.sleep(0.05)
        comp_value = GPIO.input(comp)
        if comp_value == 0:
            k -= 2**i   
    return k  

try:
    while True:
        number = adc()
        print("Десятичное число равно", number, "Напряжение равно", "{:.5f}".format(number * single))
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()