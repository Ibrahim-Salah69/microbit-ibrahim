from microbit import *
from ultrasonic import Ultrasonic
from ssd1306 import initialize, clear_oled
from ssd1306_text import add_text

while True:
    distance_value = ultrasonic_sensor.measure_distance_cm()
    motion = pin2.read_digital()

    add_text(0, 0, distance_value)
    add_text(0, 1, "Hi")
    add_text(0, 2, "------")
    add_text(0, 3, "Meqdad")

    if distance_value <= 20:
        if motion == 1:
            pin1.write_digital(1)
            pin0.write_digital(1)
        else:
            pin1.write_digital(0)
            pin0.write_digital(0)
