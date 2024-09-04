from enemy_variations import *
from player_variations import *
from story_detective import *
from battle_logic import *

# adding a line for the end of paragraphs to not skip text to fast
def press_enter():
    input('>>> ')

# game function to start the story

def game():
    print('Greetings.\n')
    player_input = input('Type "play" to begin, or type "quit" to exit. >>> ')
    
    while player_input != 'play':
        print('Invalid Input')
        player_input = input('Type "play" to begin, or type "quit" to exit. >>> ')
        if player_input == 'quit':
            print('Farewell.')
            exit()
        else:
            continue
            
    Story.story_section(chapter_0_intro)
    press_enter()
            
    Story.story_section(chapter_1_arrival)
    press_enter()
            
    Story.story_section(chapter_1_the_fox_choice)
    press_enter()
    
    # user choice chapter 1 
    
    user_choice = input('1: Investgate the Source \n2: Continue Walking, but Faster\n3: Take a Defensive Position\n>>> ')
    
    while user_choice != '1' or '2' or '3':
        if user_choice == '1':
            Story.story_section(chapter_1_the_fox_choice_1)
            press_enter()
            Story.story_section(chapter_1_cobblestone_path)
            press_enter()
            Story.story_section(chapter_1_cobblestone_path_fight)
            press_enter()
            break
            
        elif user_choice == '2':
            Story.story_section(chapter_1_the_fox_choice_2)
            press_enter()
            Story.story_section(chapter_1_the_fox_choice_2_alternative)
            press_enter()
            break
        
        elif user_choice == '3':
            Story.story_section(chapter_1_the_fox_choice_3)
            press_enter()
            Story.story_section(chapter_1_cobblestone_path)
            press_enter()
            Story.story_section(chapter_1_cobblestone_path_fight)
            press_enter()
            break    
        else:
            print('\nThere is not much time. You have to decide.\n')
            user_choice = input('1: Investigate the Source \n2: Continue Walking, but Faster\n3: Take a Defensive Position\n>>> ')
    
    # battle chapter 1
    
    Battle.combat(player_1, ani_enemy_1)
    
    # battle outcome
    
    Battle.combat_outcome(player_1, ani_enemy_1, chapter_1_cobblestone_path_fight_outcome_failure, chapter_1_cobblestone_path_fight_outcome_success)
    
    print('...to be continued.')
    press_enter()
    
if __name__ == '__main__':
    game()