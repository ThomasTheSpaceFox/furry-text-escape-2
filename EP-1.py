#!/usr/bin/env python
# coding=utf-8
# Episode no: 1
gameitem_REDkeycard = ('0')
gameitem_crowbar = ('0')
gameitem_oldkey = ('0')
d = open('./art/BUN_MINI.TCR', 'r')
bunny_mini = d.read()
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
	nullstuff = raw_input()

v = open('./art/EP1-a.TCR', 'r')
tcr_contents = v.read()

def drax_mane_TCR():
	print (chr(27) + "[2J" + chr(27) + "[H" + tcr_contents)

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
nullstuff = raw_input(bunny_mini + '''room 1 completed! 3 to go! lets get that RED KEYCARD!''')

i.close()
d.close()
v.close()