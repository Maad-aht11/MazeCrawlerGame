import MazeCrawlerGame.player as player
import sys
import MazeCrawlerGame.gameboard as gameboard
import random
from colorama import Fore, Style, Back, init

player_pos = 0

def flee(player, gameboard, monster):
    global player_pos
    chanceForFlee = random.randint(7, 15)
    if (chanceForFlee < monster.intelligence):
        print("You failed to escape and were hit by the monster 👿")
        player.health -= int(monster.strength/3)
        print("You got hit by the monster! 💔")
        if (player.health <= 0):
            print("You were killed by the monster.")
            gameboard.rooms[player_pos].player = None
            sys.exit()
    else:
        dirToFlee = ['l', 'r', 'u', 'd']
        old_player_pos = player_pos
        while (old_player_pos == player_pos):
            dirToMove = random.choice(dirToFlee)
            if (dirToMove.lower() == 'l'):
                if (player_pos - 1 < 24 and player_pos - 1 > 0):
                    gameboard.rooms[player_pos-1].player = player
                    gameboard.rooms[player_pos].player = None
                    player_pos -= 1
                    print("YOU FLED LEFT!!")
            if (dirToMove.lower() == 'r'):
                if (player_pos + 1 < 24 and player_pos + 1 > 0):
                    gameboard.rooms[player_pos+1].player = player
                    gameboard.rooms[player_pos].player = None 
                    player_pos += 1
                    print("YOU FLED RIGHT ")
            if (dirToMove.lower() == 'u'):
                if (player_pos - 5 < 24 and player_pos - 5 > 0):
                    gameboard.rooms[player_pos-5].player = player
                    gameboard.rooms[player_pos].player = None
                    player_pos -= 5 
                    print("YOU FLED UP")
            if (dirToMove.lower() == 'd'):
                if (player_pos + 5 < 24 and player_pos + 5 > 0):
                    gameboard.rooms[player_pos-1].player = player
                    gameboard.rooms[player_pos].player = None 
                    player_pos += 5 
                    print("YOU FLED DOWN ")
        print("You fleed to another room!")


def searchForGold(player, gameboard):
    global player_pos
    if (gameboard.rooms[player_pos].monster is not None):
        print("You cannot search for gold, there is a monster in your room")
    elif (gameboard.rooms[player_pos].is_searched == True):
        print("You already searched this room")
    else:
        chanceForGold = random.randint(7, 15)
        if (chanceForGold < player.intelligence):
            print("You found gold! 💰")
            player.gold += gameboard.rooms[player_pos].gold_in_room
            gameboard.rooms[player_pos].is_searched = True
        else:
            print("You didn't find any gold in this room")



#Create a monster
def createMonster():
    monst_intel = random.randint(5, 10)
    monst_dex = random.randint(5, 10)
    monst_stren = random.randint(5, 10)
    monster = gameboard.Monster(health=20, intelligence=monst_intel, dexterity=monst_dex, strength=monst_stren)
    return monster

def fight(gameboard, player, monster):
    global player_pos
    if (gameboard.rooms[player_pos].monster is not None):
        chanceToHit = random.randint(7, 12)
        if (chanceToHit > monster.dexterity):
            monster.health -= int(player.strength/3)
            print("You hit the monster! 💥")
            if (monster.health <= 0):
                print("You killed the monster")
                gameboard.rooms[player_pos].monster = None
        else:
            player.health -= int(monster.strength/3)
            print("You got hit by the monster! 💔")
            if (player.health <= 0):
                print("You were killed by the monster.")
                gameboard.rooms[player_pos].player = None
                sys.exit()
    else:
        print("There is no monster to fight !")


def sleep(gameboard, player):
    if (gameboard.rooms[player_pos].monster is not None):
        print("You may not rest now, there are monsters nearby")
    else:
        chance_for_monster = random.random()
        if chance_for_monster <= 0.8:
            print("You had a restful sleep 💤")
            player.health = 20
        else:
            gameboard.rooms[player_pos].monster = createMonster()
            print("Oh no, a monster spawned while you were sleeping! 👾")

    pass


def checkMonstInRoom(gameboard):
    global player_pos
    if gameboard.rooms[player_pos].monster is not None:
        print("You can't do that, there is a monster in your room.")
        return True
    else:
        return False
    
