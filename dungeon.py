#Cleo Tang
#261070795


#list of commands here
s0 = "list commands"
s0_1 = "valid commands"
s0_2 = "commands"

s1 = "turn on the switch"
s1_1 = "switch on"

s2 = "examine the bed"
s2_1 = "look at the bed"

s3 = "examine the closet"
s3_1 = "open the closet"

s4 = "examine the pictures"
s4_1 = "look at the pictures"

s5 = "go to the study room"
s5_1 = "enter the study room"

s6 = "examine the desk"
s6_1 = "look at the desk"
s6_2 = "open the drawer"

s7 = "examine the bookshelves"
s7_1 = "open the digital lock"

s8 = "look at the piano"
s8_1 = "examine the piano"


s9 = "open the door"

s11 = "go to the bed room"
s11_1 = "enter the bed room"




def list_commands(position):
    '''(position) -> NoneType
    takes a string of position as input and returns
    a list of commands available to user
    >>>list_commands("bed room")
    turn on the switch
    examine the bed
    examine the pictures
    examine the closet
    go to the study room
    >>>list_commands("study room")
    examine the desk
    examine the bookshelves
    look at the piano
    open the door
    '''
    if position == "bed room":
        print("turn on the switch")
        print("examine the bed")
        print("examine the pictures")
        print("examine the closet")
        print("go to the study room\n")
        
    else:
        print("examine the desk")
        print("examine the bookshelves")
        print("look at the piano")
        print("go to the bed room")
        print("open the door\n")





def open_the_door():
    '''() -> NoneType
    takes no input,returns strings in response to the input
    given by the player.
    >>>open_the_door()
    >leave
    You leave the door and look for the clue to the password.
    >enter the password
    >Enter the password: 1234
    Incorrect, you can choose to either try again or leave.
    >try again
    >Enter the password: follow your heart
    'You successfully escape the room!'
    '''
    position = "study room"
    print("This is a lock you have to enter the right password to open.")
    print("You can either choose to enter the password or leave the door.")
    
    action = input("Enter the password or leave? ").lower()
    
    #ask the player to re-enter if the command is invalid
    while action != "enter the password" and action != "leave":
        action = input("Invalid command, please re-enter: ")
    
    if action == "enter the password":
        correct_password = "follow your heart"
        password = input("Enter the password: ").lower()               
        action = "try again"
        
        while password != correct_password and action == "try again" :
            print("Incorrect,you can choose to either try again or leave.")            
            action = input().lower()
            
            while action != "try again" and action != "enter the password" and action != "leave":
                action = input("Invalid command.Please re-enter: ")
            
            #when input invalid commands go back to the beginning of the loop
            #then ask for a command again
            if action == "try again" or action == "enter the password" :
                password = input("Enter the password: ").lower()
            
            elif action == "leave":  #condition to break the loop
                print("You leave the door and look for the clue to the password.")
                
       
       #if first try password is correct, while loop won't be executed
       #when the player chooses to leave after trying, this line won't be printed
        if password == correct_password:
            print("Congratulations!You successfully escape the room!")
            position = "outside"
    #when the player choose to leave at the first attempt,this line would be printed
    else:
        print("You leave the door and look for the clue to the password.")

    return position





