#Ibrahim-Salah69
#touch logo in microbit
from microbit import *


while True:
    if pin_logo.is_touched():
        display.scroll("stop dont touc it is a trap")   
        display.show(Image.ANGRY)   
        
#tested on microbit v.2
