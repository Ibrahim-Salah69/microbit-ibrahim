#Ibrahim-Salah69
#greating in microbit
from microbit import *


while True:
    if button_a.is_pressed():
        display.scroll('hi')
        display.scroll('i am Ibrahim-Salah69')
        display.show(Image.HEART)
        sleep(2000)
        
#tested on microbit v.2