# -*- coding: utf-8 -*-
"""
Another 2048 clone

@author: Michael Scott
"""
import pygame, simpleGE, random

class startScreen(simpleGE.Scene):
    def __init__(self, score):
        super().__init__()
        self.setImage("Background.png")
        
        self.instructions = simpleGE.MultiLabel()
        self.instructions.textLines = [
            "use the arrow keys to move all tiles ",
            "get to 2048 to win",
            "press up to play",
            "press down to quit"]
        
        self.instructions.center = (320, 240)
        self.instructions.size = (550, 300)
        
        self.btnPlay = simpleGE.Button()
        self.btnPlay.center = (150, 420)
        self.btnPlay.text = "Play"
        self.btnQuit = simpleGE.Button()
        self.btnQuit.center = (500, 420)
        self.btnQuit.text = "Quit"
        
        self.lblPScore = simpleGE.Label()
        self.lblPScore.center = (320, 50)
        self.lblPScore.size = (200, 30)
        self.lblPScore.bgColor = "white"
        self.lblPScore.fgColor = "black"
        self.lblPScore.text = f"previous score: {score} "
        
        self.sprites = [self.instructions, self.btnPlay, self.btnQuit, self.lblPScore]
             
    def process(self):
        if self.btnQuit.clicked or self.isKeyPressed(pygame.K_DOWN):
            self.response = "Quit"
            self.stop()
        if self.btnPlay.clicked or self.isKeyPressed(pygame.K_UP):
            self.response = "Play"
            self.stop()
            
class Grid(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Grid.png")
        self.x = 320
        self.y = 240
        
            
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("Background.png")
        self.grid = Grid(self)
        self.tiles = []
        for i in range(12):
            self.tiles.append(Square(self))
            
            
            
        """self.tiles.append(Square(self))
        self.square.currState = 1
        self.square.imgUpdate()
        self.tiles.append(self.square)"""
        
        self.sprites = [self.grid, self.tiles]
        
    def process(self):
        for i in self.tiles:
            for j in self.tiles:
                if i != j:
                    if i.currState == j.currState:
                        if i.collidesWith(j):
                            print(i.currState)
                            j.hide()
                            i.currState += 1
                            print(i.currState)
                            i.imgUpdate()
                            j.x = random.randrange(170, 471, 100)
                            j.y = random.randrange(90, 391, 100)
                            j.show()
                        
                        
class Square(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.currState = 0
        self.squareState = [
            "imgOne.png",
            "imgTwo.png",
            "imgFour.png",
            "imgEight.png",
            "imgSixT.png",
            "imgThirT.png",
            "img64.png",
            "img128.png",
            "img256.png",
            "img512.png",
            "img1024.png",
            "img2048.png"
            ]
        self.setImage(self.squareState[self.currState])
        self.setSize(95, 95)
        self.movespeed = 100
        self.xValues = [170, 270, 370, 470]
        self.yValues = [90, 190, 290, 390]
        self.x = random.randrange(170, 471, 100)
        self.y = random.randrange(90, 391, 100)
        self.keyDown = False
        
    def imgUpdate(self):
        self.setImage(self.squareState[self.currState])
        
    def process(self):
        if self.isKeyPressed(pygame.K_LEFT):
            if self.x != 170:
                if self.keyDown == False:
                    move = True
                    for i in range(3):
                        for tile in self.scene.tiles:
                            if tile.x + 100 == self.x and tile.y == self.y and tile.currState != self.currState:
                                move = False
                        if move:
                            if self.x != 170:
                                self.x -= self.movespeed
                    self.keyDown = True
                else:
                    self.keyDown = True
        elif self.isKeyPressed(pygame.K_RIGHT):
            if self.x != 470:
                if self.keyDown == False:
                    move = True
                    for i in range(3):
                        for tile in self.scene.tiles:
                            if tile.x - 100 == self.x and tile.y == self.y and tile.currState != self.currState:
                                move = False
                        if move:
                            if self.x != 470:
                                self.x += self.movespeed
                    self.keyDown = True
                else:
                    self.keyDown = True
        elif self.isKeyPressed(pygame.K_UP):
            if self.y != 90:
                if self.keyDown == False:
                    move = True
                    for i in range(3):
                        for tile in self.scene.tiles:
                            if tile.y + 100 == self.y and tile.x == self.x and tile.currState != self.currState:
                                move = False
                        if move:
                            if self.y != 90:
                                self.y -= self.movespeed 
                    self.keyDown = True
                else:
                    self.keyDown = True
        elif self.isKeyPressed(pygame.K_DOWN):
            if self.y != 390:
                if self.keyDown == False:
                    move = True
                    for i in range(3):
                        for tile in self.scene.tiles:
                            if tile.y - 100 == self.y and tile.x == self.x and tile.currState != self.currState:
                                move = False
                        if move:
                            if self.y != 390:
                                self.y += self.movespeed
                    self.keyDown = True
                else:
                    self.keyDown = True
        else:
            self.keyDown = False
            
            
            
def main():
    keepGoing = True
    score = 0
    
    startMenu = startScreen(score)
    startMenu.start()
    while keepGoing:   
        if startMenu.response == "Play":
            game = Game()
            game.start()
            keepGoing = False
        else:
            keepGoing = False
            
if __name__ == "__main__":
    main()