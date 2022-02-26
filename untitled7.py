# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 09:15:28 2021

@author: omololu
"""
import math as m
class BMI:
    """ Body Mass index of Human"""
    __KILOGRAMS_PER_POUND = 0.45359237
    __METER_PER_INCH = 0.0254
  
    def __init__(self, name, age , weight, height):
        
        self.name = name
        self. age = age
        self.weight = weight
        self.height = height 
        
   
    def getBMI(self):
         BMI = self.weight * self.KILOGRAMS_PER_POUND/((height * self.METER_PER_INCH) * (height * self.METER_PER_INCH))
         return m.round(BMI * 100)/ 100.0
    
    def getStatus(self):
        BMI = self.getBMI(self)
        if BMI < 18.5:
            return "Underweight"
        elif BMI < 25:
            return "Normal"
        elif BMI < 30:
            return "Overweight"
        else:
            return "Obese"
   
    def __str__(self):
        return self.name,self.age, self.weight, self.height
        
         
    
if __name__ == '__main__':
    _try = 5
    while _try != 0:
        if _try < 5:
            try:
                name = str(input("name: "))
                age = int(input("age: "))
                weight = float(input('weight: '))
                height = float(input('height: '))
            
                _try = _try + 1
            except:
                print("sorry wrong data")
        else:
            input("press any key to exit")
            exit()
    print("you have reached your limit")
        
