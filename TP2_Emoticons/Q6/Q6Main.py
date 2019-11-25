# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: FANTON - MATHIEU
"""

import pygame
from Q6GeneralConfiguration import GeneralConfiguration
from Q6Sensor import Sensor
             
def main():
 
    # Creates the general configuration and the sensors
    initURL = 'https://www.polytech.univ-smb.fr/apps/myreader/capteur.php?capteur='
    generalConfiguration = GeneralConfiguration()

    generalConfiguration.addSensor(Sensor(initURL + 'epua_b204_clim', 'Temp. Clim B204', [20, 22, 23]))
    generalConfiguration.addSensor(Sensor(initURL + 'epua_b204_coursive', 'Temp. Coursive B204', [20, 22, 23]))
    generalConfiguration.addSensor(Sensor(initURL + 'epua_b204_centre', 'Temp. Centre B204', [20, 22, 23]))
    generalConfiguration.addSensor(Sensor(initURL + 'epua_toiture', 'Temp. Toiture B204', [30, 35, 40]))
    generalConfiguration.addSensor(Sensor(initURL + 'epua_onduleur1_watts', 'Puiss. Onduleur', [10000, 12000, 15000]))
    
    generalConfiguration.addSensor(Sensor(initURL + 'epua_b204_clim', 'Temp. Clim B204', [20, 22, 23]))
    generalConfiguration.addSensor(Sensor(initURL + 'epua_b204_coursive', 'Temp. Coursive B204', [20, 22, 23]))
    generalConfiguration.addSensor(Sensor(initURL + 'epua_b204_centre', 'Temp. Centre B204', [20, 22, 23]))
    generalConfiguration.addSensor(Sensor(initURL + 'epua_toiture', 'Temp. Toiture B204', [30, 35, 40]))

    
#    print(str(generalConfiguration.sensors))


    # Infinite loop    
    while True:

        # Waits for an event
        event = pygame.event.wait()
 
        if event.type == pygame.QUIT:
            pygame.quit()
            break 
        
        # Displays the selected sensor
        elif event.type == pygame.USEREVENT: 
            
            generalConfiguration.draw()
            
            print(str(generalConfiguration.selectedSensor))
            
            generalConfiguration.display()
            
#            print(str(generalConfiguration.positionToSensorId(pygame.mouse.get_pos())))         
#            print(str(generalConfiguration.maxButtonsPerLine()))
#            print(str(generalConfiguration.buttonsCountOnLine(1)))
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            
#            print(generalConfiguration.selectedSensor)
            
            # Checks if the display of a new sensor is required
            generalConfiguration.checkIfSensorChanged(event.pos)
                
# Calls the main function
if __name__ == "__main__":
    main()    