def in_bed_room(position,key):
    '''(str,bool) -> bool
    takes a string of the player's position and a boolean as to
    the availability of key, returns a string that responses to the
    commands provided by the user.
    >>>in_bed_room("bed room",False)
    >switch on
    Lucky! You are now able to see the entire room. It is spacious,but
    with little things set. You see a large bed in the center with a
    closet to the right of it, and on the walls there are pictures
    of a boy looking glorious on different stages. Surprisingly, when
    you look around,there is a door connecting to a study room.
    >examine the bed
    You search through the bed hoping that the key to the room
    would be somewhere on bed. Finally you are luck enough to
    find one yellow key under the pillow.
    >go to study room
    You enter the study room. The first thing come to your view
    is the grand bookshelves.In front of it, is the desk.
    Near the window, is a piano.
    '''
    command = input().lower()
    
    while position == "bed room":

        if command == s0 or command == s0_1 or command == s0_2: #list commands
            list_commands(position)
        elif command == s1 or command == s1_1: #switch on
            print("Great! You are now able to see the entire room. It is spacious,but")
            print("with little things set. You see a large bed in the center with a")
            print("closet to the right of it, and on the walls there are pictures")
            print("of a boy looking glorious on different stages. Surprisingly, when")
            print("you look around,there is a door connecting to a study room.")
            print("Although you can view the whole room in a glance but you cannot find a")
            print("door to the outside.\n")
        elif command == s2 or command == s2_1: #examine the bed
            print("you search through the bed hoping that the key to the room")
            print("would be somewhere on bed. Finally you are luck enough to")
            print("find one yellow key under the pillow.\n")
            key = True #get key to the locked drawer
        elif command == s3 or command == s3_1: #examine the closet
            print("The closet is empty, but there is one conspicuous suken place.")
            print("You suspect that it was caused by someone hit it heavily.\n")
        elif command == s4 or command == s4_1: #examine the pictures
            print("Nothing special found\n")
        elif command == s11 or command == s11_1: #enter bed room
            print("You are already in the bed room!\n")
         
        
        #the door to the outside is in the study room, the player must enter study room to break this loop
        elif command == s5 or command == s5_1:
            print("You enter the study room. The first thing come to your view")
            print("is the grand bookshelves.In front of it, is the desk. Near")
            print("the window, is a piano.While beside the bookshelves, there is")
            print("one thing that you desperate to see -- a door to the outside!")
            position = "study room"
            #loop will end here since the position changes to study room now
        
        #ask for commond after each completion of a command or a invalid command
        if position == "bed room": # enter the study room
            command = input("If you don't know what to do next, refer to the valid commands.\n").lower()
    #There is a key in the bed room, this function will return the result if the player has found the key
    return key





def desk(key):
    '''(bool) -> NoneType
    takes no input and returns a string in response to the player's input.
    >>>desk(True)
    You examine the desk and find a drawer locked.
    >You can choose either to open the drawer or leave: open the drawer
    
    You successfully open the drawer and find a diary inside.
    You are hunted by a hunch to read the diary:
    '6.12
    Dad and Mom want me to participate in the piano competition,
    but I don't want to... It is so stressful.
    7.20
    No one has asked me what I want to do, they only
    tell me what I should do...
    8.8
    I was conquered by this enormous fear of every new day coming...
    I hide in the closet, so that I won't see the sun rising, staying in the dark for ever.
    But then he came in...He broke in and saw me in the closet, snated my fiction book and
    threw it against the closet...I wanted to cry but only found out that I could not...
    12.12
    Christmas is coming! I love Christmas, and my favorite piece is
    'Merry Christmas Mr Lawrence''
    >>>desk(False)
    You examine the desk and find a drawer locked.
    >You can choose either to open the drawer or leave: open the drawer
    
    Oops! You don't have the key, maybe examine other things will find you one!
    >>>desk(True)
    You examine the desk and find a drawer locked.
    You can choose either to open the drawer or leave: opne
    Invalid command, please re-enter: leave

    You leave the desk and turn around to find the clue to how to open the locked drawer    
    '''
    diary = False  #only True when the player found the diary
    
    print("You examine the desk and find a drawer locked.")
    action = input("You can choose either to open the drawer or leave: ").lower()
    
    while action != "open the drawer" and action != "leave":
        action = input("Invalid command, please re-enter: ").lower()
    
    while action == "open the drawer" and not diary:
        if key :
            print()  #print a new line, better to read
            print("You successfully open the drawer and find a diary inside.")
            print("You are hunted by a hunch to read the diary:")
            print("\'6.12\nDad and Mom want me to participate in the piano competition,")
            print("but I don't want to... It is so stressful.")
            print("7.20\nNo one has asked me what I want to do, they only")
            print("tell me what I should do...")
            print("8.8\nI was conquered by this enormous fear of every new day coming... ")
            print("I hide in the closet, so that I won't see the sun rising, staying in the dark for ever.")
            print("But then he came in...He broke in and saw me in the closet, snated my fiction book and")
            print("threw it against the closet...I wanted to cry but only found out that I could not...")
            print("12.12\nChristmas is coming! I love Christmas, and my favorite piece is")
            print("\'Merry Christmas Mr Lawrence\'\'\n")
            diary = True  #condition to cease the loop
        elif not key:
            print("Oops! You don't have the key, maybe examining other things will find you one!")
            action = "none"  #condition to cease the loop
     
    if action == "leave":
        print("You leave the desk and turn around to find the clue to how to open the locked drawer")
        





