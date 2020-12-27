import rotatescreen
import time

# creating an object to access the main screen using SCREEN object
screen = rotatescreen.get_primary_display()

for i in range(4):
    # rotate screen to left 
    time.sleep(2) 
    screen.set_portrait_flipped()

    # flip screen opposite to your main screen
    time.sleep(2)
    screen.set_landscape_flipped()

    # rotate screen to right
    time.sleep(2) 
    screen.set_portrait()

    # Screen to Normal form
    time.sleep(2)
    screen.set_landscape()