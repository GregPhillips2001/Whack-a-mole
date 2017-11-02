#Greg Phillips
#11/1/17
#WhackAMole.py - Computer programming project whack-a-mole program

from ggame import *
from random import randint



if __name__ == '__main__': 
    
    red = Color(0xFF0000,1)
    black = Color(0x000000,1)
    white = Color(0xFFFFFF,1)
    
    blackCircle = CircleAsset(50,LineStyle(1,black), white)
    
    
    
    Sprite(blackCircle,(50,50))
    Sprite(blackCircle,(150,50))
    Sprite(blackCircle,(250,50))
    Sprite(blackCircle,(50,150))
    Sprite(blackCircle,(150,150))
    Sprite(blackCircle,(250,150))
    App().listenMouseEvent("click", mouseClick)
    App().run()

redCircle = CircleAsset(50,LineStyle(1,red),red) #(radius,outline,fill)