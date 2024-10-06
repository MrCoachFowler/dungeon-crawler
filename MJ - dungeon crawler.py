#Setup

import os
os.system('cls')

    #Variables

        #Floors/Rooms

floorIntro = [['bed'], ['desk'], ['closet'], ['happy'], ['door downstairs']]
floor1 = [['basement stairs'], ['living room'], ['kitchen'], ['stairs to your room'], ['front door']]
floor2 = [['stairs up'], ['adult drink barrels'], ['food storage'], ['rat den'], ['lower basement stairs']]
floor3 = [['room with your school things'], ['"Room of Forgotten Junk"'], ['second rat den'], ['"Self Protection" stash'], ['stairs back up']]
rooms = [floorIntro , floor1 , floor2 , floor3]

        #Catagorizing Rooms and Other Lists

roomsWithDownStairs = ['door downstairs', 'basement stairs',  'lower basement stairs']
roomsWithUpStairs = ['stairs to your room', 'stairs up', 'stairs back up']
roomsWithWeapons = ['kitchen', 'food storage', 'stairs back up', '"Self Protection" stash', 'room with your school things']
roomsWithEnemies = ['living room', 'rat den', 'second rat den', '"Room of Forgotten Junk"']
grabedRooms = []
weapons = ['Knife', 'Knife', 'Knife', 'Gun', 'Backpack']
enemies = ['your mom', 'a rat', 'another rat', 'a massive cockroach']
inventory = []

        #Player Stuff

game = True
playerAct = ['h', 'q', 'up', 'down', 'l', 'r', 'f', 'g']
playerFloor = 0
playerRoom = 0
currentRoom = rooms[playerFloor][playerRoom]
lastRoom = rooms[playerFloor][playerRoom]

        #Player Actions

canGrab = False
canFight = False
canFight1 = False
canFightBoss = False

        #Map Stuff

map = ['{-=--=-}', '{-=--=-}', '{-=--=-}', '{-=--=-}', '{-=--=-}', '{-=--=-}', '{-=--=-}', '{-=--=-}', '{-=--=-}', '{-=--=-}', '{-=--=-}', '{-=--=-}', '{-=--=-}', '{-=--=-}', '{-=--=-}', '{-=--=-}', '{-=--=-}', '{-=--=-}', '{-=--=-}', ]
emptyRoomImage = '{-=--=-}'
currentRoomImage = '{-=-x-=-}'

    #Fight Function

def fight():
    if len(roomsWithEnemies) > 0:
        print('You were able to if off,')
        roomsWithEnemies.remove(roomsWithEnemies[0])
        enemies.remove(enemies[0])
        if 'Knife' in inventory:
            print('But your knife broke.')
            inventory.remove('Knife')
        if 'Gun' in inventory and 'Knife' not in inventory:
            print('Your gun still has more ammo.')
    else:
        print('You fight nothing and win.')





#Intro

print()


print('''    ▒▒▒▒▒▒▒▒▒▒▒▒▒██████████████████████▒▒▒▒▒▒▒▒▒▒    
    ▒▒▒▒▒▒▒▒▒▒▒██████████████████████████▒▒▒▒▒▒▒▒▒▒    
    ▒▒▒▒▒▒▒▒▒▒▒████▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓████▒▒▒▒▒▒▒▒▒▒    
    ▒▒▒▒▒▒▒▒▒▒▒██████████████████████████▒▒▒▒▒▒▒▒▒▒    
    ▒▒▒▒▒▒▒▒▒▒████████████████████████████▒▒▒▒▒▒▒▒▒    
    ▒▒▒▒▒▒▒▒▒▒███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████▒▒▒▒▒▒▒▒▒    
    ▒▒▒▒▒▒▒▒▒███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████▒▒▒▒▒▒▒▒    
    ▒▒▒▒▒▒▒▒████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███▒▒▒▒▒▒▒▒    
    ▒▒▒▒▒▒▒▒███████████████████████████████▒▒▒▒▒▒▒▒    
    ▒▒▒▒▒▒▒▒███████████████████████████████▒▒▒▒▒▒▒▒    
    ▒▒▒▒▒▒▒▒███████████████████████████████▒▒▒▒▒▒▒▒    
    ▒▒▒▒▒▒▒▒███▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒███▒▒▒▒▒▒▒▒
      You wake up in your bed.                     ''')
