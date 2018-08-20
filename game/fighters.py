# -*- coding: utf-8 -*-
'''
This is a fighter class.
Here you can add different opponents with different characteristics.
hp - amount of health
power - strength of hit

TODO:
agility - chance to avoid hit
intuition - a critical hit chance
'''
from random import randint

class Player(object):
    
    def __init__(self, hp, power):
        self.hp = hp
        self.power = power
    
    
class Monster(object):
     
     def __init__(self, hp, power):
        self.hp = hp
        self.power = power
        
     def drop(self):
         chance = randint(0, 10)  
         if chance >= 3:
             print 'He dropped a power elixir!'
             player.h  


class Dysertasenko(object):
     
     def __init__(self, hp, power):
        pass
        
     def drop(self):
         pass   
         
         
class Bablonenko(object):
     
     def __init__(self, hp, power):
        pass
        
     def drop(self):
         pass   
        
class Uncertainty(object):
     
     def __init__(self, hp, power):
        pass
        
     def drop(self):
         pass   
         
         
class WhatFor(object):
     
     def __init__(self, hp, power):
        pass
        
     def drop(self):
         pass   