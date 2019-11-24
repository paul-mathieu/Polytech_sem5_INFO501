# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: MATHIEU Paul - FANTON Kevin
"""
import pygame
from Q2GeneralConfiguration import GeneralConfiguration
from Q2Emoticon import Emoticon

def main():
    
    
    listeX = [- x / 10 for x in range(10)][::-1] + [x / 10 for x in range(10)] 
#    listeX += listeX[::-1] 
    listeX *= 100
    
    # Creates the general configuration and the sensors
    generalConfiguration = GeneralConfiguration()

    # Creates an emoticon
    emoticon = Emoticon()
    # Injects the general configuration in the emoticon
    emoticon.setGeneralConfiguration(generalConfiguration)
  
    # Infinite loop    
#    while True:
    for x in range(2000):

        # Waits for an event
        event = pygame.event.wait()
 
        if event.type == pygame.QUIT:
            pygame.quit()
            break 
        
        # Draws the emoticon
        elif event.type == pygame.USEREVENT:
            emoticon.draw(listeX[x])
            generalConfiguration.display()
                                  
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Just pass
            pass
                
# Calls the main function
if __name__ == "__main__":
    main()    
    
    

