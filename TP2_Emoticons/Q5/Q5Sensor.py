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
        
    def setEmoticon(self, emoticon):
        self.emoticon = emoticon

    def setButton(self, button):
        self.button = button

    def setSensorId(self, sensorId):
        self.sensorId = sensorId
    
    # Getters
    def getGeneralConfiguration(self):
        return self.generalConfiguration       

    def getSensorId(self):
        return self.sensorId

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
        temp = float(self.read())
        seuils = self.thresholds
                
        #if inf to seuil min
        if temp <= seuils[0]:
            return -1

        #if equal to center seuil
        if temp == seuils[1]:
            return 0
                
        #if sup to seuil max
        if temp >= seuils[2]:
            return 1

        """
        With this 3 equations :
            - y1 = a1 * x1 + b1
            - y2 = a2 * x2 + b2
            - y3 = a3 * x3 + b3
            
        And with :
            - a = (y2-y1) / (x2-x1)
            - b = y1 - a * x1
        """
        
        def calculerAffine(x1,x2,y1,y2):
            a = (y2-y1) / (x2-x1)
            b = y2 - a*x2
            return a, b
        
        #if inf to center
        if temp <  seuils[1]:
            a, b = calculerAffine(x1 = seuils[0], x2 = seuils[1], y1 = -1, y2 = 0)
            return a * temp + b
        
        #if sup to center  
        if temp > seuils[1]:
            a, b = calculerAffine(x1 = seuils[1], x2 = seuils[2], y1 = 0, y2 = 1)
            return a * temp + b


    # Draws the emoticon for this sensor
    def drawEmoticon(self):
        self.emoticon.draw(self.getTransformedValue())

    # Draws the button for this sensor
    def drawButton(self):
        pass
    
    
