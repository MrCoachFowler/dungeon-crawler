import os
import time

#generate board
#add a list of items for each room. We want a list so we can have multiple things in a room
#check it out! You can make lists using many lines. In this case, it helps visualize the board
#The spacing between values was added so the rooms lined up and were easier to look at!
dungeon = [
    [['thing'], ['thing'],  ['thing'],  ['thing'],          ['thing','thing2']],
    [['thing'], ['thing'],  ['thing'],  ['thing'],          ['thing']],
    [['thing'], ['thing'],  ['thing'],  ['thing','thing2'], ['thing']]
]

#create player inventory and location and map variables for showing the user
playerMap = [
    ['__x__', '_____', '_____', '_____', '_____'],
    ['_____', '_____', '_____', '_____', '_____'],
    ['_____', '_____', '_____', '_____', '_____'],
]
plyrInventory=[]
plyrFloor = 0
plyrRoom = 0

#create game loop
gameRunning=True

while gameRunning:

    #make a loop that repeats if the user doesn't give a valid response
    isValidMove = False
    while not isValidMove:
        #clear the console
        os.system('cls')

        #print player map (might want to print one row at a time for better user experience!)
        #your code here...

        #get the room contents (a list of strings) to decide what to print to the user
        roomContents = dungeon[plyrFloor][plyrRoom]

        #print player inventory
        print('Your inventory: ' + str(plyrInventory))

        #describe room to user (understand the format to customize this!
        if 'thing' in roomContents:
            print('Well done, you found a thing!')
            seenStartMessage = True
        if 'thing2' in roomContents:
            print("Wowie!! a thing2? No wayz")
       

        
        #get an input from the user
        ##your code here

        #print help menu
        #an example:
        # if playerMove == 'h' or playerMove == 'help':
        #     print('l: go to the room on the left')
        #     print('r: go to the room on the right')
        #     print('up: go to the next floor')
        #     print('dwn: go to the previous floor')
        #     print('a: attack')
        #     print('g: grab an item')
        #     print('use: use an item')

        #move left
        #check if they can move left (is there a room on the left? is there a monster stopping them?)
        #update the player map (reset the current room before adding the x to the next) example:
        # playerMap[plyrFloor][plyrRoom] =  '_____'
        # plyrRoom -= 1
        # playerMap[plyrFloor][plyrRoom] =  '__x__'

        #move right

        #move up

        #move down

        #grab item
        #check if there is an item in the room to grab
        if 'item' in roomContents:
            #make sure there isn't a monster in the way
            if not 'monster' in roomContents
        #add item to inventory
        #remove item from room

        #attack
        #make sure there's a monster in the room
        #make sure they have the proper item to attack
        #remove monster from the room
        #remove item used from inventory

        #use an item
        #verify there is something to use the item on
        #update the room and player inventory appropriately

        #pause between rounds for dramatic effect
        time.sleep(2)

#handle player win/loss