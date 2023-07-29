import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
sg = GPIO.PWM(17, 50)
sg.start(2.5)
