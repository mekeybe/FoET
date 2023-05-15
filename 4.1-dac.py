import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

def decimal2binary(value):
    return [int(i) for i in bin(value)[2:].zfill(8)]

dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setup(dac, GPIO.OUT)

try:
    while True:
        number = input()
        if number == 'q':
            break
        elif (0 <= int(number) <= 255) and (number.isdigit()) and (int(number) % 1 == 0):
            GPIO.output(dac, decimal2binary(int(number)))
            print(decimal2binary(int(number)))
            print("{:.8}".format(int(number)/256*3.3), "Вольт")
        elif (not number.isdigit()):
            print("Введённое число - не число")
        elif (int(number) > 255):
            print("Введённое число превышает возможности 8-разрядного ЦАП")
        elif (int(number) < 0):
            print("Введённое число отрицательное")
        elif ((int(number) % 1) != 0):
            print("Введённое число не целое")
except ValueError:
    print("Введите число от 0 до 255")
except KeyboardInterrupt:
    print("Программа была прервана")
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()