import random
import os
print("Welcome to room clearing, we have had a spike in zombies recently. You'll need to clear room by room to reach the next floor until you reach the top where your skills will be tested.")
usableInputs = ['r', 's', 'c a', 'r a', 'c', 'd', 'p', 'f', 'l', 'fl']
print("Once you start you will be able either move left, move right, search, check ammo, reload, climb, descend, fire, flash, or pick up items. For moving left or right just say (l) or (r)")
print("You will only be able to move to a new room once you have searched the current room and made sure it is safe.")
print("You'll start with a S12K Shotgun with a ten round mag, one dummy shell just strong enough to take out the zombies. There are two dummy rounds in the starting room for you.")


#random contents in each room
def box1():
    index = random.randint(0, 2)
    if index == 0 or index == 1:
        return 'dummy shell'
    elif index == 2:
        return 'Battery'


def box2():
    index = random.randint(0, 2)
    if index == 0 or index == 1:
        return 'dummy shell'
    elif index == 2:
        return 'Battery'


def box3():
    index = random.randint(0, 2)
    if index == 0 or index == 1:
        return 'dummy shell'
    elif index == 2:
        return 'Battery'


def box4():
    index = random.randint(0, 2)
    if index == 0 or index == 1:
        return 'dummy shell'
    elif index == 2:
        return 'Battery'


def box5():
    index = random.randint(0, 2)
    if index == 0 or index == 1:
        return 'dummy shell'
    elif index == 2:
        return 'Battery'


def box6():
    index = random.randint(0, 2)
    if index == 0 or index == 1:
        return 'dummy shell'
    elif index == 2:
        return 'Battery'


#skeleton of the player
playerInventory = ['S12K']
playerMag = ['dummy shell']


#skeleton of the tower and contents of each room
tower = []
roomOne = ['dummy shell', 'dummy shell']
roomTwo = ['enemy', box1()]
roomThree = ['fake enemy', 'dummy shell']
roomFour = ['keychain', 'dummy shell']
roomFive = ['ladder up', 'enemy']
roomSix = ['ladder down', 'dummy shell']
roomSeven = [box2(), 'fake enemy', 'enemy', 'dummy shell']
roomEight = [box3(), 'enemy', 'dummy shell']
roomNine = ['flashlight', 'enemy', 'dummy shell']
roomTen = ['ladder up', 'enemy', 'fake enemy', 'dummy shell']
roomEleven = ['ladder down', 'dummy shell', 'dummy shell']
roomTwelve = ['enemy', 'dummy shell', 'dummy shell']
roomThirteen = [box4(), 'enemy', 'enemy', 'enemy', 'enemy', 'enemy', 'enemy', 'enemy', 'enemy', 'enemy', 'enemy']
roomFourteen = [box5(), box6(), 'fake enemy']
roomFifteen = ['Skibidi toilet']


#build the tower
tower.append([roomOne, roomTwo, roomThree, roomFour, roomFive])
tower.append([roomSix, roomSeven, roomEight, roomNine, roomTen])
tower.append([roomEleven, roomTwelve, roomThirteen, roomFourteen, roomFifteen])


#game loop setup
finalRoomSearch = False


#player location
rowIndex = 0
collumnIndex = 0
playerPosition = tower[rowIndex][collumnIndex]


#Item status for fininshing the game
flashlightStatus = 'empty'


#Action functions
def reloadAmmo():
    global playerMag, playerInventory
    reloadLoop = 0
    while len(playerMag) < 10:
        if "dummy shell" in playerInventory:
            playerMag.append("dummy shell")
            playerInventory.remove("dummy shell")
            reloadLoop += 1
        else:
            print("Mag +%s" % reloadLoop)
            break
    if reloadLoop == 0:
        print("You have no more ammo in your inventory.")
    elif len(playerMag) == 10:
        print("Your mag is full.")


def useFlashlight():
    global flashlightStatus, playerInventory
    if flashlightStatus == 'empty':
        print("You click the flashlight and nothing happens. You check the flashlight's battery and realize it's dead.")
        if 'Battery' in playerInventory:
            print("You reach into your bag and pull out a battery.")
            playerInventory.remove('Battery')
            flashlightStatus = 'full'
            print("The flashlight is now full.")
    elif flashlightStatus == 'full':
        print("You shine the flashlight into the room for a minute before the battery dies.")
        flashlightStatus = 'empty'


def shootGun():
    global playerMag, playerPosition
    if 'dummy shell' in playerMag:
        playerMag.pop()
        if 'enemy' in playerPosition:
            playerPosition.remove('enemy')
            print("You fire the dummy shell and hear a declaration that the zombie is down.")
        elif 'fake enemy' in playerPosition:
            print("You fire blindly into the room and realize you shot at a shadow...")
        else:
            print("You realize after the gun fires that there is absolutely nothing in the room for you to shoot at...")
    else:
        print("You pull the trigger and listen as you realize you never loaded in new ammo. Use reload.")


def moveRight():
    global collumnIndex, playerPosition, finalRoomSearch
    if collumnIndex < 4 and 'enemy' not in playerPosition:
        collumnIndex += 1
        playerPosition = tower[rowIndex][collumnIndex]
        print(f"You are now in room {collumnIndex + 1} on floor {rowIndex + 1}.")
        if collumnIndex == r'5' and rowIndex == '2':
            if 'flashlight' in playerInventory:
                print("You shine the flashlight into the final room and see ...")
                print("THE SKIBIDI TOILET!!!!")
                print("Quickly you rush forward and flush the last skibidi toilet. You saved the world, congrats.")
                finalRoomSearch = True
            else:
                print("You need to have a way to see into the dark room before you ...")
    elif 'enemy' in playerPosition:
        print("You are blocked by an enemy.")
    else:
        print("You can't move right.")


