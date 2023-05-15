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

def adc(value):
    signal = decimal2binary(value)
    GPIO.output(dac, signal)
    comp_value = GPIO.input(comp) 
#Не понимаю зачем мы считываем значение компаратора, если никуда его не выводим
    voltage = value * single
    return voltage

try:
    while True:
        for i in range(256):
            voltage = adc(i)
            time.sleep(0.05)
            print("Десятичное число равно ", i, "и напряжение равно ", "{:.5f}".format(voltage))
except KeyboardInterrupt:
    print("Программа была прервана")
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()