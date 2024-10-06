# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
inventory = []
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def fight () :
    print(inventory)
    help ()
    if inventory.count('Trowel') == 0 :
        print("You don't have a Trowel! You have lost the game. You'll get it next time!")
        keepPlaying[0] = False
        #print(keepPlaying[0])
    else :
        print("You have defeated the monster! Yay!")
        dungeonContents[currentFloor][currentRoom].remove('Monster')
        inventory.remove('Trowel')
        print("This is what's in your inventory now : " , inventory)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def superMonster () :
    print(inventory)
    help ()
    if inventory.count('Magic Brush') == 0 :
        print("You don't have a Magic Brush! You have lost the game. You'll get it next time!")
        keepPlaying[0] = False
        print(keepPlaying[0])
    else :
        print("You have weakened the monster!")
        inventory.remove('Magic Brush')
        print("This is what's in your inventory now : " , inventory)
        if inventory.count('Trowel') == 0 :
            print("You don't have a Trowel! You have lost the game. You'll get it next time!")
            keepPlaying[0] = False
            print(keepPlaying[0])
        else :
            print("You have defeated the monster! YAY!! ")
            dungeonContents[currentFloor][currentRoom].remove('Super Monster')
            inventory.remove('Trowel')
            print("This is what's in your inventory now : " , inventory)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def ultimateMonster () :
    print(inventory)
    help ()
    if inventory.count('SUPER Magic Brush') == 0 :
        print("You don't have a SUPER Magic Brush! You have lost the game. You'll get it next time!")
        keepPlaying[0] = False
        print(keepPlaying[0])
    else :
        print("You have defeated the ULTIMATE MONSTER!! YAY!!!!!!")
        dungeonContents[currentFloor][currentRoom].remove('Super ULTIMATE Monster')
        inventory.remove('SUPER Magic Brush')
        print("This is what's in your inventory now : " , inventory)
        print("WOW!! There's the ULTIMATE SUPER DUPER COOL Chest that's been told of in legends and myths! HOLY COW!!")
        print("It's all yours, Excavater! Thanks for freeing all the other excavaters!")
        (keepPlaying[0]) = False
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def grabIt (thing) :
    if (len(inventory)) == 3 :
        print("Your inventory is full! You cannot pick up the item. :(")
    else :
        inventory.append(thing)
        dungeonContents[currentFloor][currentRoom].remove(thing)
        print("One" , thing , "has been added to your inventory!")
        print("Your inventory now has these items : " , inventory)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def printMap (playerMap) :
    print(playerMap[2])
    print(playerMap[1])
    print(playerMap[0])
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def help () :
    print("Your available commands are :")
    print("'Left', 'right', 'up' and 'down' move you around the map.")
    print("'Grab' lets you pick up an object.")
    print("'Fight' lets you fight a monster.")
    print("'Help' gives you this list!")
    print("You got this!")
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def eggy () :
    print("You found the Triforce of Courage!... Uh.. huh! Maybe just leave that there.")
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def eggi () :
     print("You found a ticket to Wuhu Island!... HEY that's mine!! I hear they have great cave systems.")
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def stairCase () :
    moving = input("There's a staircase! Want to go up or down?")
    playerMap[currentFloor][currentRoom] = '_____'
    if moving == 'up' :
                currentFloor = currentFloor + 1
                print("Up we go!")
    if moving == 'down' :
                currentRoom = currentRoom - 1
                print("Down we go!")
            # move the player exclamation point to the new room
    playerMap[currentFloor][currentRoom] = '__!__'
    printMap(playerMap)
    print("The cuurent floor is" ,  currentFloor)
    print("The current room is " , currentRoom)
        #print(roomMoves[currentFloor][currentRoom])
    legitMove = True
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
playerMap = [
['__!__','_____','_____','_____','_____','_____'],
['_____','_____','_____','_____','_____','_____'],
['_____','_____','_____','_____','_____','_____']
]

dungeonContents = [
[['START'] , ['Trowel'] , ['Magic Brush'] ,
['Monster' , 'Staircase'] , ['Trowel'] , ['Trowel']],

[['Super Monster'] , ['Staircase','Super Monster'] , ['The Triforce of Courage! (WOW!!)'] , ['Trowel'] , 
['Monster'] , ['Magic Brush']],

[['Trowel'] , ['Magic Brush'] , ['Super Monster'] , ['A Ticket to WuHu Island! (HEY that is mine!)'] , 
['SUPER Magic Brush'] , ['Super ULTIMATE Monster','Ending Chest']],
]



