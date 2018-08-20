# -*- coding: utf-8 -*-
from random import randint
import sys
import time
from combat import *

class Scene(object):
    
    def enter(self):
        pass
      

class Engine(object):
    
    def __init__(self, scene_map):
        self.scene_map = scene_map
    
    ''' 
    simple fight simulator
    '''
    
                    
    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name) 
            
            
class Player(object):
    
    def __init__(self, hp, power):
        self.hp = hp
        self.power = power
    
    
class Monster(object):
     
     def __init__(self, hp, power):
        self.hp = hp
        self.power = power
        
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
            print 'Your turn'
            move = raw_input('>  ')
            checked_move = self.check_move(move)
            
            dmg = self.evaluate_move(checked_move)
            player_hp -= dmg['player_damage']
            monster_hp -= dmg['monster_damage']
            print 'Health left:', player_hp, 'Monster health:', monster_hp
            
            
        if player_hp <= 0:
            print 'You lose!'
            x = Lose()
            x.enter()
        
        else:
            print 'You win!'
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
                print 'Please use numbers only!'
                move = raw_input('>  ')
                continue
           
            
            if len(move) != 2:
                print 'Bom! Please enter two numbers: 1, 2, 3, 4 for strike and 5, 6, 7, 8 for block'
                move = raw_input('>  ')
            
            elif (int(move[0]) == 1 or int(move[0]) == 2 or int(move[0]) == 3 or int(move[0]) == 4) \
             and (int(move[1]) == 5 or int(move[1]) == 6 or int(move[1]) == 7 or int(move[1]) == 8):
                return int(move)        
           
            else: 
                print 'Bom! Please enter two numbers: 1, 2, 3, 4 for strike and 5, 6, 7, 8 for block'
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
                print 'Successful block'
            else:
                player_damage = monster_power
                print 'You get a head punch -', player_damage
        
        elif  monster_strike == 2:
            if player_block == 5 or player_block == 6:
                player_damage = 0
                print 'Successful block'
            else:
                player_damage = monster_power
                print 'Chest hit -', player_damage
       
        elif  monster_strike == 3:
            if player_block == 6 or player_block == 7:
                player_damage = 0
                print 'Successful block'
            else:
                player_damage = monster_power
                print 'Stomach hurts -', player_damage
                
        elif  monster_strike == 4:
            if player_block == 7 or player_block == 8:
                player_damage = 0
                print 'Successful block'
            else:
                player_damage = monster_power
                print 'Legs hit -', player_damage
       
       #player hit 
        if  player_strike == 1:
            if monster_block == 5 or monster_block == 8:
                monster_damage = 0
            else:
                monster_damage = player_power
                print 'You hit his head! -', monster_damage
        
        elif  player_strike == 2:
            if monster_block == 5 or monster_block == 6:
                monster_damage = 0
            else:
                monster_damage = player_power
                print 'Good hit! -', monster_damage
                
        elif  player_strike == 3:
            if monster_block == 6 or monster_block == 7:
                monster_damage = 0
            else:
                monster_damage = player_power
                print 'Got you! -', monster_damage
                
        elif  player_strike == 4:
            if monster_block == 7 or monster_block == 8:
                monster_damage = 0
            else:
                monster_damage = player_power
                print 'Good hit -', monster_damage
            
            
        return {'player_damage' : player_damage, 'monster_damage' : monster_damage}
            
        
    def drop(self):
         chance = randint(0, 10)  
         if chance >= 3:
             print 'You get the power elixir! Power +5!'
             self.Player.power += 5  
        
     
class Entrance(Scene):

     def enter(self):
        print 'You enter a dark and scary room...'
        time.sleep(1)
        print 'Strange sounds...'
        time.sleep(2)
        print 'And here they are... the three riders of Apocalypse'
        time.sleep(2)
        print 'But you are brave and accept the challenge.... '
        time.sleep(2)
        
        
                
        print 'Bamberg attacks first'
        pip_battle = Combat(Bom, Pipunov)
        pip_battle.greeting()
        pip_battle.start()
       
        print 'Then Famine...'
        dysertasenko_battle = Combat(Bom, Dysertasenko)
        dysertasenko_battle.start()
        
        print '... and Pale'
        bablonenko_battle = Combat(Bom, Bablonenko)
        bablonenko_battle.start()
       
        return 'floor'
  
              
class Floor(Scene):

     def enter(self):
        print 'Now you can enter the second floor...'
        time.sleep(1)
        print 'You start to worry...'
        time.sleep(1)
        print 'Can I do that? Am I good enough?'
        time.sleep(1)
        print 'Now you have to fight your own... FEAR!!!'
        time.sleep(1)
        
        fear_battle = Combat(Bom, Fear)
        #fear_battle.greeting()
        fear_battle.start()
        
        print 'Great victory'
        print 'As a reward you get a magic sword'
        print '+15 power, +50 healt /n'
        Bom.hp += 50
        Bom.power += 15
        return 'phdroom'
 
               
class PhDRoom(Scene):

     def enter(self):
        print 'You overcome your fear...'
        time.sleep(1)
        print 'You are so cool))'
        time.sleep(1)
        print 'You are now very close to your goal...'
        time.sleep(1)
        print 'The last big fight ahead...'
        time.sleep(1)
        print 'Here comes your main enemy...'
        time.sleep(1)
        print 'THE LACK OF MOTIVATION!!!!'
        
        WhatFor_battle = Combat(Bom, WhatFor)
        #WhatFor_battle.greeting()
        WhatFor_battle.start()
        
        
        return 'finish'


class Lose(Scene):

     def enter(self):
        print 'You lose'
        print 'What will you do?'
        print 'Fight or surrender????'
        print 'Press R to try again and S to surrender'
        
        
        while True:
            
            choice = raw_input('> ')
        
            if choice == 'R' or choice == 'r':
                a_map = Map('entrance')
                a_game = Engine(a_map)
                a_game.play()
            elif choice == 'S' or choice == 's':
                print 'Everything is gone...'
                sys.exit()
            else:
                print 'Enter R or S'
            
              
class Finish(Scene):
    
    def enter(self):
        print 'Victory!!! You are the champion!!'
        sys.exit()
 


class Map(object):
    '''
    start_scene - приходить при ініціалізації обєкту Мар
    opening_scene - запускає метод next_scene з картою яка прийшла при 
    ініціалізації обєкту
    next_scene повертає класс карти з відповідним іменем
    '''
    
    scenes = {
    'entrance': Entrance(),
    'floor': Floor(),
    'phdroom': PhDRoom(),
    'lose': Lose(),
    'finish': Finish(),
    
    }
    
    def __init__(self, start_scene):
        self.start_scene = start_scene
        
    def next_scene(self, scene_name):
        next = Map.scenes.get(scene_name)
        return next
        
    def opening_scene(self):
        return self.next_scene(self.start_scene)
        
Bom = Player(50, 10)
Pipunov = Monster(40, 7)
Dysertasenko = Monster(45, 9)
Bablonenko = Monster(50, 10)

Fear = Monster(75, 12)

WhatFor = Monster(200, 15)

#Pipunov.drop()
#print 'Player stats:', Bom.hp, Bom.power


   
a_map = Map('entrance')
a_game = Engine(a_map)
a_game.play()      
