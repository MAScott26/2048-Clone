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
            "Message :) "]
        
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
            
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("Background.png")
        self.square = Square(self)
        self.sprites = [self.square]
        
class Square(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("TestIMG.png")
        self.movespeed = 50
        self.keyDown = False
        self.squareState = {
            "ref" : ["image", "prev", "Next"],
            1 : ["image", 1, 2],
            2 : ["image", 2, 4],
            4 : ["image", 4, 8],
            8 : ["image", 8, 16],
            16 : ["image", 16, 32],
            32 : ["image", 32, 64],
            64 : ["image", 64, 128],
            128 : ["image", 128, 256],
            256 : ["image", 256, 512],
            512 : ["image", 512, 1024],
            1024 : ["image", 1024, 2048],
            2048 : ["image", 2048, 4096 ]
            }
        
    def process(self):
        if self.isKeyPressed(pygame.K_LEFT):
            if self.keyDown == False:
                self.x -= self.movespeed
                self.keyDown = True
            else:
                self.keyDown = True
        elif self.isKeyPressed(pygame.K_RIGHT):
            if self.keyDown == False:
                self.x += self.movespeed
                self.keyDown = True
            else:
                self.keyDown = True
        elif self.isKeyPressed(pygame.K_UP):
            if self.keyDown == False:
                self.y -= self.movespeed 
                self.keyDown = True
            else:
                self.keyDown = True
        elif self.isKeyPressed(pygame.K_DOWN):
            if self.keyDown == False:
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
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    keepGoing = False
            score = game.prevScore
        else:
            keepGoing = False
            
if __name__ == "__main__":
    main()