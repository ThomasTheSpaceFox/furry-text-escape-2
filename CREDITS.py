#!/usr/bin/env python
# coding=utf-8
# CINAMATIC SEQUENCE 1: Opening
f = open('./art/credits_banner.TCR', 'r')
credits_banner = f.read()
print(chr(27) + "[2J" + chr(27) + "[H" + credits_banner)
print (
'''             ---Credits---
-> Block Graphics Artist:      Thomas Leathers
-> Lead Story Writer:          Thomas Leathers
-> Lead Programmer:            Thomas Leathers
'''
)
nullstuff = raw_input('\n')
print(chr(27) + "[2J" + chr(27) + "[H" + credits_banner)
print (
'''               ---Special Thanks---
-> A special Thanks to the furry community for being awesome. :)
'''
)
nullstuff = raw_input('\n')
print(chr(27) + "[2J" + chr(27) + "[H" + credits_banner)
print (
'''---About Furry Text Escape II---
(c) 2015-2016 Thomas Leathers

Furry Text Escape II is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Furry Text Escape II is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Furry Text Escape II.  If not, see <http://www.gnu.org/licenses/>.'''
)
nullstuff = raw_input('\n')
f.close()