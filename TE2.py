#!/usr/bin/env python
# coding=utf-8
# Furry Text Escape 2 main script
gamevers = ('v1.0')
n = ('null')

tprint1 = ('1')
tprint2 = ('1')

while n.strip()!="4":
	if tprint1==('1'):
		t = open('./art/title1.TCR', 'r')
		tcr_contents = t.read()
		print (chr(27) + "[2J" + chr(27) + "[H" + tcr_contents)
		t.close()
		tprint1=('0')
		
		print (
		'''Furry Text Escape II
(c) 2015-2016 Thomas Leathers
'''
		)
		print (
		'''Choose number:
1: Watch Intro
2: begin game
3: Credits
4: quit'''
		)
	
	n = raw_input('choose number from the list above:')
	print(chr(27) + "[2A")
	if n=="2":
		#episode selection submenu
		print(chr(27) + "[2J" + chr(27) + "[H")
		episodeselection = ('null')
		tprint2 = ('1')
		t = open('./art/EPSEL-BANNER.TCR', 'r')
		tcr_contents = t.read()
		print (chr(27) + "[2J" + chr(27) + "[H" + tcr_contents + '''"which way?"
''')
		
		while episodeselection.strip()!="5":
			if tprint2==('1'):
				print(chr(27) + "[2J" + chr(27) + "[H")
				episodeselection = ('null')
				tprint2 = ('1')
				t = open('./art/EPSEL-BANNER.TCR', 'r')
				tcr_contents = t.read()
				print (chr(27) + "[2J" + chr(27) + "[H" + tcr_contents + '''"which way?"''')
				t.close()
				tprint2 = ('0')
				print (
				'''episode selection:
1: episode 1 -intro sequence only-
 : episode 2 -coming soon-
 : episode 3 -coming soon-
4: BONUS! Playable flashback to Furry Text Escape 1!
5: return to main menu.'''
				)
			
			episodeselection = raw_input('choice:')
			print(chr(27) + "[2A")
			if episodeselection=="1":
				print(chr(27) + "[2J" + chr(27) + "[H")
				execfile("EP1-intro.py")
				print(chr(27) + "[2J" + chr(27) + "[H")
				tprint2 = ('1')
			if episodeselection=="4":
				print(chr(27) + "[2J" + chr(27) + "[H")
				execfile("DARKROOM.py")
				print(chr(27) + "[2J" + chr(27) + "[H")
				tprint2 = ('1')
		print(chr(27) + "[2J" + chr(27) + "[H")
		tprint1 = ('1')
	
	if n=="1":
		print(chr(27) + "[2J" + chr(27) + "[H")
		execfile("CINA1-OPEN.py")
		print(chr(27) + "[2J" + chr(27) + "[H")
		tprint1 = ('1')
	if n=="3":
		print(chr(27) + "[2J" + chr(27) + "[H")
		execfile("CREDITS.py")
		print(chr(27) + "[2J" + chr(27) + "[H")
		tprint1 = ('1')
	
t.close()
#



