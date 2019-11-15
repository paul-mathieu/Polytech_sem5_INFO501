# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""

import pygame
import math

class Emoticon:

    #=============================================================================
    #=============================================================================
    # Part I - Initialisation
    #=============================================================================
    #=============================================================================
    
    
    #==========================================================================
    # Constructor
    #==========================================================================    
    def setGeneralConfiguration(self, generalConfiguration):
        self.generalConfiguration = generalConfiguration



    #==========================================================================
    # Constructor
    #==========================================================================    
    def headToArea(self):
        
        #position du centre du nouveau carre
        x = self.generalConfiguration.screenWidth / 2
        y = self.generalConfiguration.buttonHeight + self.generalConfiguration.emoticonBorder + self.generalConfiguration.emoticonSize / 2

        
        return x, y



    #=============================================================================
    #=============================================================================
    # Part II - Draw
    #=============================================================================
    #=============================================================================

 
    #==========================================================================
    # Draws on pygame screen      
    #==========================================================================
    def draw(self):
        
        #for the buttons
        self.printSquareButtons()
        
        #for the emoticon
        self.printSquareEmoticon()        
    
    #==========================================================================
    #Square for the emoticon
    #==========================================================================
    def printSquareEmoticon(self):
        
        #carre pour l'emoticonne
        widthRect = self.generalConfiguration.emoticonSize
        heightRect = self.generalConfiguration.emoticonSize
        x = self.generalConfiguration.screenWidth / 2 - widthRect / 2
        y = self.generalConfiguration.buttonHeight + self.generalConfiguration.emoticonBorder

        pygame.draw.rect(self.generalConfiguration.screen, (255,255,255), (x, y, widthRect, heightRect),1  )
        
        #dessin de l'emoticonne
        #self.draw()    



    #=============================================================================
    #=============================================================================
    # Part III - Buttons
    #=============================================================================
    #=============================================================================


        
    #==========================================================================
    # 
    #==========================================================================

    def printSquareButtons(self):
        
        #carre pour l'emoticonne
        widthRect = self.generalConfiguration.screenWidth
        heightRect = self.generalConfiguration.buttonHeight
        x = 0
        y = 0

        pygame.draw.rect(self.generalConfiguration.screen, (255,255,255), (x, y, widthRect, heightRect),1  )







