#==========================================================================
# File: Etch-A-Sketch           Creator: Tudor Mironovici   tcm26@njit.edu
#
# Purpose: A Turtle Graphics rendition of an Etch-A-Sketch
#==========================================================================

import turtle
from msvcrt import getch

#-----Variables-----
s = turtle.Screen()
t = turtle.Turtle()
mvmtLength = 2
penWidth = 2
#-------------------

#----------------------------
# Sets up the Etch-A-Sketch.
#----------------------------
print("Welcome to the Python Etch-A-Sketch! Keep this terminal open to input your key presses.\n")
print("ESC - quits out of the program\nSpace bar - clears the Etch-A-Sketch (takes a bit of moving to sketch again)\nDirectional Arrows - moves the Etch-a-Sketch pen in the respective directions\n\n\n")
t.hideturtle()
t.speed(1000)
t.width(penWidth)

#--------------------------------------
# Takes the user's keyboard inputs and
# interacts with the Turtle Screen.
#--------------------------------------
while True:
    key = ord(getch())
    #-----------------------------------
    # ESC input just exits the program.
    #-----------------------------------
    if (key == 27):
        break

    #----------------------------------
    # Spacebar input clears the screen
    # and leaves the pen where it was.
    #----------------------------------
    elif key == 32:
        s.clear()
        t.down()

    elif key == 224:
        key = ord(getch())

        #------------------------------------
        # Up arrow input moves the pen up by
        # the size of the mvmtLength int.
        #------------------------------------
        if key == 72:
            t.left(90)
            t.forward(mvmtLength)
            t.right(90)
        
        #-------------------------------------
        # down arrow input moves the pen down
        # by the size of the mvmtLength int.
        #-------------------------------------
        elif key == 80:
            t.right(90)
            t.forward(mvmtLength)
            t.left(90)

        #-------------------------------------
        # left arrow input moves the pen left
        # by the size of the mvmtLength int.
        #-------------------------------------
        elif key == 75:
            t.backward(mvmtLength)
        
        #----------------------------------------
        # right arrow input moves the pen right
        # by the size of the mvmtLength int.
        #---------------------------------------
        elif key == 77:
            t.forward(mvmtLength)