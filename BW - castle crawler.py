import os
import time
# import colorama

king_name = "Kingstonton Kingley the third"       
playing = "true"
while playing == "true":
    # FLOOR LISTS

    # all floors
    castle = [[], [], [], [], []]
    castle[0] = [[], []] # floor 0, tutorial
    castle[1] = [[], [], []] # floor 1, 
    castle[2] = [[], [], [], []] # floor 2,
    castle[3] = [[], [], [], []] # Floor 3,
    castle[4] = [[]]  # floor 4, the king


    # zero floor
    castle[0][0] = ["Here's the staircase into the castle, c'mon. ", "staircase up" ]
    castle[0][1] = ["There's nothing here, just Mr. Frog. Keep going. ", "nothing"]
    # first floor
    castle[1][0] = ["There's two staircases going up and down out the castle, but don't be a coward, keep going! ", "staircase up", "staircase down"] # where the player starts
    castle[1][1] = ["Theres a dagger in here, what will you do? ", "dagger"]
    castle[1][2] = ["A locked chest, strange. ", "chest"]
    # second floor
    castle[2][0] = ["Just a staircase down, keep going. ", "staircase down"]
    castle[2][1] = ["Oh no, a kinight! What will you do? ", "knight"]
    castle[2][2] = ["An armour room, oh wow. What will you do? ", "armor"]
    castle[2][3] = ["Here's the staircase, go! ", "staircase up"]
    # thrid floor
    castle[3][0] = ["Just a staircase down, keep going. ", "staircase down"]
    castle[3][1] = ["A knight is blocking the next room, what will you do? ", "knight"]
    castle[3][2] = ["There is a mysterious key on the floor, how odd ", "key"]
    castle[3][3] = ["A night is blocking the final staircase, what will you do? ", "knight", "staircase up"]
    # fourth floor
    castle[4][0] = ["The final floor. "]



    map_rooms = [" ", " ", " ", " "]

    tutorial = "on"
    while tutorial == "on":
        
        # BIG TUTORIAL AAAAAA ------------------------
        
        player_name = input("What is your name? ")
        first = input("YOU ARE "  + str(player_name) + " \n" + "YOU NEED TO SLAY THE KING \n" + "YOU WOULD MAKE A MUCH BETTER KING THAN HIM \n" + "(Press enter to continue) ")
        os.system('cls')
        
        # TUTORIAL 1
        grab_stick = "not yet happened"
        while grab_stick != "g":
            grab_stick = input("To slay the king, you need a weapon. \n" + 'You see a perfectly crisp stick right infront of you. \n' + 'Type "g" or "grab" to grab it. ')
            os.system('cls')
            if grab_stick != "g": 
                cont = input('GRAB the stick, do you understand? With "g" ')
                os.system('cls')
        print("Good, now the stick in in your inventory.") #mr_fowler: super helpful message! I'm just worried it won't show because it clears right after...
        os.system('cls')

        # TUTORIAL 2
        frog_attack = "not yet happened"
        while frog_attack != "a":
            frog_attack = input("This is your friend, he is a frog. He will help you learn to fight." + "\n" + 'Type "a" and press ENTER to attack him. ')
            os.system('cls')
            if frog_attack != "a":
                cont = input('ATTACK the frog, do you understand? With "a". And dont worry, hes gonna be fine')
                os.system('cls')
        print("Good! job! \n" + "Your frog friend rolled over onto his back, playing dead. ")
        os.system('cls')

        # TUTORIAL 3
        paper_crown = "not yet happened"
        while paper_crown != "i":
            paper_crown = input("You are almost ready to face the king, but you need a proper crown if you are going to take his throne. \n" + "You already have a little peice of paper in your inventory. \n" +'Type "i" and press ENTER to interact with it. ' )
            os.system('cls')
            if paper_crown != "i":
                cont = input('INTERACT with the paper, do you understand? With "i" ')
                os.system('cls')

        #TUTORIAL 4
        first_move = "not yet happened"
        while first_move != "u":
            first_move = input("Now you are ready to enter the dungeon. \n" + 'To move around, type "u" (up), "d" (down), "f" (forward), or "b" (backwards) then press ENTER depending on the areas you are given. \n' + 'Right now, you can only move up the castle stairs. \n' + 'Type "u" and then press ENTER to move up into the castle. ')
            os.system('cls')
            tutorial = "off"
            if first_move != "u":
                cont = input('MOVE into the castle, do you understand? With "u" ')
                os.system('cls')


    # ACTUAL GAME -----------


    player_inventory = ["stick"]

    player_room = 0
    player_floor = 1
    game = "on"
    while game == "on":
        map_rooms = [" ", " ", " ", " "]
        map_rooms[player_room] = "■"
        
        if player_floor == 3 or player_floor == 2:
            player_map = ("_________________________________________________________________\n"
            "|               |               |               |               |\n"
            "|               |               |               |               |\n"
            "|               |               |               |               |\n"
            "|       " + map_rooms[0] + "        /      " + map_rooms[1] + "        /      " + map_rooms[2] + "        /      " + map_rooms[3] + "       |\n"
            "|               |               |               |               |\n"
            "|               |               |               |               |\n"
            "|_______________|_______________|_______________|_______________|\n")
        elif player_floor == 1:
            player_map = ("_________________________________________________\n" 
            "|               |               |               |\n"
            "|               |               |               |\n"
            "|               |               |               |\n"
            "|       " + map_rooms[0] + "        /      " + map_rooms[1] + "        /      " + map_rooms[2]+ "       |\n"
            "|               |               |               |\n"
            "|               |               |               |\n"
            "|_______________|_______________|_______________|\n")
        elif player_floor == 2:
            player_map = "___           ______          ___\n" 
            "|               |               |\n"
            "\n"
            "\n"
            "         " + map_rooms[0] + "               " + map_rooms[1] + "\n"
            "\n"
            "\n"
            "|__          ___|___          __|\n"
        
    
        
        
        print("Inventory: " + str(player_inventory))
        print(player_map)
        room = castle[player_floor][player_room]
        # print(player_floor, player_room)
        action = input(room[0])
        os.system('cls')
        
        # QUIT
        if action == "q":
            game = "2763"

    # ROOM CHECKS -------------------------------------

        # KNIGHT
        if "knight" in castle[player_floor][player_room]:
            if action == "a" or action == "attack":
                if "dagger" in player_inventory:
                    print("You've slain the knight!! Good job.")
                    time.sleep(1)
                    castle[player_floor][player_room].remove("knight")
                    if "staircase up" in castle[player_floor][player_room]:
                        castle[player_floor][player_room][0] = "Don't let the deceast knight distract you, contunue onwards up the stairs! "
                    elif "staircase down" in castle[player_floor][player_room]: 
                        castle[player_floor][player_room][0] = "Just the leftover armor of the knight and the staircase back down, go on. "
                    else:
                        castle[player_floor][player_room][0] = "Nothing here anymore. "
                else:
                    print("You don't have a weapon!! \nThe knight has slain you, your whole journey has been for naught.. \nYOU DIED.")
                    game = "2763"
            else:
                print("You tried avoiding the knight but that gave them an opportunity to attack you. \nThe knight has slain you, your whole journey has been for naught.. \nYOU DIED.")
                game = "2763"

        # KING
        if player_floor == 4 and player_room == 0:
            boss_fight = input("Are you sure you're ready to face the king? Yes or No. ")
            
            if boss_fight == "Yes" or boss_fight == "yes" or boss_fight == "y":
                boss = "on"
                while boss == "on":
                    # ENDING 1
                    print("You're sure? Alright. \nYou slam the door to the throne room open, infront of you standing the King himself, King " + king_name +", to be precise. \n" + '"I AM HERE TO SLAY YOU! I SHALLL BE THE KING!" You say, reaching into your pocket for your trusty dagger.')
                    if "thermonuclear bomb" in player_inventory:
                        print("The king notices your thermonuclear bomb and stands up from the throne. \n" + '"WOAH THERE, ALRIGHT ALRIGHT!! YOU CAN BE KING!"')
                        crown_taking = "on"
                        while crown_taking == "on":
                            take_the_crown = input("Take the crown.")
                            if take_the_crown == "g" or take_the_crown == "grab" or take_the_crown == "take":
                                print("The crown is now yours!! The king fled, leaving you to claim his spot. \nAhhh, how nice it is to be king. \nTHE END")
                                time.sleep(6)
                                king_name = player_name
                                retry = input("Would you like to play again?")
                                if retry == "Yes" or retry == "yes" or retry == "y":    
                                    crown_taking = "off"
                                    boss = "off"
                                    game = "off"
                                    tutorial = "on"
                                else:
                                    print("So be it.")
                                    playing = "flase"
                                    crown_taking = "off"
                                    boss = "off"
                                    game = "off"
                            else:
                                print("TAKE IT.")
                                time.sleep(6)

                    # ENDING 2
                    else:
                        print("The king stands from his throne proudly, drawing his anchient sword from his sheath. \n" + '"You dare challenge ME?" He asked, pointing the sword towards you.') 
                        if "armor" in player_inventory:
                            print('The king throws his sword straight at your chest, but it bounces off your armour and clatters to the floor. \nYou throw the sword back at him, peircing his heart.')
                            crown_taking = "on"
                            while crown_taking == "on":
                                take_the_crown = input("Take his crown.")
                                if take_the_crown == "g" or take_the_crown == "grab" or take_the_crown == "take":
                                    print("The crown is now yours!! The king has died, leaving you to claim his spot. \nAhhh, how nice it is to be king. \n THE END")
                                    king_name = player_name
                                    time.sleep(6)
                                    retry = input("Would you like to play again?")
                                if retry == "Yes" or retry == "yes" or retry == "y":    
                                    crown_taking = "off"
                                    boss = "off"
                                    game = "off"
                                    tutorial = "on"
                                else:
                                    print("So be it.")
                                    playing = "flase"
                                    crown_taking = "off"
                                    boss = "off"
                                    game = "off"
                    # ENDING 3
                        else:
                            print('The king throws his sword straight at your chest, peircing your heart. \nYou have been defeated, the king keeps his crown- for now. \nTHE END')
                            time.sleep(3)
                            retry = input("Would you like to play again?")
                            if retry == "Yes" or retry == "yes" or retry == "y":    
                                boss = "off"
                                game = "off"
                                tutorial = "on"
                            else:
                                print("So be it.")
                                playing = "flase"
                                game = "off"
                                boss = "off"
                                


            elif boss_fight == "No" or boss_fight == "no" or boss_fight == "n":
                print("Fine, then go back.")
                player_floor = 3
                player_room = 3
            else:
                print("Answer the question.")

        
    # ACTION CHECKS ---------------------------------- 
    
        # FORWARD
        if action == "f" or action == "forward":
            if player_room != len(castle[player_floor]) -1:
                player_room += 1
                if player_room > len(castle[player_floor]) -1:
                    player_floor += 1
                    player_room = 0
                    room = castle[player_floor][player_room]
                room = castle[player_floor][player_room]
            else: 
                print("There is no other door here") 

        # BACKWARDS
        if action == "b" or action == "backwards":
            if player_room != 0:
                player_room -= 1
            else: 
                print("You cant go back any further, be brave and carry on!")
            room = castle[player_floor][player_room]

        # UP 
        if action == "u" or action == "up":
            if "staircase up" in castle[player_floor][player_room]:
                if player_floor == 2 and player_room == 3:
                    player_floor = 3
                    player_room = 0
                elif player_floor == 3 and player_room == 3:
                    player_floor = 4
                    player_room = 0
                else:
                    player_floor += 1  
            else:
                print("Nuh uh you cant do that, there's no stairs")

        # DOWN
        if action == "d" or action == "down":
            if "staircase down" in castle[player_floor][player_room]:
                if player_floor == 3 and player_room == 0:
                    player_floor = 2
                    player_room = 3
                elif player_floor == 4 and player_room == 0:
                    player_floor = 3
                    player_room = 3
                else:
                    player_floor -= 1  
            else:
                print("Nuh uh you cant do that, there's no stairs")

        # GRAB
        if action == "g" or action == "grab" or action == "take" or action == "t":
            if "key" in castle[player_floor][player_room] or "armor" in castle[player_floor][player_room] or "dagger" in castle[player_floor][player_room]:
                new_item = castle[player_floor][player_room].pop(1)  
                player_inventory.append(new_item)
                print(player_inventory)
                if new_item == "armor":
                    print("You grabbed " + new_item + '!')
                    time.sleep(0.5)
                else:
                    print("You grabbed a " + new_item + '!')
                    time.sleep(0.5)
                castle[player_floor][player_room][0] = "Nothing here anymore. "
                
        # INTERACT
        if action == "i" or action == "interact" or action == "use":
            if "chest" in castle[player_floor][player_room]:
                if "key" in player_inventory:
                    print("You opened the chest to reveal a thermonuclear bomb, congradulations!!!")
                    time.sleep(.5)
                    player_inventory.append("thermonuclear bomb")
                    castle[player_floor][player_room][0] = "Just an empty chest now. "
                    castle[player_floor][player_room][1] = "nothing"
                    player_inventory.remove("key")
                else:
                    print("How? With your MIND?? Just keep going. ")
                    time.sleep(.5)
            else:
                print("Interact with what??? Just keep going. ")
                time.sleep(.5)