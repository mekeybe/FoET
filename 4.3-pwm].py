import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.OUT)

P = GPIO.PWM(23, 1000)
P.start(0)

try:
    while True:
        D = int(input("Введите рабочий цикл: "))
        P.ChangeDutyCycle(D)
        print("{:.2f}".format(D*3.3/100))
finally:
    GPIO.OUTPUT(22, 0)
    GPIO.cleanup()