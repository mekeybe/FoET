import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

def decimal2binary(value):
    return [int(i) for i in bin(value)[2:].zfill(8)]

dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setup(dac, GPIO.OUT)

try:
    while True:
        T = input("Введите период треугольного сигнала: ")
        if (T == "Quit"):
            break
        elif (not T.isdigit()):
            print("Вы ввели не число")
        t = int(T)/512
        for i in range(256):
            GPIO.output(dac, decimal2binary(i))
            time.sleep(t)
        for i in range(255, -1, -1):
            GPIO.output(dac, decimal2binary(i))
            time.sleep(t)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
