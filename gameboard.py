import random

class Gameboard():

    def __init__(self):
        self.rooms = []

    class Monster:
            def __init__(self, health, intelligence, dexterity, strength):
                self.health = health
                self.intelligence = intelligence
                self.dexterity = dexterity
                self.strength = strength

    class Room():

        def __init__(self, gold_in_room, is_searched, pos):
            self.gold_in_room = gold_in_room
            self.is_searched = is_searched
            #Chat GPT Quoted //
            self.monster = None
            #//
            self.player = None
            self.pos = pos
           

        
    def addRoom(self, room):
        self.rooms.append(room)














