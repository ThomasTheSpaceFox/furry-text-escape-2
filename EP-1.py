#!/usr/bin/env python
# coding=utf-8
# Episode no: 1
gameitem_REDkeycard = ('0')
gameitem_crowbar = ('0')
gameitem_oldkey = ('0')
gameitem_secpasswd = ('0')
gameitem_filecabkey = ('0')
gameitem_seccomcling = ('0')
gameitem_screwdrivr = ('0')
gameitem_ventcontrlkey = ('0')
gameitem_ventcontrlcling = ('0')
gameitem_seccodebook = ('0')
d = open('./art/BUN_MINI.TCR', 'r')
bunny_mini = d.read()
e = open('./art/FOX_MINI.TCR', 'r')
fox_mini = e.read()
i = open('./art/inv_banner.TCR', 'r')
inv_banner = i.read()

def showhelpscreen():
	print (bunny_mini + 
'''   Hi! mrs. helpbunny here! E:)
    The premise of this escape game is very simple:
interact with objects in the correct order.
Objects are in brackets like this: [tree]
    You would type “tree” to interact with the tree.
Your character is smart, he can figure out what objects to use 
if he has the correct ones.
Foxes are clever like that. E;)

other commands:
besides object names, you can use these other commands too.
[look]: this clears the screen. the image and the room description
will be shown again as well. Neat! E:D
[inventory]: shows the inventory.
''')

def inventory_screen():
	print (chr(27) + "[2J" + chr(27) + "[H" + inv_banner)
	print ('''---Inventory---''')
	if gameitem_REDkeycard==('1'):
		print ('Red Keycard: Yes')
	elif gameitem_REDkeycard==('0'):
		print ('Red Keycard: No.')
	if gameitem_crowbar==('1'):
		print ('crowbar: Yes.')
	elif gameitem_crowbar==('0'):
		print ('???: No.')
	if gameitem_oldkey==('1'):
		print ('old key: Yes.')
	elif gameitem_oldkey==('0'):
		print ('???: No.')
	if gameitem_filecabkey==('1'):
		print ('File Cabinet Key: Yes.')
	elif gameitem_filecabkey==('0'):
		print ('???: No.')
	if gameitem_secpasswd==('1'):
		print ('White Class 3 Security Card: Yes.')
	elif gameitem_secpasswd==('0'):
		print ('???: No.')
	if gameitem_screwdrivr==('1'):
		print ('Screwdriver: Yes.')
	elif gameitem_screwdrivr==('0'):
		print ('???: No.')
	if gameitem_ventcontrlkey==('1'):
		print ('Vent Control Key: Yes.')
	elif gameitem_ventcontrlkey==('0'):
		print ('???: No.')
	if gameitem_seccodebook==('1'):
		print ('Security Code Book: Yes.')
	elif gameitem_seccodebook==('0'):
		print ('???: No.')
	nullstuff = raw_input()

v = open('./art/EP1-a.TCR', 'r')
tcr_contents = v.read()

def drax_mane_TCR():
	print (chr(27) + "[2J" + chr(27) + "[H" + tcr_contents)

hinttextis = ('''We will need to find the key for that door.''')

def showhintscreen():
	print (bunny_mini + hinttextis)


se_1_complete = ('0')
inpt1 = ('null')
manedrdraw = ('1')
while se_1_complete==('0'):
	if manedrdraw==('1'):
		drax_mane_TCR()
		print (bunny_mini + '''Hmm. in here there is: a [workbench], a locked [cabinet], and a [door] 
to the next room.''')
		manedrdraw = ('0')

	inpt1 = raw_input(':')
	#print(chr(27) + "[2A")
	if inpt1==("cabinet"):
		if gameitem_crowbar==('0'):
			print ("the cabinet is locked.")
		if gameitem_crowbar==('1'):
			print ("you break open the cabinet with the crowbar. OLD KEY Found!")
			gameitem_oldkey = ('1')
	if inpt1==("workbench"):
		print ("This is a workbench. Here, are many tools.")
		print ("among them you find a crowbar. CROWBAR Found!")
		gameitem_crowbar = ('1')
	if inpt1==("door"):
		if gameitem_oldkey==('0'):
			print ("The door is locked. It has a old looking keylock.")
		if gameitem_oldkey==('1'):
			print ('you use the old key on the door. The door unlocked!')
			se_1_complete = ('1')
	if inpt1==("look"):
		manedrdraw = ('1')
		
	if inpt1==("inventory"):
		inventory_screen()
		manedrdraw = ('1')
	
	if inpt1==("help"):
		showhelpscreen()
	if inpt1==("hint"):
		showhintscreen()
