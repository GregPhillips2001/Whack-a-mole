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
    
    
    #Creates circles where mole can appear
    circle1 = Sprite(blackCircle,(50,50))
    circle2 = Sprite(blackCircle,(150,50))
    cirlcle3 = Sprite(blackCircle,(250,50))
    Sprite(blackCircle,(50,150))
    Sprite(blackCircle,(150,150))
    Sprite(blackCircle,(250,150))
    
    
    App().listenMouseEvent("click", mouseClick) #Listens for mouse click
    App().run()

redCircle = CircleAsset(50,LineStyle(1,red),red) #(radius,outline,fill)