input('Enter to continue')
os.system('cls')
print('''▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒██▓▓▒▒▒▒▒▒███▓▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓███░░▒▒▒▒▓██████░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒█████▓███▓▒▒▒█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒███████████████████▓▓██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒████████▓▒▓▓▓▓▓███▓░▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▓░░░▓░▒░░░▓▓██▓░▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒░░▓░░░░░▓▒░▓▓██▓██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░▓░░░█▓▒█▓░░▒░▓████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░░░░▒▓█▒░░░▒░▓████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
░░░░░░░░░░░░░░░██░▓▒▒░░░░░░░░▓▒███▓▓░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▓██░░▓░░░░░░▒░░▓██▒▓▒░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▓██░░░░░▓░░░░███▓█▒░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░▓█████▓▓▓█████▓▓░░░░░░░░░░░░░░░░░░░░
      Your alarm is going off.''')
input('''Enter to continue''')
os.system('cls')
print('''            ░░▒░          
          ░▓▓▓▓▒          
          ▒▒▓▒▒▒          
          ░▒▒▒▒░          
      ░░░░▒▒▓▓▒░          
     ░░▒░░▒▒▒▒▒▒▒░░░      
    ░▒▒▒▒▒░░░░░░░░░░      
   ░▒▒▒░        ░▒▒░░    
  ░▒▒▒░            ░▒░    
  ▒▒▒▒░           ░░░░    
   ░▒▒▒▒░          ░▒▒    
    ░░░░░▒▒░        ▒▒░  
         ░▒▒░        ▒▒  
                     ░░  
                     ░▒░  
                     ▒▒
      "Not again" you think to yourself.''')
input('Enter to continue')
os.system('cls')
print('''                        ░ ░  ░             ░█████░ ██▒██░ ░ ░  ░░░░░    ░░░ ░ ░          
                      ░░                █████ ██ █▓ ███ ██▒░██░█████  ░░░ ░            
                       ░                                           █                  
       ░ ░ ░░░         ░           █░    ██████  ██████████ ▒███████                  
       ░░░▒░░░░        ░        ██       ████ █  ██████████ ░███████  ░  ░            
        ░             ░░     ██ ██    █  █ █  █        ░ ██ ▒███████     ░         ░  
        ░             ░░     ██ ██████▓  ██████  ██ ▒██████ ████████     ░            
        ▒             ░░       █░▒█   ▒                           █     ░            
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ ██      █░████  ▒▓             █▓█  █ ░░░ ░░░░░░░░░ ░░░░
░░░░░░░░░  ░░░░     ░ ▒░░░     ▒█      █▓█░ ▒██  ██████████ ░▒░▒   █    ░░░░░░░░░░░░░░░
  ▒░░░░░░░░░      ▒     ▒░░░░░████ █   █   ▓█    ██████████  ███████▒░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█        █  ███▒   █████████▒    ░   █░░░░░░░░░░░░░░░░░░░
                                   █   █                          ▓█     ░            
                               █   ██  █████████████████████████████    ░░░            
                               █   █   █████████████████████████████▓ ▒░░░░░░░░░░░ ░    
                               █████████████████████████████████                      
    ░░                         ██████████████████████████████████                      
                         ░░     ███ ███████████████  ████████████   ░                  
      You missed your bus again.''')
input('Enter to continue')
os.system('cls')

print("""Mom won't be happy.""")
print()
print('You can ask for help at anytime with [h].')
input('Enter to continue')

os.system('cls')



#Game

