import time
loop_control = "on"
gender = "N/A"
print ("You wake up in a bed.")
time.sleep(2)
print ("You slowly sit up in the dark room. \nWhen you look around the dark room you can't really make anything out.\nYou slowly get up and make your way through your room and out the door.")
time.sleep(5)
print ("You enter your bathroom and flick on the light.\nYou enter the shower quickly and start up the hot water.\nYou quickly start cleaning off.\nThe steam from the water rises and floats out into the rest of the bathroom.")
time.sleep(5)
print ("When you finish, you step out and  dry off.\nYou step over to the fogged up mirror and begin wiping it off.")
input_var = input("When you look into the mirror, what do you see?\n1. A dashing young man\n2. A beautiful young girl\n==> ")
while loop_control == "on":
    input_var = input("Please Select 1 or 2\n==> ")
    loop_control = "off"
    if input_var == "1":
        gender = "Male"
    elif input_var == "2":
        gender = "Female"
    else:
        loop_control = "on"
loop_control = "on"
if gender == "Male":
    print ("You stare blankly into the mirror, a tired, shaggy haired boy looking back at you.\nYou sigh as you quickly dry the rest of the way off and head back to your room.")
    print ("You flick on the light in your room and you see the fairly messy room stares back at you.\nYou go over to a fairly empty closet and quickly pull out some clothes.")
else:
    print ("You stare blankly into the mirror as a tired, dishevled girl stares back.\nYou sigh as you quickly dry the rest of way off and head back to your room.")
    print ("You flick on the light in your room and see the fairly messy room.\nYou go over to a slightly overflowling closet and try and figure out what to wear today.\nYou find something suitable and get dressed.")
