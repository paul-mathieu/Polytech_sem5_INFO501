# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""

import pygame
import math
  
class Emoticon:
    # Constructor
    def __init__(self, sensor) :
        self.sensor = sensor
        


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

    def headToArea(self, position):
        
        x, y = position
        t_emo = self.generalConfiguration.emoticonSize
        t_bout= self.generalConfiguration.buttonHeight
        t_bord=self.generalConfiguration.emoticonBorder      
        t_ecran =self.generalConfiguration.screenWidth
        
        #position prime
        new_y = t_bout+t_bord+(t_emo//2)-y
        new_x = x+(t_ecran//2)

        
        return [new_x, new_y]

        
    #==========================================================================
    # Setter
    #==========================================================================    
    def setEmoticonParameters(self, size) :  
        self.eyeWidth = 0.1*size 
        self.eyeHeight = 0.15*size
        self.eyeLeftPosition = [-0.15*size, 0.1*size] 
        self.eyeRightPosition = [0.15*size, 0.1*size] 
        self.mouthPosition = [0, -0.25*size]
        self.mouthMaxHeight = 0.3*size 
        self.mouthMaxWidth = 0.55*size 
        self.mouthAngle = math.pi/10 
        
        
        

    #==========================================================================
    # Color
    #==========================================================================    
    def color(self,x):
        if x<=0:
            rouge = 255
            vert = 255 +x*255
        else:
            rouge = 255 -x*255
            vert = 255
        
        return (rouge,vert,0)

    #=============================================================================
    #=============================================================================
    # Part II - Draw
    #=============================================================================
    #=============================================================================

 
    #==========================================================================
    # Draws on pygame screen      
    #==========================================================================
    def draw(self, x):
        
        self.head(x)
        self.eye()
        
        self.mouth(x)
        
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

        pygame.draw.rect(self.generalConfiguration.screen, (255,255,255), (x, y, widthRect, heightRect), 1)
        
        #dessin de l'emoticonne
        #self.draw()    



    #==========================================================================
    # Square for the buttons
    #==========================================================================

    def printSquareButtons(self):
        
        #carre pour l'emoticonne
        widthRect = self.generalConfiguration.screenWidth
        heightRect = self.generalConfiguration.buttonHeight
        x = 0
        y = 0

        pygame.draw.rect(self.generalConfiguration.screen, (255,255,255), (x, y, widthRect, heightRect),1  )



    #==========================================================================
    #Head of the emoticon
    #==========================================================================
    def head(self, coeffCouleur):
        
        #taille de l'emo
        taille_emo = self.generalConfiguration.emoticonSize
        
        #tracage du cercle
        pygame.draw.circle(self.generalConfiguration.screen, self.color(coeffCouleur), self.headToArea([0,0]),taille_emo//2)
        
        #centre du cercle
        pygame.draw.circle(self.generalConfiguration.screen, (255,255,255), self.headToArea([0,0]),1)

    #==========================================================================
    #Eyes of the emoticon
    #==========================================================================
    def eye(self):
        
        #size of the emo
        size=self.generalConfiguration.emoticonSize
        self.setEmoticonParameters(size)
        
        #coord left :
        
        #coord
        coordL = self.headToArea(self.eyeLeftPosition)
        
        #center
        coordL[0] -= self.eyeWidth / 2
        coordL[1] -= self.eyeHeight
        
        #add W and H
        coordL.append(self.eyeWidth)
        coordL.append(self.eyeHeight)
        
        
        #coord right :
        
        #coord
        coordR = self.headToArea(self.eyeRightPosition)
        
        #center
        coordR[0] -= self.eyeWidth / 2 #=> wrong beacause coord left
        coordR[1] -= self.eyeHeight
        
        #add W and H
        coordR.append(self.eyeWidth)
        coordR.append(self.eyeHeight)
        
        #draw left eye
        pygame.draw.ellipse(self.generalConfiguration.screen, [0,0,0], coordL)

        #draw right eye
        pygame.draw.ellipse(self.generalConfiguration.screen, [0,0,0], coordR)


    def mouth(self, x):
        
        coordCentre = self.headToArea(self.mouthPosition)
        coordArc = self.headToArea(self.mouthPosition)
        coordLine = self.headToArea(self.mouthPosition)
        
        
        heightMouth = abs(x) * self.mouthMaxHeight
        
        #center
        coordArc[0] -= self.mouthMaxWidth / 2
        
        #add W and H
        coordArc.append(self.mouthMaxWidth)
        coordArc.append(heightMouth)
        
        
        #coord if line
        coordLine[0] -= self.mouthMaxWidth / 2

        
        cMouth1 = [coordLine[0], coordLine[1]]
        cMouth2 = [coordLine[0] + self.mouthMaxWidth, coordLine[1]]
        
        #draw mouth
        
        
        
        #if line
        if -.15 < x < .15:
            #print(coordArc[0:2], coordArc[2:4])
            pygame.draw.line(self.generalConfiguration.screen, [0,0,0], cMouth1, cMouth2)
            
        elif -.15 > x :
            
            coordArc[1] = coordCentre[0] + self.mouthMaxHeight
            coordArc[3] = heightMouth
            pygame.draw.arc(self.generalConfiguration.screen, [0,0,0], coordArc, math.pi/10, math.pi - math.pi/10)
        
        
        else:
            
            coordArc[1] = coordCentre[0] - heightMouth + self.mouthMaxHeight
            coordArc[3] = heightMouth
            pygame.draw.arc(self.generalConfiguration.screen, [0,0,0], coordArc, math.pi+math.pi/10, 2 * math.pi - math.pi/10)
        
        
#        print(self.setEmoticonParameters(size).eyeLeftPosition)
#        pygame.draw.ellipse(self.generalConfiguration.screen, [0,0,0], self.headToArea(self.setEmoticonParameters(size).eyeLeftPosition+[self.setEmoticonParameters(size).eyeWidth]+[self.setEmoticonParameters(size).Height]))
#        pygame.draw.ellipse(self.generalConfiguration.screen, [0,0,0], self.headToArea(self.setEmoticonParameters.eyeRightPosition)+[self.eyeWidth]+[self.Height])
      

