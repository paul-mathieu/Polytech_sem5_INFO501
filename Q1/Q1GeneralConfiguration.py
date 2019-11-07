# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""
import pygame
import math

class GeneralConfiguration:
    # Constructor
    def __init__(self, largeurEcran, hauteurEcran) :
        
        self.largeurEcran = largeurEcran
        self.hauteurEcran = hauteurEcran
        
        self.initPygame(largeurEcran, hauteurEcran)
        
        # Parameters for the buttons
        self.buttonWidth = 150
        self.buttonHeight = 80
        
        # Parameters for the emoticons
        self.emoticonSize = 400
        self.emoticonBorder = 20

    # Initializes pygame
    def initPygame(self, largeurEcran, hauteurEcran):
        
        #Initialization
        pygame.init()
        # Sets the screen size.
        pygame.display.set_mode((largeurEcran, hauteurEcran))    
        # Sets the timer to check event every 200 ms
        pygame.time.set_timer(pygame.USEREVENT, 200)
        # Gets pygame screen
        self.screen = pygame.display.get_surface()
        
    # Draws on pygame screen    
    def draw(self):
        
        centreX = int(self.largeurEcran/2)
        centreY = int(self.hauteurEcran/2)
        largeurEllipse = 15
        rayonTete = 80
        
        # Draws a circle in red with a center in 100, 100 and a radius equal to 80
        pygame.draw.circle(self.screen, [255, 0, 0], [centreX, centreY], rayonTete) 
        
        #Q1.c) Rectangle blanc
        #pygame.draw.rect(self.screen, [255, 255, 255], [centreX - rayonTete, centreY - rayonTete, rayonTete*2, rayonTete*2], 1) 


        # Draws a black ellipse contained in a rectangle whose left upper corner is 50,60, 
        # width=15 and height=20
        
        #oeil droit
        pygame.draw.ellipse(self.screen, [255,255,255], [centreX + 30 - int(largeurEllipse/2), centreY - 30, largeurEllipse, 20])

        #oeil gauche
        pygame.draw.ellipse(self.screen, [255,255,255], [centreX - 30 - int(largeurEllipse/2), centreY - 30, largeurEllipse, 20])


        # Draws a black arc contained in a rectangle whose left upper corner  is 60,120, 
        # width=80, height=30, starting angle=5*pi/4, ending angle=7*pi/4
        
        #bouche
        
        #si le visage sourit
        pygame.draw.arc(self.screen, [255,255,255], [centreX - int(80 / 2), centreY + 10, 80, 30], 7*math.pi/6, 11*math.pi/6)
        
        #si le visage ne sourrit pas
        #pygame.draw.arc(self.screen, [255,255,255], [centreX - int(80 / 2), centreY + 11, 80, 30], 1*math.pi/6, 5*math.pi/6)
        
        #si le visage est ni content ni mécontent
        #pygame.draw.line(self.screen, [0,0,0], [50,100], [150,100]) 
        
       
            
    # Displays pygame screen
    def display(self):
        # Draws on the screen surface
        self.draw()        
        # Updates the displat and clears new timer events
        pygame.display.flip()
        pygame.event.clear(pygame.USEREVENT)

        
        