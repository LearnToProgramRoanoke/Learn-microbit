from microbit import *

snow1 = Image("00900:90909:09090:90909:00000")
snow2 = Image("00500:90909:09090:90909:05050")
snow3 = Image("00300:50505:09090:90909:09090")
snow4 = Image("00100:10101:05050:90909:09090")
snow5 = Image("00000:00000:01010:50505:05050")
snow6 = Image("00000:00000:00000:10101:01010")
snow7 = Image("00000:00000:00000:00000:01010")

snow_globe = [Image.HOUSE, snow1, snow2, snow3, snow4, snow5, snow6, snow7, Image.HOUSE]

display.scroll("SHAKE FOR SNOW")
display.show(Image.HOUSE)

while True:
  if accelerometer.was_gesture('shake'):
    display.show(snow_globe, delay=1000)