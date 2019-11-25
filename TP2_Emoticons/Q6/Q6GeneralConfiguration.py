# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: FANTON - MATHIEU
"""

import pygame
from Q6Emoticon import Emoticon
from Q6Button import Button

class GeneralConfiguration:
    
    
    #==========================================================================
    # Constructor
    #==========================================================================    
    
    def __init__(self) :
        self.initPygame()
        
        # Parameters for the screen
        self.screenWidth = 850
        self.screenHeight = 1200 
        
        # Parameters for the emoticons        
        self.emoticonSize = 400
        self.emoticonBorder = 100  
        self.emoticonBorderInMatrix = 3        
        
        # Parameters for the buttons
        self.buttonWidth = 150
        self.buttonHeight = 80
                
        # Sensors list
        self.sensors = []
        
        self.selectedSensor = 0

        
    #==========================================================================
    # Initializes pygame
    #==========================================================================    
    
    def initPygame(self): 
        #Initialization
        pygame.init()
        # Sets the screen size.
        pygame.display.set_mode((850, 1200))    
        # Sets the timer to check event every 200 ms
        pygame.time.set_timer(pygame.USEREVENT, 200)         
        # Gets pygame screen
        self.screen = pygame.display.get_surface()         
        
  
      
    #==========================================================================
    # Getters 
    #==========================================================================    

    def getScreen(self):
        return self.screen

    def getEmoticonSize(self):
        return self.emoticonSize

    def getEmoticonBorder(self):
        return self.emoticonBorder

    def getButtonWidth(self):
        return self.buttonWidth

    def getButtonHeight(self):
        return self.buttonHeight

    
    def getSensors(self):
        return self.sensors
        
    def getSelectedSensor(self):
        return self.selectedSensor
        
    def getScreenParameters(self):
        return self.screenWidth, self.screenHeight
        
    #==========================================================================
    # Adds a sensor 
    #==========================================================================    

    def addSensor(self, sensor):
        sensor.setGeneralConfiguration(self)
        sensor.setSensorId(len(self.sensors))
        sensor.setEmoticon(Emoticon(sensor))
        sensor.setButton(Button(sensor))
        self.sensors.append(sensor)


 
    #==========================================================================
    # Retrieves the sensor id from a posiiion
    #==========================================================================    

    def positionToSensorId(self, position):
        
        for sensor in self.sensors:
            
            positionButton = sensor.button.getPosition()
#            print(str(positionButton))
            
            if positionButton[0] <= position[0] <= positionButton[2] and positionButton[1] <= position[1] <= positionButton[3]:
                
                return sensor.sensorId
        
        return None


    #==========================================================================
    # Checks if the display of a new sensor was requested
    #==========================================================================    

    def checkIfSensorChanged(self, eventPosition):
        
        if self.positionToSensorId(eventPosition) != self.selectedSensor and self.positionToSensorId(eventPosition) != None:
            
            self.selectedSensor = self.positionToSensorId(eventPosition)

            





    #==========================================================================
    # Muximum number of button per line
    #==========================================================================    
    def maxButtonsPerLine(self):
        
        return self.screenWidth // self.buttonWidth


    #==========================================================================
    # Muximum number of button per line
    #==========================================================================    
    def buttonsCountOnLine(self, line):
        
        return list(map(lambda x : x if x > 0 else 0, [len(self.sensors) - self.maxButtonsPerLine() * (line - 1)]))[0]






    
    #==========================================================================
    # Draws on pygame screen   
    #==========================================================================    

    def draw(self):
        
        # Clears the surface
        pygame.display.get_surface().fill([0, 0, 0])

        # Coords of x value for the position of the left corner on x
        buttonWidth = self.buttonWidth
       


        
        self.sensors[self.selectedSensor].drawEmoticon()
        
#        print(len(self.sensors))
        
        posSensor = 0
        valY = 1
        for row in range(len(self.sensors) // self.maxButtonsPerLine() + 1):
            
#            print(str(row))
            
            if len(self.sensors) <= self.maxButtonsPerLine():
                valX = self.screenWidth / 2 - (len(self.sensors) * buttonWidth) / 2 
            else:
                valX = self.screenWidth / 2 - (5 * buttonWidth) / 2
            
            for sensor in self.sensors[ posSensor : posSensor+self.maxButtonsPerLine() ]:
                
                sensor.drawButton(valX, valY)
    
                valX += buttonWidth
            
            valY += self.buttonHeight
            posSensor += self.maxButtonsPerLine()
            
#            print(str(valY))
            
    #==========================================================================
    # Displays
    #==========================================================================    

    def display(self):
        
        # Title for the screen
        pygame.display.set_caption("Mesure de la Température - " + self.sensors[self.selectedSensor].getLabel())
        
        
        # Draws on the screen surface
        self.draw()
        
        # Updates the display and clears new timer events
        pygame.display.flip()
        pygame.event.clear(pygame.USEREVENT)






#
#Question 5.a) 
#Analyser les fichiers fournis dans le dossier Q5. Dans la fonction main() du fichier
#Q5Main.py, on a ajouté un capteur à l’objet generalConfiguration à l’aide de la méthode
#addSensor(). 
#Expliquer le fonctionnement de cette méthode. 
#Que vaut l’attribut sensors de la classe GeneralConfiguration après cet ajout ?
#
#Cette méthode permet d'ajouter un attribut à la classe generalConfiguration, qui est par
#défaut optionnel. Elle permet ainsi de générer les button et emoticon correspondant, avec
#des valeurs correctes.
#
#L'attribut sensors sera alors une liste ayant pour valeur 
#




