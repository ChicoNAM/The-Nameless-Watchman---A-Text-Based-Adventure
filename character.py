class Character:
    def __init__(self, name: str, health: int, attack: int, defense: int) -> None:
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

class Player(Character):
    def __init__(self, name: str, health: int, attack: int, defense: int, sanity: int, awareness: int, reason: int) -> None:
        super().__init__(name, health, attack, defense)
        self.sanity = sanity
        self.awareness = awareness
        self.reason = reason
        
    def p_attack(self,target):
        
        flag = True
        
        if self.health < 1:
            flag = False
        
        while flag == True:
            print('')
            print(f'You fire at the {target.name}.')
                
            if (self.attack - target.defense) <= 0:
                target.health = target.health - 1
            else:
                target.health = target.health - (self.attack - target.defense)

            if target.health >= 1:
                print(f'The {target.name} has been shot. You have wounded your enemy. {target.name} has {target.health} health left.')
            else:
                target.health = 0
                print(f'{target.name} died.')
                input('>>> ')
                break
            flag = False
                
        
class Enemy(Character):
    def __init__(self, name: str, health: int, attack: int, defense: int) -> None:
        super().__init__(name, health, attack, defense)
        
    def e_attack(self,target):
        
        flag = True
        
        if self.health < 1:
            flag = False
        
        while flag == True:

            if (self.attack - target.defense) <= 0:
                target.health = target.health - 1
            else:
                target.health = target.health - (self.attack - target.defense)
                    
            if target.health >= 1:
                print(f'The {self.name} is attacking. You have been hit. You have {target.health} health left.')
            else: 
                target.health = 0
                print(f'You have been mortally wounded. Your life flashes before your eyes.\n')
                input('>>> ')
                break
            
            flag = False