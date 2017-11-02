#Greg Phillips
#11/1/17
#WhackAMole.py - Computer programming project whack-a-mole program

from ggame import *
from random import randint


#Knows what circle is clicked if you click a circle
def mouseClick(event):
    if event.x >= 0 and event.x <= 100 and event.y >= 0 and event.y <= 100:
        print("Circle 1")
    if event.x >= 101 and event.x <= 200 and event.y >= 0 and event.y <= 100:
        print("Circle 2")
    if event.x >= 201 and event.x <= 300 and event.y >= 0 and event.y <= 100:
        print("Circle 3")
    if event.x >= 0 and event.x <= 100 and event.y >= 101 and event.y <= 200:
        print("Circle 4")
    if event.x >= 101 and event.x <= 200 and event.y >= 101 and event.y <= 200:
        print("Circle 5")
    if event.x >= 201 and event.x <= 300 and event.y >= 101 and event.y <= 200:
        print("Circle 6")


#Sprites moles in random circles
def moleAppear():
    num = randint(1,5)
    
    if num == 1:
        
    
    
#keeps track of how many frames have passed
#new moles after more than x frames have passed
def step():
    data["frames"] += 1
    if data["frames"] == 200:
        moleAppear()



if __name__ == '__main__': 
    
    data = {}
    data["score"] = 0
    data["frames"] = 0
    
    red = Color(0xFF0000,1)
    black = Color(0x000000,1)
    white = Color(0xFFFFFF,1)
    
    blackCircle = CircleAsset(50,LineStyle(1,black), white)
    redCircle = CircleAsset(50,LineStyle(1,red),red) #(radius,outline,fill)
    
    #Creates circles where mole can appear
    circle1 = Sprite(blackCircle,(50,50)) #(num of pixels right, num of pixels down)
    circle2 = Sprite(blackCircle,(150,50))
    circle3 = Sprite(blackCircle,(250,50))
    circle4 = Sprite(blackCircle,(50,150))
    circle5 = Sprite(blackCircle,(150,150))
    circle6 = Sprite(blackCircle,(250,150))
    
    
    App().listenMouseEvent("click", mouseClick) #Listens for mouse click
    App().run()

