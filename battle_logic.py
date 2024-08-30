from enemy_variations import *
from player_variations import *
from character import *
from story_detective import *

class Battle():
    def __init__(self, player, enemy) -> None:
        self.player = player
        self.enemy = enemy   
        
    #   def player_attack(self,target):
        
        # print(f'You fire at the {target.name}.')
            
        # if (self.attack - target.defense) <= 0:
        #     target.health = target.health - 1
        # else:
        #     target.health = target.health - (self.attack - target.defense)

        # if target.health >= 1:
        #     print(f'The {target.name} has been shot. You have wounded your enemy. {target.name} has {target.health} health left.')
        # else:
        #     print(f'{target.name} died.')
            
    # def enemy_attack(self,target):
    #     print(f'{self.name} is attacking.')

    #     if (self.attack - target.defense) <= 0:
    #         target.health = target.health - 1
    #     else:
    #         target.health = target.health - (self.attack - target.defense)
                
    #     if target.health >= 1:
    #         print(f'The {self.name} is attacking. You have been hit. You have {target.health} health left.')
    #     else: 
    #         print(f'You have been mortally wounded. Your life flashes before your eyes.\n')
    #         print(f'In the end, the searing pain and the sickening crunch of your bones gave way to a torrent of blood that pooled beneath you, \nyour vision fading to black as your lifeless body crumpled onto the blood-soaked cobblestones, the forest devouring the last remnants of your struggle in a gruesome silence.')
    
    def combat(player, enemy):
            
            while player.health >= 1 and enemy.health >= 1:
            
                combat_input = input(f'1. Attack {enemy.name}.\n2. Do nothing.\n>>> ')
            
                if combat_input == '1':
                    player.p_attack(enemy)
                    print('')
                    enemy.e_attack(player)
                    print('')
                elif combat_input == '2':
                    enemy.e_attack(player)
                    print('')
                else:
                    print("You don't have much choice.")
                    print('')
                    combat_input = input(f'1. Attack {enemy.name}.\n2. Do nothing.\n>>> ')
    
    def combat_outcome(player, enemy, outcome_1, outcome_2):
        
        flag = True
        
        while flag == True:
            
            if player.health < 1: 
                print(Story.story_section(outcome_1))
                input('>>> ')
                break
            elif enemy.health < 1:
                print(Story.story_section(outcome_2))
                input('>>> ')
                break
            
            flag == False

