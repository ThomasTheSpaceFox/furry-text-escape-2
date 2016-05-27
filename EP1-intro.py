#!/usr/bin/env python
# coding=utf-8
# Episode 1 intro.

f = open('./art/opening1d.TCR', 'r')
tcr_contents = f.read()
def TCR_SHOW1():
	print(chr(27) + "[2J" + chr(27) + "[H" + tcr_contents)

d = open('./art/BUN_MINI.TCR', 'r')
bunny_mini = d.read()
e = open('./art/FOX_MINI.TCR', 'r')
fox_mini = e.read()
g = open('./art/keyghost_mini.TCR', 'r')
keyghost_mini = g.read()

TCR_SHOW1()
print (
fox_mini + '''so what now?'''
)
nullstuff = raw_input('\n')
TCR_SHOW1()
print (
bunny_mini + '''I have no idea.'''
)
nullstuff = raw_input('\n')
TCR_SHOW1()
print (
keyghost_mini + '''Please, allow me to shed some light on your troubles.'''
)
f.close()
nullstuff = raw_input('\n')
f = open('./art/EP1INTRO1.TCR', 'r')
tcr_contents = f.read()
TCR_SHOW1()
print (
fox_mini + '''MEEP! a ghost!'''
)
nullstuff = raw_input()
TCR_SHOW1()
print (
bunny_mini + '''"ugh." *facepaw* "Apologies for him sir. Please, explain."'''
)
nullstuff = raw_input()
TCR_SHOW1()
print (
keyghost_mini + '''Thank you. Now, see these three doors?'''
)
nullstuff = raw_input()
TCR_SHOW1()
print (
bunny_mini + '''Yes, What about em?'''
)
nullstuff = raw_input()
TCR_SHOW1()
print (
keyghost_mini + '''well each leads to a different area of the prison...'''
)
nullstuff = raw_input()
TCR_SHOW1()
print (
keyghost_mini + '''and each area contains a well hiden, spare keycard.'''
)
nullstuff = raw_input()
TCR_SHOW1()
print (
bunny_mini + '''We need all three to get out of this place, don't we?'''
)
nullstuff = raw_input()
TCR_SHOW1()
print (
keyghost_mini + '''correct! they are RED, BLUE and GREEN. And if you fail...'''
)
nullstuff = raw_input()
TCR_SHOW1()
print (
fox_mini + '''o_o "w-what?"'''
)
nullstuff = raw_input()
TCR_SHOW1()
print (
keyghost_mini + '''you will be trapped here, FOREVER!!! WAHAHAHAhaha....!!!'''
)
f.close()
g.close()
nullstuff = raw_input()
f = open('./art/atrium1.TCR', 'r')
tcr_contents = f.read()
TCR_SHOW1()
print (
fox_mini + '''"phew, he's gone.  I'm glad thats over." DX'''
)
nullstuff = raw_input()
TCR_SHOW1()
print (
bunny_mini + '''you heard what he said, Red Keycard here we come!'''
)
nullstuff = raw_input()
TCR_SHOW1()
print (
fox_mini + '''*shrug* "Here we go again..."'''
)
nullstuff = raw_input()
f.close()

d.close()
e.close()