nullstuff = raw_input(bunny_mini + '''room 1 completed! 3 to go! lets get that RED KEYCARD!''')

hinttextis = ('''That door will not open unless the computer lets it open.''')
v.close()
se_2_complete = ('0')
inpt1 = ('null')
manedrdraw = ('1')
v = open('./art/EP1-b.TCR', 'r')
tcr_contents = v.read()

gameitem_secpasswd = ('0')
gameitem_filecabkey = ('0')
gameitem_seccomcling = ('0')


while se_2_complete==('0'):
	if manedrdraw==('1'):
		drax_mane_TCR()
		print (bunny_mini + '''Ok, so in here we have: a [desk], a filing 
[cabinet], a [door] to the next room,  and a security [computer] ''')
		manedrdraw = ('0')

	inpt1 = raw_input(':')
	#print(chr(27) + "[2A")
	if inpt1==("cabinet"):
		if gameitem_filecabkey==('0'):
			print ("the filing cabinet is locked.")
		if gameitem_filecabkey==('1'):
			print ('''you unlock the filing cabinet with the key, in it you 
find a white security card. SECURITY CARD found!''')
			gameitem_secpasswd = ('1')
	if inpt1==("computer"):
		if gameitem_secpasswd==('0'):
			print ('''The computer has a prompt on it that says:
"insert While class 3 security card to unlock door."''')
		if gameitem_secpasswd==('1'):
			print ('''you insert the security card into the computer. *CLUNK* *ERRK* *BEEP*
a digital voice says: "Access granted. Door to maintenance unlocked."''')
			gameitem_seccomcling = ('1')
	if inpt1==("desk"):
		print ("A desk with various papaers scattered about.")
		print ("Under one of the papers you find a key. FILING CABINET KEY Found!")
		gameitem_filecabkey = ('1')
	if inpt1==("door"):
		if gameitem_seccomcling==('0'):
			print ('''The door won't open. It appears to be locked by the security [computer]''')
		if gameitem_seccomcling==('1'):
			print ('You try the door and it is now unlocked!')
			se_2_complete = ('1')
	if inpt1==("look"):
		manedrdraw = ('1')
		
	if inpt1==("inventory"):
		inventory_screen()
		manedrdraw = ('1')
	
	if inpt1==("help"):
		showhelpscreen()
	if inpt1==("hint"):
		showhintscreen()
nullstuff = raw_input(bunny_mini + '''room 2 completed! 2 to go! maintenance here we come!''')
v.close()

hinttextis = ('''Personally I think we should turn off that vent fan, 
I'd rather not be sliced & diced today.''')
se_3_complete = ('0')
inpt1 = ('null')
manedrdraw = ('1')
v = open('./art/EP1-c.TCR', 'r')
tcr_contents = v.read()

gameitem_screwdrivr = ('0')
gameitem_ventcontrlkey = ('0')
gameitem_ventcontrlcling = ('0')

