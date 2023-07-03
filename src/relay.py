import sys
import time
#import RPi.GPIO as GPIO

class Relay():
    def __init__(self, gpio_number: int, name: str):
        self._gpio_number = gpio_number
        self._manual_timeout_sec = 0
        self._name = name
        #GPIO.setup(gpio_number, GPIO.OUT)

    def open(self):
        print("open relay")
        #GPIO.output(self._gpio_number, GPIO.LOW)

    def close(self):
        pass
        #GPIO.output(self._gpio_number, GPIO.HIGH)

    def get_name(self):
        return self._name

    def manual_set_timeout_sec(self, manual_timeout_sec = 0):
        print(f'manual_set_timeout_sec {manual_timeout_sec} GPIO {self._gpio_number}')
        self._manual_timeout_sec = manual_timeout_sec

    def manual_get_timeout_sec(self):
        print(f'manual_set_timeout_sec {self._manual_timeout_sec} GPIO {self._gpio_number}')
        return self._manual_timeout_sec

    def manual_open(self):
        print(f'manual_open GPIO {self._gpio_number}')
        self.open()
        time.sleep(self._manual_timeout_sec)
        self.close()

    def auto_set_planning(self, days = 0, time = 0):
        pass

    def auto_open(self):
        pass
