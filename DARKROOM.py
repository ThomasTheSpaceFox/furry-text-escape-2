#!/usr/bin/env python
# coding=utf-8
# Episode no: 1
gameitem_toothbrush = ('0')
gameitem_floppydisk = ('0')
d = open('./art/BUN_MINI.TCR', 'r')
bunny_mini = d.read()
e = open('./art/FOX_MINI.TCR', 'r')
fox_mini = e.read()
i = open('./art/inv_banner.TCR', 'r')
inv_banner = i.read()
print (fox_mini + '''*tailswish*, *facepaw*, "How do i get in these situations?"''')
nullstuff = raw_input("...")
print (bunny_mini + '''so you are a male fox? and you are stuck with me in a dark room.''')
nullstuff = raw_input("...")
print (fox_mini + '''Yes. Who are you anyways, bunny?''')
nullstuff = raw_input("...")
print (bunny_mini + '''I'm Mrs. Helpbunny! and I'm here to help!''')
nullstuff = raw_input("...")

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
	if gameitem_floppydisk==('1'):
		print ('Security Floppy Disk: Yes')
	elif gameitem_floppydisk==('0'):
		print ('???: No.')
	if gameitem_toothbrush==('1'):
		print ('Toothbrush: Yes.')
	elif gameitem_toothbrush==('0'):
		print ('???: No.')
	nullstuff = raw_input()

v = open('./art/DARKROOM-REVAMPED.TCR', 'r')
tcr_contents = v.read()

def drax_mane_TCR():
	print (chr(27) + "[2J" + chr(27) + "[H" + tcr_contents)

se_1_complete = ('0')
inpt1 = ('null')
manedrdraw = ('1')
while se_1_complete==('0'):
	if manedrdraw==('1'):
		drax_mane_TCR()
		print (bunny_mini + '''Hmm. in here there is: a [sink], [door], and a [box] 
the door appears to need some kind of disk key, judging by the disk drive.''')
		manedrdraw = ('0')

	inpt1 = raw_input(':')
	#print(chr(27) + "[2A")
	if inpt1==("box"):
		if gameitem_toothbrush==('0'):
			print ("the box is locked. it has an old skeleton key lock.")
		if gameitem_toothbrush==('1'):
			print ("you pick the lock with the toothbrush,")  
			print ("in the box you find a Floppy Disk. SECURITY FLOPPY DISK Found!")
			gameitem_floppydisk = ('1')
	if inpt1==("sink"):
		print ("This is a sink. you see an unopened toothbrush.")
		print ("You take the Toothbrush. TOOTHBRUSH Found!")
		gameitem_toothbrush = ('1')
	if inpt1==("door"):
		if gameitem_floppydisk==('0'):
			print ("The door is locked. it seems to need some kind of disk key.")
		if gameitem_floppydisk==('1'):
			print ('you insert the floppy disk into the drive. The door opens!')
			se_1_complete = ('1')
	if inpt1==("look"):
		manedrdraw = ('1')
		
	if inpt1==("inventory"):
		inventory_screen()
		manedrdraw = ('1')
	
	if inpt1==("help"):
		showhelpscreen()
nullstuff = raw_input(bunny_mini + '''The door opened! You escaped! Congrads! Thanks For Playing!''')
d.close()
e.close()
v.close()
i.close()