possibleCommands = ['left', 'right', 'up', 'down', 'grab', 'fight', 'help']


# this is where the available moves are kept for each room
# this needs to be expanded for every room
# THIS NEEDS TO BE EXPANDED FOR THE REMAINING TWO FLOORS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
roomMoves = [
    [['right'], ['left', 'right'], ['left', 'right'], ['up', 'right', 'left'], ['left']],
    [['right'], ['up','down','left' ,'right'], ['left', 'right'], ['right', 'left'], ['left']],
    [['right'], ['left' ,'right'], ['left', 'right'], ['down','right', 'left'], ['right', 'left']]
    ]
# There's no staircase in that room!! :O
# this is where the player starts, index 1 is floor and index 2 is room imside of the floor list
currentFloor = 0
currentRoom = 0

# print in backwards order so it looks good on the screen
printMap(playerMap)
keepPlaying = [True]
while (keepPlaying[0] == True) :
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    legitCommand = False
    command = input("What is your command? ")
    while (legitCommand == False) :
        if possibleCommands.count (command) == 1 :
            legitCommand = True
        else :
            print("This is not a good command! Try again or try help.")
            break
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    if command == 'help' :
        help ()
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    if command == 'right' or command == 'left' or command == 'up' or command == 'down' :
        legitMove = False
        while (legitMove == False) :
            playerMove = command
            if roomMoves [currentFloor][currentRoom].count (playerMove) == 1 :                                                                                                                               
                print("Here we go!")
                playerMap[currentFloor][currentRoom] = '_____'
                if playerMove == 'right' :
                        currentRoom = currentRoom + 1
                if playerMove == 'left' :
                    currentRoom = currentRoom - 1
                if playerMove == 'up' :
                    currentFloor = currentFloor + 1
                if playerMove == 'down' :
                    currentFloor = currentFloor - 1
                    # move the player exclamation point to the new room
                playerMap[currentFloor][currentRoom] = '__!__'
                printMap(playerMap)
                print("The contents of this room are : " , dungeonContents[currentFloor][currentRoom])
                print("The current floor is" ,  currentFloor)
                print("The current room is " , currentRoom)
                #print(roomMoves[currentFloor][currentRoom])
                legitMove = True
            else :
                print("You can't go there.")
                break
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    if command == 'fight' :
            if dungeonContents[currentFloor][currentRoom].count ('Monster') == 1 :
                fight()
            else :
                    #print("You have run back to the previous room! You fradey cat!")
                    #playerMap[currentFloor][currentRoom] = '_____'
                    #currentRoom = currentRoom - 1
                    # move the player exclamation point to the new room
                    #playerMap[currentFloor][currentRoom] = '__!__'
                    #printMap(playerMap)
                if dungeonContents[currentFloor][currentRoom].count ('Super Monster') == 1 : # staircase if for all monsters
                    superMonster()
                else :
                    #print("You have run back to the previous room! You fradey cat!") # if you move back as an action fradey cat!
                    #playerMap[currentFloor][currentRoom] = '_____'
                    #currentRoom = currentRoom - 1
                    # move the player exclamation point to the new room
                    #playerMap[currentFloor][currentRoom] = '__!__'
                    #printMap(playerMap)
                    if dungeonContents[currentFloor][currentRoom].count ('Super ULTIMATE Monster') == 1 :
                        ultimateMonster()
                    else :
                        print("There is no monster to fight here!")
                    #print("You have run back to the previous room! You fradey cat!")
                    #playerMap[currentFloor][currentRoom] = '_____'
                    #currentRoom = currentRoom - 1
                    # move the player exclamation point to the new room
                    #playerMap[currentFloor][currentRoom] = '__!__'
                    #printMap(playerMap)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    if command == 'grab' :
        if dungeonContents[currentFloor][currentRoom].count ('Trowel') == 1 :
            grabIt('Trowel')
        else :
            if dungeonContents[currentFloor][currentRoom].count ('Magic Brush') == 1 :
                grabIt('Magic Brush')
            else :
                if dungeonContents[currentFloor][currentRoom].count ('Weird Thing') == 1 :
                    eggy()
                else :
                    if dungeonContents[currentFloor][currentRoom].count ('another Weird Thing') == 1 :
                        eggi()
                    else :
                        if dungeonContents[currentFloor][currentRoom].count ('SUPER Magic Brush') == 1 :
                            grabIt ('SUPER Magic Brush')
                        else :
                            print("There's nothing to grab here!")
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~   