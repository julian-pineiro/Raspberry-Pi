#Module: HardwareModules
#Contains Hardware Sensors and Module classes.

import time
import RPi.GPIO as GPIO
#import FakeRPi.GPIO as GPIO
import datetime
import Adafruit_DHT as sensor
from abc import ABC, abstractmethod


class Module(ABC):
    @abstractmethod
    def getID(self):
        pass
    @abstractmethod
    def getPort(self):
        pass

class Relay(Module):
    def __init__(self, identity, port):
        self.i = identity
        self.p = port
        self.on = True
        GPIO.setup(port, GPIO.OUT)   
        GPIO.output(port, GPIO.HIGH)

    def switch(self):
        if self.on:
            GPIO.output(self.getPort(), GPIO.LOW)
            self.on=False
        else:
            GPIO.output(self.getPort(), GPIO.HIGH)
            self.on=True

    def getID(self):
        return self.i

    def getPort(self):
        return self.p

    def isOn(self):
        if self.on: return True
        else: return False

    def toString(self):
        print("identity = "+str(self.getID())+
              ", port = "+str(self.getPort())+
              ", is on: "+str(self.isOn()))

        
'''  
--DHT11 Sensor Config--
    Positive: pin 1 
    Ground: pin 6 
    Data: pin 11 
'''
class DHT11(Module):
    #Port in DHT11 stands for the data port.
    def __init__(self, identity, port):
        self.i = identity
        self.p = port
    def read(self):
        #Read_retry Parameters are (model(=11), GPIO data port)
        humidity, temperature = sensor.read_retry(11,self.getPort())
        return [humidity, temperature]
    def getID(self):
        return self.i

    def getPort(self):
        return self.p
      