def moveLeft():
    global collumnIndex, playerPosition
    if collumnIndex > 0:
        collumnIndex -= 1
        playerPosition = tower[rowIndex][collumnIndex]
        print("You are now in room %s." % (collumnIndex + 1))
    else:
        print("You can't move left.")


def climbUp():
    global rowIndex, collumnIndex
    if (collumnIndex == 4 or collumnIndex == 7) and 'ladder up' in playerPosition:
        rowIndex += 1
        collumnIndex = 0
        print(f"You are now on floor {rowIndex} in room {collumnIndex}.")
    else:
        print("You need to be in a room where you can climb up.")


def climbDown():
    global rowIndex, collumnIndex
    if collumnIndex == 0 and 'ladder down' in playerPosition:
        rowIndex -= 1
        collumnIndex = 0
        print("You are now on floor %s." % rowIndex)
    else:
        print("You need to be in a room where you can climb down.")


def searchRoom():
    print("You search the room and find: %s " % playerPosition)
    if 'enemy' in playerPosition:
        print("You look around and see a zombie shambling towards you!")
    elif 'enemy' not in playerPosition:
        print("This room appears safe for now.")


def pickUpItem():
    global playerPosition
    while True:
        print("You look around the room: %s" % playerPosition)
        if not playerPosition:
            print("There's nothing left in the room.")
            break
        itemChoice = input("What would you like to pick up? (type 'stop' to end): ")
        if itemChoice == 'stop':
            print("You decide to stop picking up items.")
            break
        if itemChoice in playerPosition:
            if itemChoice in (box1(), box2(), box3(), box4(), box5(), box6()):
                playerInventory.append(itemChoice)
                playerPosition.remove(itemChoice)
                print("You pick up a %s" % itemChoice)
            elif itemChoice == "flashlight":
                playerInventory.append(itemChoice)
                playerPosition.remove(itemChoice)
                print("You pick up the flashlight, feeling its weight; it feels empty like it's missing its battery.")
                if "Battery" in playerInventory:
                    playerInventory.remove("Battery")
                    flashlightStatus = 'full'
                    print("You unscrew the flashlight and pop in the battery from earlier.")
            elif itemChoice == "dummy shell":
                playerInventory.append(itemChoice)
                playerPosition.remove(itemChoice)
                print("You pick up a %s" % itemChoice)
            elif itemChoice == "battery":
                playerInventory.append(itemChoice)
                playerPosition.remove(itemChoice)
                print("You pick up a %s" % itemChoice)
            elif itemChoice == "keychain":
                playerInventory.append(itemChoice)
                playerPosition.remove(itemChoice)
                print("You reach down and pick up the small keychain")
                print("Flipping it over you see a familiar face ...")
                print("""⢀⡴⠑⡄⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠸⡇⠀⠿⡀⠀⠀⠀⣀⡴⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠑⢄⣠⠾⠁⣀⣄⡈⠙⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⡀⠁⠀⠀⠈⠙⠛⠂⠈⣿⣿⣿⣿⣿⠿⡿⢿⣆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⡾⣁⣀⠀⠴⠂⠙⣗⡀⠀⢻⣿⣿⠭⢤⣴⣦⣤⣹⠀⠀⠀⢀⢴⣶⣆
⠀⠀⢀⣾⣿⣿⣿⣷⣮⣽⣾⣿⣥⣴⣿⣿⡿⢂⠔⢚⡿⢿⣿⣦⣴⣾⠁⠸⣼⡿
⠀⢀⡞⠁⠙⠻⠿⠟⠉⠀⠛⢹⣿⣿⣿⣿⣿⣌⢤⣼⣿⣾⣿⡟⠉⠀⠀⠀⠀⠀
⠀⣾⣷⣶⠇⠀⠀⣤⣄⣀⡀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠉⠈⠉⠀⠀⢦⡈⢻⣿⣿⣿⣶⣶⣶⣶⣤⣽⡹⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠉⠲⣽⡻⢿⣿⣿⣿⣿⣿⣿⣷⣜⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣷⣶⣮⣭⣽⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣀⣀⣈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⠿⠿⠿⠛⠉ """)
            else:
                print("You can't pick that item up.")
        else:
            print("That item is not in the room.")


def fireGun():
    if 'dummy shell' in playerMag:
        playerMag.pop()
        print("Mag -1")
        if 'enemy' in playerPosition:
            playerPosition.remove('enemy')
            print("You shoot an enemy.")
        elif 'fake enemy' in playerPosition:
            print("You realize it's just a shadow on the wall.")
        else:
            print("You shoot blindly into the room.")
    else:
        print("You hear your shotgun's hammer click and nothing happens ... you need to load ammo.")


#Game loop
while not finalRoomSearch:
    action = input("What would you like to do? ").lower()
    os.system('cls')
    if action in usableInputs:
        print("You try to %s" % action)
        if action == 'r':
            moveRight()
        elif action == 's':
            searchRoom()
        elif action == 'c a':
            print(playerMag)
        elif action == 'r a':
            if not reloadAmmo():
                print("You have no more ammo in your inventory")
        elif action == 'c':
            if climbUp():
                print("Climbed")
        elif action == 'd':
            if climbDown():
                print("Descended")
        elif action == 'p':
            pickUpItem()
        elif action == 'f':
            fireGun()
        elif action == 'l':
            moveLeft()
        elif action == 'fl':
            useFlashlight()
        else:
            print("Unavailable action")
    else:
        print("That's an invalid movement. You can use %s" % usableInputs)
        print("r, move right; s, search room; c a, check ammo in mag; r a, reload ammo; c, climb ladder up; d, descend floor; p, enter search/loot loop; f, use flashlight; l, move left; f, flash")




