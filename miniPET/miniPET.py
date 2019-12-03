'''
miniPET.py
Title: Program your own micro:bit mini pet
Author: Darrell Little
Date: 12/2/2019
License: GNU General Public License v3.0
Permissions of this strong copyleft license 
are conditioned on making available complete 
source code of licensed works and modifications, 
which include larger works using a licensed work, 
under the same license. Copyright and license 
notices must be preserved.
'''

from microbit import *
display.scroll("PRESS A TO FEED")
display.scroll("PRESS B TO PLAY")
display.scroll("PRESS A + B TO SLEEP")

display.show(Image.RABBIT)
sleep(2000)

while True:
    if button_a.is_pressed() and button_b.is_pressed():
        display.show(Image.ASLEEP)
        sleep(2000)
    elif button_b.is_pressed():
        display.show(Image.HAPPY)
        sleep(2000)
    elif button_a.is_pressed():
        display.show(Image.HEART)
        sleep(2000)
    else:
        display.show(Image.RABBIT)
    
