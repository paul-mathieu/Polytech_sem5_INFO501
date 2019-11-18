# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""

import pygame
from Q1GeneralConfiguration import GeneralConfiguration



largeurEcran = 1500
hauteurEcran = 1000


def main(largeurEcran, hauteurEcran):

    # Creates an instance of the class GeneralConfiguration
    generalConfiguration = GeneralConfiguration(largeurEcran, hauteurEcran)
     
    
    #print({'Largeur' : get_width(generalConfiguration), 'hauteur' : get_height(generalConfiguration)})
    listeX = [- x / 10 for x in range(10)][::-1] + [x / 10 for x in range(10)] 
    listeX *= 100
    
    # Infinite loop    
    for x in range(2000):

        # Waits for an event
        event = pygame.event.wait()
 
        # Checks if the user wants to quit
        if event.type == pygame.QUIT:
            pygame.quit()
            break 
        
        # Display the drawing
        elif event.type == pygame.USEREVENT:
            generalConfiguration.display()
                       
        # Checks if the user has clicked with the mouse               
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Just pass
            pass



def get_width(generalConfiguration):
    return generalConfiguration.largeurEcran
    
def get_height(generalConfiguration):
    return generalConfiguration.hauteurEcran


                
# Calls the main function
if __name__ == "__main__":
    main(largeurEcran, hauteurEcran)
    
    
    


        




