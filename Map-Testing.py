#making maps here

class maps(object): #To compile all the variables the program uses to display maps.
    def __init__(self, name, data, map_height, map_length, left, right, up, down, leave, character_place):
        self.name = name
        self.data = data
        self.map_height = map_height
        self.map_length = map_length
        self.left = left
        self.right = right
        self.up = up
        self.down = down
        self.leave = leave
        self.character_place = character_place

# Special Characters for map design [ ‾ 

#Three Test maps to test moving from one room to another seamlessly.
bedroom1 = [
    " "," "," "," "," "," "," "," "," "," ","\n",
    " "," ","_","|"," ","|","_","_","_"," ","\n",
    " "," ","|"," "," "," "," "," ","|"," ","\n",
    " "," ","|"," "," "," "," "," ","|"," ","\n",
    " "," ","|"," "," "," "," "," ","|","_","\n",
    " "," ","|"," "," "," "," "," "," "," ","\n",
    " "," ","|"," "," "," "," "," ","|","‾","\n",
    " "," ","|"," "," "," "," "," ","|"," ","\n",
    " "," ","|","_","_","_","_","_","|"," ","\n",
    " "," "," "," "," "," "," "," "," "," ","\n",
]
room2 = [
    " ","  "," "," "," "," "," "," "," "," ","\n",
    " "," ","_","_","_","_","_","_","_"," ","\n",
    " "," ","|"," "," "," "," "," ","|"," ","\n",
    " "," ","|"," "," "," "," "," ","|"," ","\n",
    " "," ","|"," "," "," "," "," ","|","_","\n",
    " "," ","|"," "," "," "," "," "," "," ","\n",
    " "," ","|"," "," "," "," "," ","|","‾","\n",
    " "," ","|"," "," "," "," "," ","|"," ","\n",
    " "," ","|","_","_"," ","_","_","|"," ","\n",
    " "," "," "," ","|"," ","|"," "," "," ","\n",
]
LivingRoom = [
    " "," "," "," "," "," "," "," "," "," ","\n",
    " "," "," "," "," "," "," "," "," "," ","\n",
    " "," ","_","_","_","_","_","_","_"," ","\n",
    " "," ","|"," "," "," "," "," ","|"," ","\n",
    " "," ","|"," "," "," "," "," ","|"," ","\n",
    " ","_","|"," "," "," "," "," ","|"," ","\n",
    " "," "," "," "," "," "," "," ","|"," ","\n",
    " ","‾","|"," "," "," "," "," ","|"," ","\n",
    " "," ","|"," "," "," "," "," ","|"," ","\n",
    " "," ","|"," "," "," "," "," ","|"," ","\n",
    " "," ","|"," "," "," "," "," ","|"," ","\n",
    " "," ","|"," "," "," "," "," ","|"," ","\n",
    " ","_","|"," "," "," "," "," ","|"," ","\n",
    " "," "," "," "," "," "," "," ","|"," ","\n",
    " ","‾","|"," "," "," "," "," ","|"," ","\n",
    " "," ","|"," "," "," "," "," ","|"," ","\n",
    " "," ","|","_","_","_","_","_","|"," ","\n",
    " "," "," "," "," "," "," "," "," "," ","\n",
    " "," "," "," "," "," "," "," "," "," ","\n",
]
hold = ["@"]

uproom2 = [25, 27, 28, 29]#Next several lines are what control boundaries such as walls for each room
downroom2 = [80, 81, 83, 84]
leftroom2 = [25, 36, 47, 58, 69, 80]
rightroom2 = [29, 40, 51, 73, 84]
leaveroom2 = [104, 64]
leftbedroom1 = [25, 36, 47, 58, 69, 80]
rightbedroom1 = [29, 40, 51, 73, 84]
upbedroom1 = [25, 27, 28, 29]
downbedroom1 = [80, 81, 82, 83, 84]
leavebedroom1 = [15, 64]
upLivingRoom = [40, 39, 38, 37, 36]
downLivingRoom = [172, 171, 170, 169, 168]
leftLivingRoom = [58, 47, 36, 80, 91, 102, 113, 124, 135, 157, 168]
rightLivingRoom = [172, 161, 150, 139, 128, 117, 106, 95, 84, 73, 62, 51, 40]
leaveLivingRoom = [144, 67]
character_place = 58
game = "YES"
curentmap = ""

room2map = maps("Room 2", room2, 10, 11, leftroom2, rightroom2, uproom2, downroom2, leaveroom2, 58)
bedroom1map = maps("Bedroom 1", bedroom1, 10, 11, leftbedroom1, rightbedroom1, upbedroom1, downbedroom1, leavebedroom1, 26)
LivingRoommap = maps("Living Room", LivingRoom, 19, 11, leftLivingRoom, rightLivingRoom, upLivingRoom, downLivingRoom, leaveLivingRoom, 5)


