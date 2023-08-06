import sys
import time
#import RPi.GPIO as GPIO

class Relay():
    def __init__(self, gpio_number: int, name: str):
        self._gpio_number = gpio_number
        self._name = name
        self._manual_timeout_sec = 0
        self._auto_timeout_days = 0
        self._auto_timeout_time = 0
        #GPIO.setup(gpio_number, GPIO.OUT)

    def open(self):
        print("gpio open relay")
        #GPIO.output(self._gpio_number, GPIO.LOW)

    def close(self):
        print("gpio close relay")
        #GPIO.output(self._gpio_number, GPIO.HIGH)

    def get_name(self):
        return self._name

    def manual_set_timeout_sec(self, manual_timeout_sec = 0):
        print(f'manual_set_timeout_sec {manual_timeout_sec} GPIO {self._gpio_number}')
        self._manual_timeout_sec = manual_timeout_sec

    def manual_get_timeout_sec(self):
        print(f'manual_set_timeout_sec {self._manual_timeout_sec} GPIO {self._gpio_number}')
        return self._manual_timeout_sec

    def auto_set_planning(self, days = 0, time = 0):
        self._auto_timeout_days = days
        self._auto_timeout_time = time

    def auto_get_planning_days(self):
        return self._auto_timeout_days

    def auto_get_planning_time(self):
        return self._auto_timeout_time

    def auto_open(self):
        pass
