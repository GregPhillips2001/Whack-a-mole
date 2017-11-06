#Greg Phillips
#11/1/17
#WhackAMole.py - Computer programming project whack-a-mole program

from ggame import *
from random import randint


#Knows what circle is clicked if you click a circle
#Knows if you click a mole
def mouseClick(event):
    if event.x >= 0 and event.x <= 100 and event.y >= 0 and event.y <= 100 and data["mole1"] == True:
        updateScore()
    if event.x >= 101 and event.x <= 200 and event.y >= 0 and event.y <= 100 and data["mole2"] == True:
        updateScore()
    if event.x >= 201 and event.x <= 300 and event.y >= 0 and event.y <= 100 and data["mole3"] == True:
        updateScore()
    if event.x >= 0 and event.x <= 100 and event.y >= 101 and event.y <= 200 and data["mole4"] == True:
        updateScore()
    if event.x >= 101 and event.x <= 200 and event.y >= 101 and event.y <= 200 and data["mole5"] == True:
        updateScore()
    if event.x >= 201 and event.x <= 300 and event.y >= 101 and event.y <= 200 and data["mole6"] == True:
        updateScore()


#Sprites moles in random circles
def moleAppear():
    redCircle = CircleAsset(50,LineStyle(1,red),red) #(radius,outline,fill)
    whiteCircle = CircleAsset(50,LineStyle(1,black),white)
    
    #Cicle1
    num = randint(1,5)
    if num == 1:
        Sprite(redCircle,(50,50)) #(num of pixels right, num of pixels down)
        data["mole1"] = True
    else:
        Sprite(whiteCircle,(50,50))
        data["mole1"] = False
    
    #Circle2
    num = randint(1,5)
    if num == 1:
        Sprite(redCircle,(150,50)) #(num of pixels right, num of pixels down)
        data["mole2"] = True
    else:
        Sprite(whiteCircle,(150,50))
        data["mole2"] = False
    
    #Circle3
    num = randint(1,5)
    if num == 1:
        Sprite(redCircle,(250,50)) #(num of pixels right, num of pixels down)
        data["mole3"] = True
    else:
        Sprite(whiteCircle,(250,50))
        data["mole3"] = False
        
    #Circle4
    num = randint(1,5)
    if num == 1:
        Sprite(redCircle,(50,150)) #(num of pixels right, num of pixels down)
        data["mole4"] = True
    else:
        Sprite(whiteCircle,(50,150))
        data["mole4"] = False
    
    #Circle5
    num = randint(1,5)
    if num == 1:
        Sprite(redCircle,(150,150)) #(num of pixels right, num of pixels down)
        data["mole5"] = True
    else:
        Sprite(whiteCircle,(150,150))
        data["mole5"] = False
        
    #Circle60
    num = randint(1,5)
    if num == 1:
        Sprite(redCircle,(250,150)) #(num of pixels right, num of pixels down)
        data["mole6"] = True
    else:
        Sprite(whiteCircle,(250,150))
        data["mole6"] = False
        

        
    
    
#keeps track of how many frames have passed
#new moles after more than 50 frames have passed
def step():
    data["frames"] += 1
    if data["frames"] == 1000:
        gameover()
    if data["frames"]% 50 == 0:
        moleAppear()

def gameover():
    whiteRectangle = RectangleAsset(1000,1000,LineStyle(1,white),white)
    gameovertext = TextAsset("Game Over!")
    
    Sprite(whiteRectangle)
    Sprite(gameovertext, (400,200))

def updateScore():
    data["score"] += 10
    data["scoreText"].destroy()
    scoreBox = TextAsset("Score = "+str(data["score"]))
    data["scoreText"] = Sprite(scoreBox, (25,225))


if __name__ == '__main__': 
    
    #Dictionary
    data = {}
    data["score"] = 0
    data["frames"] = 0
    data["mole1"] = False
    data["mole2"] = False
    data["mole3"] = False
    data["mole4"] = False
    data["mole5"] = False
    data["mole6"] = False
    
    red = Color(0xFF0000,1)
    black = Color(0x000000,1)
    white = Color(0xFFFFFF,1)
    
    blackCircle = CircleAsset(50,LineStyle(1,black), white)
    
    #Creates circles where mole can appear
    circle1 = Sprite(blackCircle,(50,50)) #(num of pixels right, num of pixels down)
    circle2 = Sprite(blackCircle,(150,50))
    circle3 = Sprite(blackCircle,(250,50))
    circle4 = Sprite(blackCircle,(50,150))
    circle5 = Sprite(blackCircle,(150,150))
    circle6 = Sprite(blackCircle,(250,150))
    
    scoreBox = TextAsset("Score = 0")
    
    data["scoreText"] = Sprite(scoreBox, (25,225))
        
    App().listenMouseEvent("click", mouseClick) #Listens for mouse click
    App().run(step)

