#!/usr/bin/env python
# coding=utf-8
# Episode 1 intro.

f = open('./art/atrium1.TCR', 'r')
tcr_contents = f.read()
def TCR_SHOW1():
	print(chr(27) + "[2J" + chr(27) + "[H" + tcr_contents)

d = open('./art/BUN_MINI.TCR', 'r')
bunny_mini = d.read()
e = open('./art/FOX_MINI.TCR', 'r')
fox_mini = e.read()
g = open('./art/opening1d.TCR')
tcr_contentsb = g.read()
TCR_SHOW1()
print (
fox_mini + '''Well that was interesting.'''
)
nullstuff = raw_input()
TCR_SHOW1()
print (
bunny_mini + '''indeed. So what shall we do now, fox?'''
)
nullstuff = raw_input()
print(chr(27) + "[2J" + chr(27) + "[H" + tcr_contentsb)
print (
fox_mini + '''Well we have the RED keycard.'''
)
nullstuff = raw_input()
print(chr(27) + "[2J" + chr(27) + "[H" + tcr_contentsb)
print (
bunny_mini + '''And we have two more to find. Blue and Green.'''
)
nullstuff = raw_input()
TCR_SHOW1()
print (
bunny_mini + '''Welp, Blue keycard here we come!'''
)
nullstuff = raw_input()

f.close()
g.close()
d.close()
e.close()
