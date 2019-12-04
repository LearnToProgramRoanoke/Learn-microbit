'''
miniPET_advanced.py
Title: Program your own micro:bit mini pet
Author: Darrell Little
Date: 12/3/2019
License: GNU General Public License v3.0
Permissions of this strong copyleft license 
are conditioned on making available complete 
source code of licensed works and modifications, 
which include larger works using a licensed work, 
under the same license. Copyright and license 
notices must be preserved.
'''

from microbit import *

# Create variables for tracking health level and timer count down
timer = 60
health = 3
# Change Image for a different type of pet
myPet = Image.RABBIT

# Display instructions 
display.scroll("PRESS A TO FEED")
display.scroll("B TO PLAY")
display.scroll("A + B TO SLEEP")

# temp display of pet for testing
#display.show(myPet)
#sleep(2000)

# main game loop 
while True:
    # check for timer value, if zero decrease health value, reset timer
    if timer < 1:
        health -= 1
        timer = 60
    else:
        # If/Else statements checking for a button press
        # Increase health for each action taken
        if button_a.is_pressed() and button_b.is_pressed():
            display.show(Image.ASLEEP)
            sleep(1000)
            health += 1
            display.scroll(str(health))
            sleep(500)
        elif button_b.is_pressed():
            display.show(Image.HAPPY)
            sleep(1000)
            health += 1
            display.scroll(str(health))
            sleep(500)
        elif button_a.is_pressed():
            display.show(Image.HEART)
            sleep(1000)
            health += 1
            display.scroll(str(health))
            sleep(500)
        else:
            # If no button is pressed, check health level then display image of pet
            if health < 1:
                # Game ends when health drops to zero
                # break exits the loop and stops program
                display.scroll("Game Over")
                break
            else:
                # display pet for 1 second and count down the timer
                display.show(myPet)
                sleep(1000)
                timer -= 1
                #Temp display of timer count down for testing
                #display.scroll(str(timer))
                #sleep(500)
			    