from microbit import *
import random

rock = Image("00900:"
             "09990:"
             "99999:"
             "09990:"
             "00900:")
paper = Image("99999:"
              "90009:"
              "90009:"
              "90009:"
              "99999:")
scissors = Image("99009:"
                 "99090:"
                 "00900:"
                 "99090:"
                 "99009:")

display.scroll("ROCK")
display.show(rock)
sleep(500)

display.scroll("PAPER")
display.show(paper)
sleep(500)

display.scroll("SCISSORS")
display.show(scissors)
sleep(500)

display.scroll("SHAKE OR PRESS B TO PLAY!")
sleep(500)

def playAction():
  play_item = random.randint(1,3)
  if play_item == 1:
    display.show(rock)
  if play_item == 2:
    display.show(paper)
  if play_item == 3:
    display.show(scissors)

while True:
  if accelerometer.was_gesture('shake'):
    playAction()
  elif button_b.is_pressed():
    playAction()