def mappart(x):#Code to print out each character to make sure they are in a gri pattern
    b = 0
    for items in x:
        print (items, end= ' ')
        if items==len(x):
            print (x[b]) 

def pauseMenu(): #Testing a pause function for game. Should be easy.
    global game_state
    game_state = "Paused"
    while game_state == "Paused":
        print ("Game Paused")
        test2 = input("1. Status")
        if test2.upper() == "E":
            game_state = "Running"
        elif tes2 == "1":
        else:
            pass

def move(x, y): #Function to move and display the map with character on it.
    var = y.pop(x)
    var2 = hold.pop(0)
    hold.append(var)
    y.insert(x, var2)
    mappart(y)

def moveprep(x, y): #The way to prep the lists for inserting the new place of the character
    var = y.pop(x)
    var2 = hold.pop(0)
    hold.append(var)
    y.insert(x, var2)

mapend = "NO" #controls when map ends

def mapcode(x, y, a, b, c, d, e, f, g, h, i):
    move(y, x)
    global mapend
    mapend = "NO"
    while mapend == "NO":
        usermove = input("Use WASD keys to move.\n")
        if usermove.upper() == "W":
            moveprep(y, x)
            if y in e: #Checks to see if the character will be bumping into a wall
                moveprep(y, x)
                print ("You are trying to walk into a wall.")
            elif y in g: #Checks to see if there is an exit
                print ("You leave the area")
                mapend = "YES"
            elif y > 10: #Checks if the map is ending
                y -= 11
                move(y, x)
                print (x.index("@"))
                i.character_place = x.index("@")
            else:
                moveprep(y, x)
                print ("Can no longer move up")
        elif usermove.upper() == "S":
            moveprep(y, x)
            if y in f: #Checks if @ will hit wall. Same for rest of elif usermove.upper()
                moveprep(y, x)
                print ("You are trying to walk into a wall.")
            elif y in g:
                print ("You leave the area")
                mapend = "YES"
            elif y <= ((a*b)-(b-1)):
                y += b
                move(y, x)
                print (x.index("@"))
                i.character_place = x.index("@")
            else:
                moveprep(y, x)
                print ("Can no longer move down")
        elif usermove.upper() == "A":
            moveprep(y, x)
            mapvar = (y - b) % b
            if y in c:
                moveprep(y, x)
                print ("You are trying to walk into a wall.")
            elif y in g:
                print ("You leave the area")
                mapend = "YES"
            elif mapvar != 0:
                y -= 1
                move(y, x)
                print (x.index("@"))
                i.character_place = x.index("@")
            else:
                moveprep(y, x)
                print ("Can no longer move left")
        elif usermove.upper() == "D":
            moveprep(y, x)
            mapvar = (y - (b-2)) % b
            if y in d:
                moveprep(y, x)
                print ("You are trying to walk into a wall.")
            elif y in g:
                print ("You leave the area")
                mapend = "YES"
            elif mapvar != 0:
                y += 1
                move(y, x)
                print (x.index("@"))
                i.character_place = x.index("@")
            else:
                moveprep(y, x)
                print ("Can no longer move right")
        elif usermove.upper() == "E": #How pause function works
            pauseMenu()

def mapcode2(x):#Simplifies mapcode fucntion
    global currentmap
    currentmap = x.name
    mapcode(x.data, x.character_place, x.map_height, x.map_length, x.left, x.right, x.up, x.down, x.leave, x.character_place, x)

def game_loop(): #Game_loop
    global currentmap
    mapcode2(room2map)
    mapend = "NO"
    print (currentmap)
    print (room2map.character_place)
    while game == "YES":
        if (currentmap == bedroom1map.name or currentmap == LivingRoommap.name) and (bedroom1map.character_place == 15 or LivingRoommap.character_place == 67):
            if currentmap == bedroom1map.name:
                bedroom1map.character_place = 0
                room2map.character_place = 93
                mapcode2(room2map)
            elif currentmap == LivingRoommap.name:
                LivingRoommap.character_place = 0
                room2map.character_place = 63
                mapcode2(room2map)
        elif (currentmap == room2map.name or currentmap == bedroom1map.name) and (room2map.character_place == 64 or bedroom1map.character_place == 64):
            if currentmap == room2map.name:
                room2map.character_place = 0
                LivingRoommap.character_place = 68
                mapcode2(LivingRoommap)
            elif currentmap == bedroom1map.name:
                bedroom1map.character_place = 0
                LivingRoommap.character_place = 145
                mapcode2(LivingRoommap)
        elif (currentmap == room2map.name or currentmap == LivingRoommap.name) and (room2map.character_place == 104 or LivingRoommap.character_place == 144):
            if currentmap == room2map.name:
                room2map.character_place = 0
                bedroom1map.character_place = 26
                mapcode2(bedroom1map)
            elif currentmap == LivingRoommap.name:
                LivingRoommap.character_place = 0
                bedroom1map.character_place = 63
                mapcode2(bedroom1map)

game_loop()
