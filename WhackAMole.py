#Greg Phillips
#11/1/17
#WhackAMole.py - Computer programming project whack-a-mole program

from ggame import *
from random import randint



if __name__ == '__main__': 
    
    red = Color(0xFF0000,1)
    black = Color(0x000000,1)
    
    redCircle = CircleAsset(50,LineStyle(1,red),red) #(radius,outline,fill)

    App().run(step)

