# -*- coding: utf-8 -*-
from random import randint
from Bom import *

class Combat(object):
    
    def __init__(self, Player, Monster):
        self.Player = Player
        self.Monster = Monster
    
    def greeting(self):
        
        print '''
               Your strike:        Your block: 
                  
                head   1      head and chest     5
                chest  2      chest and belly    6
                belly  3      belly and legs     7
                legs   4      head and legs      8
                '''
                
    #ініціюєм стати гравців    
    def start(self):
            
        player_hp = self.Player.hp
        player_power = self.Player.power
        monster_hp = self.Monster.hp
        monster_power = self.Monster.power
               
    #Бій
        while player_hp > 0 and monster_hp > 0:
            print '\n'
            print 'Введи свії хід!'
            move = raw_input('>  ')
            checked_move = self.check_move(move)
            
            dmg = self.evaluate_move(checked_move)
            player_hp -= dmg['player_damage']
            monster_hp -= dmg['monster_damage']
            print 'Залишилося здоровя:', player_hp, 'Здоровя монстра:', monster_hp
            
            
        if player_hp <= 0:
            print 'Ти програла'
            x = Lose()
            x.enter()
        
        else:
            print 'Перемога!'
            self.drop() 
            print '\n'   
        
    #Перевірка правильності вводу
    def check_move(self, move):
        
        self.move = move
        
        #check if move is valid
        while True:
            
            try:
                int(move)
                
            except ValueError:
                print 'Бом! Вводи тільки цифри!'
                move = raw_input('>  ')
                continue
           
            
            if len(move) != 2:
                print 'else Бом! Введи 2 цифри: 1, 2, 3, 4 для удару та 5, 6, 7, 8 для блоку'
                move = raw_input('>  ')
            
            elif (int(move[0]) == 1 or int(move[0]) == 2 or int(move[0]) == 3 or int(move[0]) == 4) \
             and (int(move[1]) == 5 or int(move[1]) == 6 or int(move[1]) == 7 or int(move[1]) == 8):
                return int(move)        
           
            else: 
                print 'else Бом! Введи 2 цифри: 1, 2, 3, 4 для удару та 5, 6, 7, 8 для блоку'
                move = raw_input('>  ')
            
    
    def evaluate_move(self, move):
        
        self.move = move
        
        monster_strike = randint(1, 4)
        monster_block = randint(5, 8) 
        player_strike = int(move / 10)  
        player_block = int(move - (int(move / 10) * 10))
        #player_hp = self.Player.hp
        player_power = self.Player.power
        #monster_hp = self.Monster.hp
        monster_power = self.Monster.power
        player_damage = 0
        monster_damage = 0
        
        
        #monster_hit
        if  monster_strike == 1:
            if player_block == 5 or player_block == 8:
                player_damage = 0
                print 'Ти заблокувала удар'
            else:
                player_damage = monster_power
                print 'Монстр луснув тебе по голові -', player_damage 
        
        elif  monster_strike == 2:
            if player_block == 5 or player_block == 6:
                player_damage = 0
                print 'Ти заблокувала удар'
            else:
                player_damage = monster_power
                print 'Монстр стукнув тебе в груди -', player_damage
       
        elif  monster_strike == 3:
            if player_block == 6 or player_block == 7:
                player_damage = 0
                print 'Ти заблокувала удар'
            else:
                player_damage = monster_power
                print 'Монстр дав тобі по пузу -', player_damage 
                
        elif  monster_strike == 4:
            if player_block == 7 or player_block == 8:
                player_damage = 0
                print 'Ти заблокувала удар'
            else:
                player_damage = monster_power
                print 'Монстр дав тобі по ляжках -', player_damage
       
       #player hit 
        if  player_strike == 1:
            if monster_block == 5 or monster_block == 8:
                monster_damage = 0
            else:
                monster_damage = player_power
                print 'Ти попала по голові -', monster_damage 
        
        elif  player_strike == 2:
            if monster_block == 5 or monster_block == 6:
                monster_damage = 0
            else:
                monster_damage = player_power
                print 'Ти стукнула його в груди -', monster_damage 
                
        elif  player_strike == 3:
            if monster_block == 6 or monster_block == 7:
                monster_damage = 0
            else:
                monster_damage = player_power
                print 'Трісь по пузу -', monster_damage 
                
        elif  player_strike == 4:
            if monster_block == 7 or monster_block == 8:
                monster_damage = 0
            else:
                monster_damage = player_power
                print 'Бах його по ногах -', monster_damage 
            
            
        return {'player_damage' : player_damage, 'monster_damage' : monster_damage}
            
        
    def drop(self):
         chance = randint(0, 10)  
         if chance >= 3:
             print 'З нього випав еліксир сили! Сила +5!'
             self.Player.power += 5  
               
