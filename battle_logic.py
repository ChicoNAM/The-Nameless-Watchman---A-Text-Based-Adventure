from enemy_variations import *
from player_variations import *
from character import *
from story_detective import *

class Battle():
    def __init__(self, player, enemy) -> None:
        self.player = player
        self.enemy = enemy   
    
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
                Story.story_section(outcome_1)
                input('>>> ')
                break
            elif enemy.health < 1:
                Story.story_section(outcome_2)
                input('>>> ')
                break
            
            flag == False