while game == True:

    #Updating Player Location, Map, and Reseting Variables

    currentRoom = rooms[playerFloor][playerRoom]

    if playerFloor == 0:
        fix = 0
    else:
        fix = 1
    map.insert((rooms[playerFloor].index(currentRoom) + (len(rooms[playerFloor] * playerFloor))) - fix, currentRoomImage)


    cantMoveRight = False
    cantMoveLeft = False
    canGoDown = False
    canGoUp = False
    canGrab = False
    canFight = False


    #Print information to player

    if playerFloor == 0:
        print('    ', map[0], map[1], map[2], map[3], '   Your Room       }')
        print('--------------------------------------------------------    }')
    print('       ', '{-=-}', '{-=-Your Room-=-}', '{-=-}', '       2nd Story      }')
    print(map[4], map[5], map[6], map[7], map[8], 'First Story    }')
    print(map[9], map[10], map[11], map[12], map[13], 'Basement       }')
    print(map[14], map[15], map[16], map[17], map[18], 'Lower Basement }')
    print('')
    print("You are now at the" , str(currentRoom[0]) + '.')

        #Special room cases (Items, enemies, ending)

    if currentRoom[0] in roomsWithWeapons: #Printing items in room
        if currentRoom[0] == '"Self Protection" stash':
            print('You see a', weapons[-2])
        elif currentRoom [0] == 'room with your school things':
            print('You see a', weapons[-1])
        else:
            print('You see a', weapons[0])
        canGrab = True

    if currentRoom[0] in roomsWithEnemies: #Printing enemies in room
        canFight1 = True
        print('You see', enemies[0])
        if lastRoom == rooms[playerFloor][playerRoom - 1]:
                cantMoveRight = True
        elif lastRoom == rooms[playerFloor][playerRoom + 1]:
                cantMoveLeft = True

    if currentRoom[0] == 'front door': #Ending the game
        if 'Backpack' in inventory:
            print('You can go exit the door to the right now that you have your things.')
        else:
            print('You need to get your things before you can leave.')

    print('Inventory:' , inventory)
    print('')

        #Remove player marker from map now that it is printed

    map.remove(currentRoomImage)
    map.insert(rooms[playerFloor].index(currentRoom), emptyRoomImage)


    #Player Turn

    playerMove = input("What would you like to do? ")
    os.system('cls')

    #Consequenses

        #Checking if the player can do certain actions

    if rooms[playerFloor].index(currentRoom) + 2 > len(rooms[playerFloor]): #check if player is able to move right
        cantMoveRight = True
    if rooms[playerFloor].index(currentRoom) - 1 < 0: #check if player is able to move left
        cantMoveLeft = True

    if currentRoom[0] in roomsWithDownStairs: #check is player can go down
        canGoDown = True
    if currentRoom[0] in roomsWithUpStairs: #check if player can go up
        canGoUp = True

    if len(enemies) > 0:
        if 'Knife' in inventory or 'Gun' in inventory and canFight1 == True: #check if player can fight
            canFight = True
            if 'Gun' in inventory:
                canFight = True
                if enemies[0] == 'a massive cockroach': #check is player can fight boss
                    canFightBoss = True


        #Making the actions affect the game
   
    if playerMove == playerAct[0]: #help
        print('''Commands:
    [h] for help
    [q] to quit
    [up] to go up
    [down] to go down
    [l] to go left
    [r] to go right
    [f] to fight
    [g] to grab''' )
        if 'Backpack' in inventory:
              print('You can leave at the front door now that you have your things.')
        else:
            print('You have to go down into the basement and look for your backpack.')
        print()
       
    elif playerMove == playerAct[1]: #exit
        os.system('cls')
        quit()

    elif playerMove == playerAct[2]: #up
        if canGoUp == True:
            playerFloor -= 1
        else:
            print("You can't go Up")

    elif playerMove == playerAct[3]: #down
        if canGoDown == True:
            playerFloor += 1
        else:
            print("You can't go Down")

    elif playerMove == playerAct[4]: #left
        if cantMoveLeft == True:
            print("You can't move Left")
            if canFight == True:
                print('There is a monster in the way')
        else:
            lastRoom = rooms[playerFloor][playerRoom]
            playerRoom -= 1

    elif playerMove == playerAct[5]: #right

        #Checking if the player can finish the game and ending
        if 'Backpack' in inventory and currentRoom[0] == 'front door':
            if 'air' in inventory:
                print("You float to school with the air you grabbed")
            else:
                print('You leave and start the 10 mile trek to school.')
            exit()
       
        #Normal use cases
        elif cantMoveRight == True:
            print("You can't move Right")
            if canFight == True:
                print('There is a monster in the way')
        else:
            lastRoom = rooms[playerFloor][playerRoom]
            playerRoom += 1

    elif playerMove == playerAct[6]: #fight
        if canFightBoss == True:
            fight()
        elif canFight == True:
            fight()
        else:
            if currentRoom[0] not in roomsWithEnemies:
                print('You fight nothing and win.')
            else:
                print("You punch them with your hands, but they doesn't really care.")

    elif playerMove == playerAct[7]: #grab
        if canGrab == True:
            print('you grabed')
            move = []
            move = weapons.pop(roomsWithWeapons.index(currentRoom[0]))
            inventory.append(move)
            grabedRooms.append(roomsWithWeapons.pop(roomsWithWeapons.index(currentRoom[0])))
        else:
            print('You grabbed some air.')
            inventory.append('air')

    else: #unknown
        print('That is not a command, use [h] for help.')

Period 3,
Matthew Jeffrey