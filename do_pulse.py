# based on Trinket IO demo

import board
from digitalio import DigitalInOut, Direction, Pull
from analogio import AnalogOut, AnalogIn
import adafruit_dotstar as dotstar
import time
# import neopixel

# One pixel connected internally!
dot = dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1, brightness=0.05)

######################### HELPERS ##############################

def do_pulse():
    pulse = 0
    maxrange = 255
    for pulse in range(0,maxrange,5):
        dot[0]=(pulse,0,0)
        time.sleep(0.01)
        print((pulse))
    pulse = maxrange
    if pulse == maxrange:
        time.sleep(0.5)
        
    for pulse in range(maxrange,0,-5):
        dot[0]=(pulse,0,0)
        time.sleep(0.01)
    return pulse

######################### MAIN LOOP ##############################
while True:
  # spin internal LED around! autoshow is on
  # dot[0] = wheel(i & 255)
   
    do_pulse()
    
    time.sleep(0.25)