while se_3_complete==('0'):
	if manedrdraw==('1'):
		drax_mane_TCR()
		print (bunny_mini + '''Well, in here there is another [workbench],
a [toolrack], a [vent] with a spinning fan, and vent control [panel]. ''')
		manedrdraw = ('0')

	inpt1 = raw_input(':')
	#print(chr(27) + "[2A")
	if inpt1==("panel"):
		if gameitem_ventcontrlkey==('0'):
			print ("This panel has a keyslot. and it seems to control that vent fan.")
		if gameitem_ventcontrlkey==('1'):
			print ('''You insert the Key into the panel and Press the "OFF" button.
Sure enough, the vent fan turns off.''')
			gameitem_ventcontrlcling = ('1')
	if inpt1==("toolrack"):
		if gameitem_screwdrivr==('0'):
			print ('''There are many tools on the toolrack,
Though strangely, a key is screwed to it.''')
		if gameitem_screwdrivr==('1'):
			print ('''you use the screwdriver to remove the key. VENT KEY Found!''')
			gameitem_ventcontrlkey = ('1')
	if inpt1==("workbench"):
		print ("A large workbench with a busted light on it.")
		print ("among the parts you find a screwdriver. SCREWDRIVER Found!")
		gameitem_screwdrivr = ('1')
	if inpt1==("vent"):
		if gameitem_ventcontrlcling==('0'):
			print ('''The vent is missing its cover, but it's fan is spinning too fast 
to get through! ''')
		if gameitem_ventcontrlcling==('1'):
			print ('You both climb past the now sitll fan through to the next room.')
			se_3_complete = ('1')
	if inpt1==("look"):
		manedrdraw = ('1')
		
	if inpt1==("inventory"):
		inventory_screen()
		manedrdraw = ('1')
	
	if inpt1==("help"):
		showhelpscreen()
	if inpt1==("hint"):
		showhintscreen()
nullstuff = raw_input(bunny_mini + '''room 3 done! 1 more to go! Lets get that Keycard!''')
v.close()



hinttextis = ('''We need That Red Keycard! its probably in that lockbox.''')
se_4_complete = ('0')
inpt1 = ('null')
manedrdraw = ('1')
v = open('./art/EP1-d.TCR', 'r')
tcr_contents = v.read()

gameitem_REDkeycard = ('0')
gameitem_seccodebook = ('0')
gameitem_seccomclingb = ('0')
print (chr(27) + "[2J" + chr(27) + "[H")
print (bunny_mini + '''Ok Red keycard home stretch here, Just tell me what to do. Ok fox? ''')
nullstuff = raw_input('...')
print (fox_mini + '''Rodger that!''')
nullstuff = raw_input('...')
print (bunny_mini + '''Ok, here we go! ''')
nullstuff = raw_input('...')
while se_4_complete==('0'):
	if manedrdraw==('1'):
		drax_mane_TCR()
		print (bunny_mini + '''OK, in here we have another Security [computer],
a computer controlled [lockbox], a [door] back to the atrium,
and a [bookcase]''')
		manedrdraw = ('0')

	inpt1 = raw_input(':')
	#print(chr(27) + "[2A")
	if inpt1==("computer"):
		if gameitem_seccodebook==('0'):
			print ('''This computer seems to need some security codes before
it will let me unlock that lockbox. ''')
		if gameitem_seccodebook==('1'):
			print ('''I spend a moment entering the security codes
into the computer, while you nom on some cookies.
An audiable click comes from the lockbox.''')
			gameitem_seccomclingb = ('1')
	if inpt1==("lockbox"):
		if gameitem_seccomclingb==('0'):
			print ('''This Lockbox is not going to open unless the computer unlocks it.''')
		if gameitem_seccomclingb==('1'):
			print ('''I open the lockbox and grab the RED Keycard. RED KEYCARD Found!!''')
			gameitem_REDkeycard = ('1')
	if inpt1==("bookcase"):
		print ("A large Bookcase with varous books, binders and notebooks on it.")
		print ("Among them i find a promising security codebook. SECURITY CODEBOOK Found!")
		gameitem_seccodebook = ('1')
	if inpt1==("door"):
		if gameitem_REDkeycard==('0'):
			print ('''This door leads back to the atrium, Though we will need
the RED keycard to use it.''')
		if gameitem_REDkeycard==('1'):
			print ('''I swipe the keycard in the reader, and the door opens, 
leading us back to the atrium.''')
			se_4_complete = ('1')
	if inpt1==("look"):
		manedrdraw = ('1')
		
	if inpt1==("inventory"):
		inventory_screen()
		manedrdraw = ('1')
	
	if inpt1==("help"):
		showhelpscreen()
	if inpt1==("hint"):
		showhintscreen()
nullstuff = raw_input(bunny_mini + '''Finally The Red Keycard! lets get back to the atrium!''')
v.close()

e.close()
i.close()
d.close()
