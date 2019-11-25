# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: MATHIEU
"""


import pygame


class Button:

    
    def __init__(self, sensor) :
        self.sensor = sensor
 
    
    #==========================================================================
    # Draws rect on pygame screen     
    #==========================================================================
 

    def draw(self, valX): 
        
#        print("a")
        
        #draw all buttons :
        #first pos = wScreen / 2 - ( len(sensor) * wButton ) / 2
        buttonWidth = self.sensor.generalConfiguration.buttonWidth
        buttonHeight = self.sensor.generalConfiguration.buttonHeight
#        print(str(buttonWidth))
        
#        valX = self.sensor.generalConfiguration.screenWidth / 2 - (len(self.sensor.generalConfiguration.sensors) * buttonWidth) / 2
        
#        print(str(valX))
        
        pygame.draw.rect(self.sensor.generalConfiguration.screen, (255,255,255), (valX, 0, buttonWidth, buttonHeight), 1)
        self.draw_lines(['', self.sensor.getLabel(), '', self.sensor.read()], valX)
        
            
    

    #==========================================================================
    # Draws line on pygame screen     
    #==========================================================================
 

    def draw_lines(self, listValues, x): 
        
        screen = pygame.display.get_surface()
        # Creates the font
        font = pygame.font.Font(None, 15)
        
        position = [x, 1]
        for element in listValues:
            # Creates the text image containing « This is a test » written in white
            textImage = font.render(element, 1, [255,255,255])
            
            
            position[0] = position[0] + int((self.get_width() - textImage.get_rect().width) / 2)
            
            # Pastes the image on the screen. The upper left corner is at the position 100, 200
            screen.blit(textImage, position)  

            position[0] = x
            position[1] += 20




    #==========================================================================
    # Getter for the position
    #==========================================================================

    def getPosition(self):
            return [self.sensor.generalConfiguration.screenWidth / 2 - self.sensor.generalConfiguration.buttonWidth , 0]
  
    
    #==========================================================================
    # Test of display
    #==========================================================================


    def testButton(self):
        screen = pygame.display.get_surface()
        # Creates the font
        font = pygame.font.Font(None, 30)
        # Creates the text image containing « This is a test » written in white
        textImage = font.render('This is a test', 1, [255,255,255])
        # Pastes the image on the screen. The upper left corner is at the position 100, 200
        screen.blit(textImage, [100, 200])


    
    #==========================================================================
    # Getter for the the W and the H
    #==========================================================================
    
    def get_width(self):
        return self.sensor.generalConfiguration.buttonWidth
        
    def get_height(self):  
        return self.sensor.generalConfiguration.buttonHeight
    
    
    