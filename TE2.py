#!/usr/bin/env python
# coding=utf-8
# Furry Text Escape 2 main script
gamevers = ('v1.0')
n = ('null')
while n.strip()!="3":
	t = open('./art/title1.TCR', 'r')
	tcr_contents = t.read()
	print (chr(27) + "[2J" + chr(27) + "[H" + tcr_contents)
	t.close()
	print (
	'''Furry Text Escape II
(c) 2015-2016 Thomas Leathers
'''
	)
	print (
	'''Choose number:
1: Begin game
2: Credits
3: quit'''
	)
	n = raw_input('choose number from the list above:')
	if n=="1":
		print(chr(27) + "[2J" + chr(27) + "[H")
		execfile("CINA1-OPEN.py")
		print(chr(27) + "[2J" + chr(27) + "[H")
	
	if n=="2":
		print(chr(27) + "[2J" + chr(27) + "[H")
		execfile("CREDITS.py")
		print(chr(27) + "[2J" + chr(27) + "[H")
	
t.close()




