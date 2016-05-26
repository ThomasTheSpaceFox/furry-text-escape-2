#!/usr/bin/env python
# coding=utf-8
# CINAMATIC SEQUENCE 1: Opening
d = open('./art/BUN_MINI.TCR', 'r')
bunny_mini = d.read()
e = open('./art/FOX_MINI.TCR', 'r')
fox_mini = e.read()
f = open('./art/opening1a-b.TCR', 'r')
tcr_contents = f.read()
print(chr(27) + "[2J" + chr(27) + "[H" + tcr_contents)
print (
'''You look in the mirror. Wondering, yet again, how you 
get in these situations...'''
)
nullstuff = raw_input('\n')
print(chr(27) + "[2J" + chr(27) + "[H" + tcr_contents)
print (
'''Once more you are trapped.'''
)
nullstuff = raw_input('\n')
print(chr(27) + "[2J" + chr(27) + "[H" + tcr_contents)
print (
fox_mini + '''"at least this time..."'''
)
nullstuff = raw_input('\n')
print(chr(27) + "[2J" + chr(27) + "[H" + tcr_contents)
print (
fox_mini + '''"the room isn't dark."'''
)
nullstuff = raw_input('\n')
print(chr(27) + "[2J" + chr(27) + "[H" + tcr_contents)
f.close()
print (
'''It seems only a year since you escaped a very dark room with the help
of a peculiar bunny.'''
)
nullstuff = raw_input('\n')
f = open('./art/opening1a.TCR', 'r')
tcr_contents = f.read()
print(chr(27) + "[2J" + chr(27) + "[H" + tcr_contents)
print (
'''Suddenly, you see a familiar face out of the corner of your eye.'''
)
nullstuff = raw_input('\n')
print(chr(27) + "[2J" + chr(27) + "[H" + tcr_contents)
print (
bunny_mini + '''"Hi!"'''
)
nullstuff = raw_input('\n')
print(chr(27) + "[2J" + chr(27) + "[H" + tcr_contents)
print (
fox_mini + '''"umm.. hello? Can you get me out of here?"'''
)
nullstuff = raw_input('\n')
print(chr(27) + "[2J" + chr(27) + "[H" + tcr_contents)
print (
bunny_mini + '''"Not really, But i can let you out of this room so we can
get out of this crazy place!"'''
)
nullstuff = raw_input('\n')
print(chr(27) + "[2J" + chr(27) + "[H" + tcr_contents)
f.close()
print (
bunny_mini + '''"I'd stand back if i were you!"'''
)
nullstuff = raw_input('\n')
print(chr(27) + "[2J" + chr(27) + "[H" + tcr_contents)
f.close()
print (
fox_mini + '''"ok.."'''
)
nullstuff = raw_input('\n')
f = open('./art/FX-CRASH.TCR', 'r')
tcr_contents = f.read()
print(chr(27) + "[2J" + chr(27) + "[H" + tcr_contents)
f.close()
print (
'''*Crash!*'''
)
nullstuff = raw_input('\n')
f = open('./art/opening1a-c.TCR', 'r')
tcr_contents = f.read()
print(chr(27) + "[2J" + chr(27) + "[H" + tcr_contents)
print (
fox_mini + '''"Did... Did you just smash the door out of the wall! o_o"'''
)
nullstuff = raw_input('\n')
print(chr(27) + "[2J" + chr(27) + "[H" + tcr_contents)
f.close()
print (
bunny_mini + '''"Yes, yes i did. Now lets get going!"'''
)
nullstuff = raw_input('\n')
f = open('./art/opening1b.TCR', 'r')
tcr_contents = f.read()
print(chr(27) + "[2J" + chr(27) + "[H" + tcr_contents)
f.close()
print (
'''And so our adventure begins. Our heros, once again on a quest to escape.'''
)
nullstuff = raw_input('\n')
f = open('./art/opening1c.TCR', 'r')
tcr_contents = f.read()
print(chr(27) + "[2J" + chr(27) + "[H" + tcr_contents)
f.close()
print (
'''will our heroes escape this strange, ghostly, forgotten prison?'''
)
nullstuff = raw_input('\n')
f = open('./art/opening1d.TCR', 'r')
tcr_contents = f.read()
print(chr(27) + "[2J" + chr(27) + "[H" + tcr_contents)
f.close()
print (
'''Only time will tell...'''
)
nullstuff = raw_input('\n')
d.close()
e.close()