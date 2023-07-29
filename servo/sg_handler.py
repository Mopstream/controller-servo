import RPi.GPIO as GPIO
from .util import calculate_angle
import time

from servo import sg


def end():
    sg.stop()
    GPIO.cleanup()


def rotate(angle):
    mov = calculate_angle(angle)
    sg.ChangeDutyCycle(mov)


def feed():
    sg.ChangeDutyCycle(12.5)
    time.sleep(1)
    sg.ChangeDutyCycle(2.5)
