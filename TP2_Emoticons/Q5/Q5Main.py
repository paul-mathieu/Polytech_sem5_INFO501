# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""

import pygame
from Q5GeneralConfiguration import GeneralConfiguration
from Q5Sensor import Sensor
             
def main():
    
    
    
#    listeX = [- x / 10 for x in range(10)][::-1] + [x / 10 for x in range(10)] 
#    listeX += listeX[::-1] 
#    listeX *= 100
    
    
    
 
    # Creates the general configuration and the sensors
    initURL = 'https://www.polytech.univ-smb.fr/apps/myreader/capteur.php?capteur='
    generalConfiguration = GeneralConfiguration()

    generalConfiguration.addSensor(Sensor(initURL + 'epua_b204_clim', 'Temp. Clim B204', [20, 22, 23]))
    generalConfiguration.addSensor(Sensor(initURL + 'epua_b204_coursive', 'Temp. Clim B204', [20, 22, 23]))
    generalConfiguration.addSensor(Sensor(initURL + 'epua_b204_centre', 'Temp. Clim B204', [20, 22, 23]))
    generalConfiguration.addSensor(Sensor(initURL + 'epua_toiture', 'Temp. Clim B204', [30, 35, 40]))
    generalConfiguration.addSensor(Sensor(initURL + 'epua_onduleur1_watts', 'Temp. Clim B204', [10000, 12000, 15000]))




    # Infinite loop    
    while True:
#    for x in range(2000):

        # Waits for an event
        event = pygame.event.wait()
 
        if event.type == pygame.QUIT:
            pygame.quit()
            break 
        
        # Displays the selected sensor
        elif event.type == pygame.USEREVENT: 
            
            generalConfiguration.draw()
            
            generalConfiguration.display()
                                  
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Checks if the display of a new sensor is required
            generalConfiguration.checkIfSensorChanged(event.pos)
                
# Calls the main function
if __name__ == "__main__":
    main()    