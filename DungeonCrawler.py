import os
import time

#generate board
dungeon = [[],[],[]]
dungeon[0] = [['start'], ['sword'], ['monster'], ['upstairs'], ['monster','water bucket']] #first floor
dungeon[1] = [['upstairs'], ['monster'], ['sword'], ['downstairs'], ['sword']] #second floor
dungeon[2] = [['downstairs'],['sword'],['monster'],['fire','great sword'],['boss monster']] #third floor

#create player inventory and location variables
playerMap = [['__x__', '_____', '_____', '_____', '_____'],[ '_____', '_____', '_____', '_____', '_____'],[ '_____', '_____', '_____', '_____', '_____']]
plyrInventory=[]
plyrFloor = 0
plyrRoom = 0
previousRoom = -1

#create game loop
gameRunning=True
seenStartMessage=False
while gameRunning:
    isValidMove = False
    while not isValidMove:
        os.system('cls')

        #print player map
        for i in range(1,len(playerMap)+1):
            print(playerMap[len(playerMap) - i])
        roomContents = dungeon[plyrFloor][plyrRoom]

        #print player inventory
        print('Your inventory: ' + str(plyrInventory))

        ##describe room to user
        if 'start' in roomContents and not seenStartMessage:
            print("'It's a good thing you're up', a mouse squealed excitedly from the corner. 'Things have definitely been better'\n'There was a big party at this school last night except the chemistry class got a little.. carried away.\nLong story short, some of the students were accidentally turned into monsters. While they got huge muscles and breath that reminds me of ketchup and broccoli, I somehow got turned into a rat.\nRumor has it, one of the teachers also got turned into a monster and they're guarding the antidote and key to escape on the top floor.\nIf we work together, we might be able to get out of here alive!\n\nIf you ever need help, you can use enter h to see the menu of your options")
            seenStartMessage = True
        if 'sword' in roomContents:
            print("Upon entering the room, you notice an old sword leftover from when the school had a fencing program.")
        if 'monster' in roomContents:
            print("Oh no! It's a hideous monster and they're blocking the path forward")
        if 'water bucket' in roomContents:
            print("A rusty old bucket full of water sits in the corner")
        if 'fire' in roomContents:
            print("The physics class must've really gotten carried away with their voltage lab. The entire room is on fire!")
        if 'great sword' in roomContents:
            print("It is hard to see, but it looks like a very large, shiny sword is sitting in the far corner of the room")
        if 'boss monster' in roomContents:
            print("Holy mama jama! That has got to be the scariest monster of them all. No ordinary sword will work here...")
        if 'upstairs' in roomContents:
            print('A white tile staircase leads upwards in the corner')
        if 'downstairs' in roomContents:
            print('A white tile staircase leads downwards in the corner')

        

        playerMove = input('What would you like to do? ')
        #help menu
        if playerMove == 'h' or playerMove == 'help':
            print('l: go to the room on the left')
            print('r: go to the room on the right')
            print('up: go to the next floor')
            print('dwn: go to the previous floor')
            print('a: attack')
            print('g: grab an item')
            print('use: use an item')

        #move left
        elif playerMove == 'l':
            if plyrRoom == 0:
                print("There is not a door on the left...")
                 
            elif 'monster' in roomContents and previousRoom > plyrRoom:
                print("You are unable to run past the monster...")
                 
            else:
                isValidMove = True
                playerMap[plyrFloor][plyrRoom] =  '_____'
                previousRoom = plyrRoom
                plyrRoom -= 1
                playerMap[plyrFloor][plyrRoom] =  '__x__'
        #move right
        elif playerMove == 'r':
            if plyrRoom == len(dungeon[plyrFloor]) - 1:
                print("There is not a door on the right...")
                 
            elif 'monster' in roomContents and previousRoom < plyrRoom:
                print("You are unable to run past the monster...")
                 
            else:
                isValidMove = True
                previousRoom = plyrRoom
                playerMap[plyrFloor][plyrRoom] =  '_____'
                plyrRoom += 1
                playerMap[plyrFloor][plyrRoom] =  '__x__'

        #move up
        elif playerMove == 'up':
            if not 'upstairs' in roomContents:
                print("There is no stairs going up...")
                 
            else:
                isValidMove = True
                playerMap[plyrFloor][plyrRoom] =  '_____'
                plyrFloor += 1
                playerMap[plyrFloor][plyrRoom] =  '__x__'

        #move down
        elif playerMove == 'dwn':
            if not 'downstairs' in roomContents:
                print("There is no stairs going down...")
            
            else:
                isValidMove = True
                playerMap[plyrFloor][plyrRoom] =  '_____'
                plyrFloor -= 1
                playerMap[plyrFloor][plyrRoom] =  '__x__'

        #grab item
        elif playerMove == 'g':
            if not 'sword' in roomContents and not 'water bucket' in roomContents and not 'great sword' in roomContents:
                print("There is nothing to grab...")
            elif 'monster' in roomContents:
                print("You go to grab the item but the monster steps in to block your way...")
            elif 'fire' in roomContents:
                print("You reach out but the fire strikes at you too quickly")
            else:
                isValidMove = True
                for item in roomContents:
                    if item == 'sword' or item == 'water bucket' or item == 'great sword':
                        print("You received a " + item)
                        plyrInventory.append(item)
                        roomContents.remove(item)

        #attack
        elif playerMove == 'a':
            if not 'monster' in roomContents and not 'boss monster' in roomContents:
                print("There is nothing to attack. You take a practice swing and scrape your arm...")

            elif 'boss monster' in roomContents and not 'great sword' in plyrInventory:
                print("You're going to need one heck of a sword for that!")
                 
            elif not 'boss monster' in roomContents and not 'sword' in plyrInventory:
                print("You try scratching the monster but it doesn't seem to work. If only you had a sword...")
            else:
                isValidMove = True
                if 'monster' in roomContents:
                    print("The monster has been slayed, but the sword broke!")
                    plyrInventory.remove('sword')
                    roomContents.remove('monster')
                else:
                    print("You did it!!")
                    gameRunning = False

        #use an item
        elif playerMove == 'use':
            if not 'fire' in roomContents:
                print("There is a time and place for everything...")
                 
            else:
                isValidMove = True
                print("The fire subsided")
                roomContents.remove('fire')

        else:
            print('Unrecognized action\nTry h or help for a reminder')

        #pause between rounds for dramatic effect
        time.sleep(2)

os.system('cls')
print("You did it! The antidote worked great.\nIt was a little awkward seeing your friends after having fought them with fencing swords, but they forgave you and everyone went for ice cream.")