def printGameInfo(gameboard, player):
    global player_pos
    print("********************************")
    counter = 0
    for  j in range(5):
        for i in range(5):
            if (player_pos == counter):
                print(f"{"@":5}", end = "")
            else:
                print(f"{"-":5}", end="")
            counter += 1
        print()
    print("********************************")
    print()
    print(Fore.RED+f"Player Health: {player.health} ❤️")
    print(Style.RESET_ALL, end="")
    print(f"Player Gold: {player.gold} 🪙")
    print(f"Player Strength: {player.strength} 💪")
    print(f"Player Intelligence: {player.intelligence} 📚")
    print(f"Player Dexterity: {player.dexterity} ✋")
    print()

    if (gameboard.rooms[player_pos].monster is not None):
        print("There is a monster in your room! 👾")
        print(Fore.RED+f"Monster Health {gameboard.rooms[player_pos].monster.health} ❤️")
        print(Style.RESET_ALL, end="")
        print(f"Monster Strength {gameboard.rooms[player_pos].monster.strength} 💪")
        print(f"Monster Intelligence {gameboard.rooms[player_pos].monster.intelligence} 📚")
        print(f"Monster Dexterity {gameboard.rooms[player_pos].monster.dexterity} ✋")
        print()

    




def move(gameboard, dirToMove, player):
    global player_pos
    monst_in_room = checkMonstInRoom(gameboard)
    if (dirToMove.lower() == 'l'):
        if (monst_in_room == False):
            if (player_pos - 1 < 24 and player_pos - 1 > 0):
                gameboard.rooms[player_pos-1].player = player
                gameboard.rooms[player_pos].player = None
                player_pos -= 1
            else:
                print("You cannot move there")
        else:
            print("There is a monster in your room, you cannot move rooms")
    if (dirToMove.lower() == 'r'):
        if (monst_in_room == False):
            if (player_pos + 1 < 24 and player_pos + 1 > 0):
                gameboard.rooms[player_pos+1].player = player
                gameboard.rooms[player_pos].player = None 
                player_pos += 1
            else:
                print("You cannot move there")
        else:
            print("There is a monster in your room, you cannot move rooms")
    if (dirToMove.lower() == 'u'):
        if (monst_in_room == False):
            if (player_pos - 5 < 24 and player_pos - 5 > 0):
                gameboard.rooms[player_pos-5].player = player
                gameboard.rooms[player_pos].player = None
                player_pos -= 5 
            else:
                print("You cannot move there")
        else:
            print("There is a monster in your room, you cannot move rooms")
    if (dirToMove.lower() == 'd'):
        if (monst_in_room == False):
            if (player_pos + 5 < 24 and player_pos + 5 > 0):
                gameboard.rooms[player_pos-1].player = player
                gameboard.rooms[player_pos].player = None 
                player_pos += 5
            else:
                print("You cannot move there")
        else:
            print("There is a monster in your room, you cannot move rooms")


#Create the player
intel = random.randint(10, 20)
stren = random.randint(10, 20)
dex = random.randint(10, 20)
player = player.Player(health=20, gold = 0, strength = stren, dexterity = dex, intelligence=intel, pos = 0)


#Initalializes gameboard with gold and monsters
gameboard = gameboard.Gameboard()
for i in range(25):
    gold = random.randint(150, 300)
    room = gameboard.Room(gold_in_room=gold, is_searched=False, pos= i)
    monster_chance = random.random()
    if (monster_chance >= 0.3):
        monster = createMonster()
        room.monster = monster
    gameboard.addRoom(room)

#Initalize the player to the first room
gameboard.rooms[0].player = player






print("Hello and welcome to Maze Crawler")
print("Here is the maze, the @ indicates where your player is ")
printGameInfo(gameboard, player)

print("Directions:")
print("Enter 'l' to move left")
print("Enter 'r' to move right")
print("Enter 'u' to move up")
print("Enter 'd' to move down")
print("Enter 'f' to fight")
print("Enter 's' to sleep")
print("Enter 'z' to flee")
print("Enter 'g' to look for gold")
while (player.gold <= 800):
    player_input = input("What is your move? ")
    if (player_input.lower() == 'l' or player_input.lower() == 'r' or player_input == 'u' or player_input == 'd'):
        move(gameboard=gameboard, dirToMove=player_input.lower(), player = player)
        printGameInfo(gameboard=gameboard, player=player)
    elif (player_input.lower() == 'f'):
        fight(gameboard, player, gameboard.rooms[player_pos].monster)
        printGameInfo(gameboard=gameboard, player=player)
    elif (player_input.lower() == 's'):
        sleep(gameboard=gameboard, player=player)
        printGameInfo(gameboard=gameboard, player=player)
    elif (player_input.lower() == 'g'):
        searchForGold(player, gameboard)
        printGameInfo(gameboard, player)
    elif (player_input.lower() == 'z'):
        if (gameboard.rooms[player_pos].monster is not None):
            flee(player, gameboard, gameboard.rooms[player_pos].monster)
            printGameInfo(gameboard, player)
        else:
            print("there is no monster to flee from!")
    else:
        print("That is not a valid command!")
print("Congratualtions, you won the game! 🎉")




    







