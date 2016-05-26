#!/usr/bin/env python
# coding=utf-8
# Furry Text Escape 2 main script
gamevers = ('v1.0')
f = open('./art/title1.TCR', 'r')
tcr_contents = f.read()
print (tcr_contents)
f.close()
print (
'''Furry Text Escape II
(c) 2015-2016 Thomas Leathers
'''
)


nullstuff = raw_input('press enter to continue.\n')
print(chr(27) + "[2J" + chr(27) + "[H")
execfile("CINA1-OPEN.py")
print(chr(27) + "[2J" + chr(27) + "[H")