""""Twinkle.py
Display random colors on a strip of Neopixels
Date: 12/17/2017
Author: Darrell Little
This software is in the public domain
"""
from microbit import *
from random import choice
import neopixel

# Create a Neopixel instance
# Include the data pin it is connected to
# and the number of pixels in the strip
np = neopixel.NeoPixel(pin0, 2)

# Create the colors using Red, Green, Blue values
# 0 is off and 255 is full brightness
# Numbers in between results in a dimmer light
# Here are the three primary colors at about half-brightness
red = (155, 0, 0)
green = (0, 155, 0)
blue = (0, 0, 155)

# Remaining colors are a blend of the three primary colors
yellow = (155, 155, 0)
purple = (128, 0, 128)
teal = (0, 128, 128)

# Create a list of the colors 
randomColors = [red,green,blue,yellow,purple,teal]

# Create a list of times to display the color in milliseconds
randomTimes = [250,350,500]

while True:
    for pixel in range(0, len(np)):
        # Using choice picks a random item from the named list
        np[pixel] = choice(randomColors)
        np.show()
        sleep(choice(randomTimes))
