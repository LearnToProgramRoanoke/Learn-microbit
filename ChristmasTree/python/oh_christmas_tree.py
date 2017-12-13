from microbit import *
import music

# Create images for LED display
tree1 = Image("00500:09590:555555:00300:00300")
tree2 = Image("00900:05550:55555:00300:00300")
tree3 = Image("00500:09590:55555:00300:00300")
tree4 = Image("00500:05550:95559:00300:00300")
tree5 = Image("00500:05550:55955:00300:00300")
tree6 = Image("00500:05550:59595:00300:00300")

# Put images in a sequence inside a list
showTree = [tree1,tree2,tree3,tree4,tree5,tree6]

# Create song to play with display
music.set_tempo(ticks=8,bpm=40)
song1 = [
    "C4:2","F:1","F:1","F:2","G:2","A:1","A:1","A:2",
    "A:1","G:1","A:1","Bb:2","E:1","G:2","F:2",
    "C4:2","F:1","F:1","F:2","G:2","A:1","A:1","A:2",
    "A:1","G:1","A:1","Bb:2","E:1","G:2","F:2",
    "C:1","C:1","A:1","D5:4","C4:1","C:1","Bb:1","Bb:4",
    "Bb:1","Bb:1","G5:1","C4:4","Bb:1","Bb:1","A:2","A:2",
    "C4:2","F:1","F:1","F:1","G:2","A:1","A:1","A:1",
    "A:1","G:1","A:1","Bb:2","E:1","G:2","F:2"
]

while True:
    if button_a.is_pressed():
        # wait=False allows song to play without blocking
        music.play(song1,wait=False,loop=False)
        # display sequence of LED images
        display.show(showTree, delay=500, loop=True, wait=False)
