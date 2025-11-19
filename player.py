class Player:
    def __init__(self, health, intelligence, dexterity, gold, strength, pos):
        self.health = health
        self.intelligence = intelligence
        self.dexterity = dexterity
        self.gold = gold
        self.strength = strength
        self.pos = pos
        
    def player_info(self):
        return (f"Player Health: {self.health} \nPlayer Gold: {self.gold} \nPlayer Strength: {self.strength} \nPlayer Intelligence: {self.intelligence} \nPlayer Dexterity {self.dexterity}")