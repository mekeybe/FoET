import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]
comp = 4
troyka = 17
single = 3.3/2**8

GPIO.setmode(GPIO.BCM)

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)

def decimal2binary(decimal):
    return [int(i) for i in bin(decimal)[2:].zfill(8)]

def adc():
    number = 0
    for i in range(7, -1, -1):
        number += 2**i
        GPIO.output(dac, decimal2binary(number))
        time.sleep(0.05)
        comp_value = GPIO.input(comp)
        if comp_value == 0:
            number -= 2**i
    return number

try:
    while True:
        number = adc()
        i = 7
        while number < 2**i:
            i -= 1
        light = 0
        for j in range(i):
            light += 2**j
        GPIO.output(leds, decimal2binary(light))
        print("Число равно", number,"Напряжение равно", "{:.5f}".format(number * single))
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()