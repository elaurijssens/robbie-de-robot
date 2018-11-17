from gpiozero import Robot
import time
import RPi.GPIO as GPIO

# GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

# set GPIO Pins
GPIO_TRIGGER = 17
GPIO_ECHO = 27

# set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

def afstand():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)

    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    StartTime = time.time()
    StopTime = time.time()

    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()

    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()

    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2

    return distance


robby = Robot(left = (7, 8), right = (9, 10))

bocht = 0.1

while True:

    d = afstand()

    print('Afstand is {:f}'.format(d))

    if d > 60:
        robby.forward(1, curve_right = bocht )
        time.sleep(0.2)
    elif (d > 40) & (d < 60):
        robby.forward((d - 40) / 20, curve_right = bocht )
        time.sleep(0.2)
    elif d < 10:
        robby.backward(0.5 , curve_right = bocht )
        time.sleep(1)
        robby.left(1)
        time.sleep(3)
    else:
        robby.stop()
        time.sleep(2)

        kwispel = 0

        while kwispel < 20:
            robby.left()
            time.sleep(0.1)
            robby.right()
            time.sleep(0.1)
            kwispel = kwispel + 1


