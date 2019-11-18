# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""

import http
import urllib
import ssl

class Sensor:
    # Constructor
    def __init__(self, url, label, thresholds):
        self.url = url
        self.label = label 
        self.thresholds = thresholds
    
    # Setters
    def setGeneralConfiguration(self, generalConfiguration):
        self.generalConfiguration = generalConfiguration
    
    # Getters
    def getGeneralConfiguration(self):
        return self.generalConfiguration       

    def getLabel(self):
        return self.label
                     
    # Checks if the connection to the sensor is set
    def isConnectedToUrl(self):        
        try:
            self.request = urllib.request.urlopen(url=self.url, context=ssl.create_default_context(ssl.Purpose.CLIENT_AUTH))
        except OSError:
            return False
        else: 
            return self.request.getcode() == http.HTTPStatus.OK

    # Reads the sensor
    def read(self):
        if self.isConnectedToUrl():
            return self.request.read().decode('utf-8')
        else:
            return None
            
    # Gets the transformed value
    def getTransformedValue(self):
        
        #Temperature value
        temp = self.read()
        seuils = self.thresholds
        
        #if inf to seuil min
        if float(temp) <= seuils[0]:
            return -1

        #if equal to center seuil
        if float(temp) == seuils[1]:
            return 0
                
        #if sup to seuil max
        if float(temp) >= seuils[2]:
            return 1



        #if sup to center  
        if float(temp) > seuils[1]:
            return .5 * temp - 11

        #if inf to center
        if float(temp) <  seuils[1]:
            return temp - 22
        



sensor = Sensor('https://www.polytech.univ-smb.fr/apps/myreader/capteur.php?capteur=epua_b204_clim', "Clim B204", [20, 22, 23])
print(sensor.read())
print(sensor.getLabel())
print(sensor.getTransformedValue())