def bookshelves():
    '''() -> NoneType
    takes no input and prints contents in response to the input
    >>>bookshelves()
    You scout the bookshelves,and get a digital locker.
    >You can choose either enter the password or put down the locker:put down the locker
    You have put down the locker and turn around to find the clue to the password.
    >>>bookshelves()
    You scout the bookshelves,and get a digital locker.
    >You can choose either enter the password or put down the locker:locker
    >Invalid command, please re-enter: enter the password
    >Enter the digital password here: 434732
    Genius!You open the digital locker.Inside is a note.
    It says:
        'What is essential is invisible to the eye.
        To see rightly, the key is to follow your heart.'

    You seems be inspired, 'where this key can take me to?',you think to yourself.
    >>>bookshelves()
    You scout the bookshelves,and get a digital locker.
    >You can choose either enter the password or put down the locker:enter the password
    >Enter the digital password here: 457878
    >Incorrect.You can choose to try again or put down the locker: put down the locker
    You have put down the locker and turn around to find the clue to the password.
    '''
    correct_password = "434732"
    
    print("You scout the bookshelves,and get a digital locker.")
    action = input("You can choose either enter the password or put down the locker:").lower()
    
    #ask the player to re-enter the command if the command is invalid
    while action != "enter the password" and action != "put down the locker":
        action = input("Invalid command, please re-enter: ").lower()
    
    while action == "enter the password" or action == "try again":
        password = input("Enter the digital password here: ")
        if password != correct_password :
            action = input("Incorrect.You can choose to try again or put down the locker: ").lower()
        else:    
            print("Genius!You open the digital locker.Inside is a note.")
            print("It says:")
            print("\t\'What is essential is invisible to the eye.")
            print("\tTo see rightly, the key is to follow your heart.\'\n")
            print("You seems be inspired, \'where this key can take me to?\',you think to yourself.")
            action = "none"  #condition to cease the loop
    
    #if condition ensures that when the password is correct this line won't be printed.
    if action == "put down the locker":        
        print("You have put down the locker and turn around to find the clue to the password.")




def piano():
    '''() -> NoneType
    takes no input and prints the contents in response to the player's input
    >>>piano()
    You walk towards the piano and find a pile of music sheets.
    You can either choose to examine the music sheets or put down the music sheets:
    >ExAmIne the music sheets
    >Which music piece are you looking for? MERRY CHAEKHG
    You flip through and find the piece merry chaekhg but find nothing special on it.
    >You can either choose to find a piece or put down the music sheets: put down the sheets
    You put down the music sheets and try to find some clue somewhere else.
    >>>piano()
    You walk towards the piano and find a pile of music sheets.
    You can either choose to examine the music sheets or put down the music sheets:
    >put down the SHEETS
    You put down the music sheets and try to find some clue somewhere else.
    '''
    look = "examine the music sheets"
    look_1 = "examine the sheets"
    look_2 = "find a piece"
    put_down = "put down the music sheets"
    put_down_1 = "put down the sheets"
    music_sheet = False
    
    print("You walk towards the piano and find a pile of music sheets.")
    
    action = input("You can either choose to examine the music sheets or put down the music sheets:\n").lower()
    
    #ask for re-enter if the command is invalid
    while action != look and action != look_1 and action != look_2 and action != put_down and action != put_down_1:
        action = input("Invalid commands, please re-enter: ").lower()
        
    while (action == look or action == look_1 or action == look_2) and not music_sheet:
        
        piece = input("Which music piece are you looking for?  ").lower()
        
        if piece in "\'merry christmas mr lawrence\'":
            print("You flip through and find the piece \'Merry Christmas Mr Lawrence\'")
            print("Scan through you notice that some notes were marked, luckily you are")
            print("able to read them, which are : 434732")
            print("It looks very like a password for you, now you want to find where you can use this password.")
            print() #print a new line so better to read
            music_sheet = True #condition to cease the loop and for the whole function
        else:
            print("You flip through and find the piece",piece,"but find nothing special on it.")
            action = input("You can either choose to find a piece or put down the music sheets: ").lower()
        
        #ask for re-enter if the action is invalid
        while action != look and action != look_1 and action != look_2 and action != put_down and action != put_down_1:
            action = input("Invalid commands, please re-enter: ").lower()
        
    if action == "put down the music sheets" or action == "put down the sheets":
        print("You put down the music sheets and try to find some clue somewhere else.")





