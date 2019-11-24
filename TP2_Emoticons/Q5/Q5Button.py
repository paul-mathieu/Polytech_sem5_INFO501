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
 

    def draw(self): 
        pygame.draw.rect(self.sensor.generalConfiguration.screen, (255,255,255), self.getPosition() +  [self.get_width(), self.get_height()],1  )
        
        
    

    #==========================================================================
    # Draws line on pygame screen     
    #==========================================================================
 

    def draw_lines(self, listValues): 
        
        screen = pygame.display.get_surface()
        # Creates the font
        font = pygame.font.Font(None, 15)
        
        positionIni = self.getPosition()
        position = self.getPosition()
        for element in listValues:
            # Creates the text image containing « This is a test » written in white
            textImage = font.render(element, 1, [255,255,255])
            
            
            position[0] = positionIni[0] + int((self.get_width() - textImage.get_rect().width) / 2)
            
            # Pastes the image on the screen. The upper left corner is at the position 100, 200
            screen.blit(textImage, position)  

            position[1] += 20
            
            
        
    



    #==========================================================================
    # Square for the emoticon
    #==========================================================================
    def printSquareEmoticon(self):
        
        #carre pour l'emoticonne
        widthRect = self.sensor.generalConfiguration.emoticonSize
        heightRect = self.sensor.generalConfiguration.emoticonSize
        x = self.sensor.generalConfiguration.screenWidth / 2 - widthRect / 2
        y = self.sensor.generalConfiguration.buttonHeight + self.sensor.generalConfiguration.emoticonBorder

        pygame.draw.rect(self.sensor.generalConfiguration.screen, (255,255,255), (x, y, widthRect, heightRect), 1  )
        
        #dessin de l'emoticonne
        #self.draw()    

    #==========================================================================
    # Square for the buttons
    #==========================================================================

    def printSquareButtons(self):
        
        #carre pour l'emoticonne
        widthRect = self.sensor.generalConfiguration.screenWidth
        heightRect = self.sensor.generalConfiguration.buttonHeight
        x = 0
        y = 0

        pygame.draw.rect(self.sensor.generalConfiguration.screen, (255,255,255), (x, y, widthRect, heightRect),1  )





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
    
    
    