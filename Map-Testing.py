#Code from an old discontinued project that I had a good map system for

bedroom = [
    " "," "," "," "," "," "," "," "," "," ","\n",
    " "," ","_","|"," ","|","_","_","_"," ","\n",
    " "," ","|"," "," "," "," "," ","|"," ","\n",
    " "," ","|"," "," "," "," "," ","|"," ","\n",
    " "," ","|"," "," "," "," "," ","|"," ","\n",
    " "," ","|"," "," "," "," "," ","|"," ","\n",
    " "," ","|"," "," "," "," "," ","|"," ","\n",
    " "," ","|"," "," "," "," "," ","|"," ","\n",
    " "," ","|","_","_","_","_","_","|"," ","\n",
    " "," "," "," "," "," "," "," "," "," ","\n",
] #Sample room
hold = ["@"] #Character

up = [25, 27, 28, 29] #Placement of Walls
down = [80, 81, 82, 83]
left = [25, 36, 47, 58, 69, 80]
right = [29, 40, 51, 62, 73, 84]
leave = [15] #Placement of exit

def mappart(x): #prints off every item in list
    b = 0
    for items in x:
        print (items, end= ' ')
        if items==len(x):
            print (x[b]) 


character_place = 58 #the starting point in the map


def move(x): #How the charcter moves
    var = bedroom.pop(x)
    var2 = hold.pop(0)
    hold.append(var)
    bedroom.insert(x, var2)
    mappart(bedroom)

def moveprep(x): #preps map to have variables adjusted
    var = bedroom.pop(x)
    var2 = hold.pop(0)
    hold.append(var)
    bedroom.insert(x, var2)

mapend = "NO" #controls while loop

move(character_place) #moves character on map and displays it

def mapcode(): #code for map variable manipulation. Allows user to move character. Hope to be interchangeable with many maps
    global mapend
    global character_place
    while mapend == "NO":
        usermove = input("Use WASD keys to move.\n")
        if usermove.upper() == "W":
            moveprep(character_place)
            if character_place in up:
                moveprep(character_place)
                print ("You are trying to walk into a wall.")
            elif character_place in leave:
                print ("You leave the area")
                mapend = "YES"
            elif character_place > 10:
                character_place -= 11
                move(character_place)
                print (bedroom.index("@"))
            else:
                moveprep(character_place)
                print ("Can no longer move up")
        elif usermove.upper() == "S":
            moveprep(character_place)
            if character_place in down:
                moveprep(character_place)
                print ("You are trying to walk into a wall.")
            elif character_place in leave:
                print ("You leave the area")
                mapend = "YES"
            elif character_place < 97:
                character_place += 11
                move(character_place)
                print (bedroom.index("@"))
            else:
                moveprep(character_place)
                print ("Can no longer move down")
        elif usermove.upper() == "A":
            moveprep(character_place)
            mapvar = (character_place - 11) % 11
            if character_place in left:
                moveprep(character_place)
                print ("You are trying to walk into a wall.")
            elif character_place in leave:
                print ("You leave the area")
                mapend = "YES"
            elif mapvar != 0:
                character_place -= 1
                move(character_place)
                print (bedroom.index("@"))
            else:
                moveprep(character_place)
                print ("Can no longer move right")
        elif usermove.upper() == "D":
            moveprep(character_place)
            mapvar = (character_place - 9) % 11
            if character_place in right:
                moveprep(character_place)
                print ("You are trying to walk into a wall.")
            elif character_place in leave:
                print ("You leave the area")
                mapend = "YES"
            elif mapvar != 0:
                character_place += 1
                move(character_place)
                print (bedroom.index("@"))
            else:
                moveprep(character_place)
                print ("Can no longer move left")

mapcode()