def in_study_room(position,key):
    '''(str,str) -> str
    takes a string of the player's position and the availability of key
    and returns strings that response tousers' input.
    >>>in_study_room("study room",True)
    examine the desk
    You examine the desk and find a drawer locked.
    You can choose either to open the drawer or leave: leave
    You leave the desk and turn around to find the clue to how to open the locked drawer
    If you don't know what to do next, refer to the valid commands.
    go to the bed room
    You enter the bed room.There is a bed, some pictures and a closet.
    >>>in_study_room("study room",False)
    open the door
    This is a lock you have to enter the right password to open.
    You can either choose to enter the password or leave the door.
    Enter the password or leave? enter the password
    Enter the password: follow your heart
    You successfully escape the room!
    >>>in_study_room("study room",False)
    sit down
    If you don't know what to do next, refer to the valid commands.
    '''
    
    command = input().lower()
    
    while position == "study room":
        
        if command == s0 or command == s0_1 or command == s0_2:  #list commands
            list_commands(position)
        elif command == s5 or command == s5_1:
            print("You are already in the study room!")
        elif command == s6 or command == s6_1: #examine the desk
            desk(key)
        elif command == s7: #examine the bookshelves
            bookshelves()
        elif command == s8 or command == s8_1:  #examine the piano
            piano()
        elif command == s9 :  #open the door
            position = open_the_door()  #condition to cease the loop if position == "outside"
        elif command == s11 or command == s11_1:   #enter the bed room
            print("You enter the bed room.There is a bed, some pictures and a closet.")
            position = "bed room"  #condition to cease the loop
        
        #ask for commond after each completion of a command or a invalid command
        if position == "study room": 
            command = input("If you don't know what to do next, refer to the valid commands.\n").lower()
        
            
    return position
        
        




                

def escape_room():
    '''() -> str
    Takes no input and returns a certain content
    according to the input provided by the user
    >>>escape_room()
    You wake up in a dark yet seemly cozy room. After a few
    seconds your eyes adapt to the dark, you are able to
    find something like a switch on the wall.
    What do you do?
    >turn on the switch
    Great! You are now able to see the entire room. It is spacious,but
    with little things set. You see a large bed in the center with a
    closet to the right of it, and on the walls there are pictures
    of a boy looking glorious on different stages. Surprisingly, when
    you look around,there is a door connecting to a study room.
    Although you can view the whole room in a glance but you cannot find a
    door to the outside.
    
    If you don't know what to do next, refer to the valid commands.
    >list commands
    turn on the switch
    examine the bed
    examine the pictures
    examine the closet
    go to the study room

    If you don't know what to do next, refer to the valid commands.
    >examine the bed
    you search through the bed hoping that the key to the room
    would be somewhere on bed. Finally you are luck enough to
    find one yellow key under the pillow.

    If you don't know what to do next, refer to the valid commands.
    >go to the study room
    You enter the study room. The first thing come to your view
    is the grand bookshelves.In front of it, is the desk. Near
    the window, is a piano.While beside the bookshelves, there is
    one thing that you desperate to see -- a door to the outside!
    '''
    
    #discription of the room
    
    print("You wake up in a dark yet seemly cozy room. After a few")
    print("seconds your eyes adapt to the dark, you are able to")
    print("find something like a switch on the wall.")
    print("What do you do?")
    
    position = "bed room"  #the player begins from the bed room
    key = False
    
    while position != "outside":
        if position == "bed room":  #the player may also enter the bed room from the study room
            key = in_bed_room(position,key)
            #once inside the bed room, the only way to get out the loop is to enter the study room
            position = "study room"
        if position == "study room":
            position = in_study_room(position,key)
        
    





