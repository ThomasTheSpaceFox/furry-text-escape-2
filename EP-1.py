#!/usr/bin/env python
# coding=utf-8
# Episode no: 1
gameitem_REDkeycard = ('1')

def inventory_screen():
	print ('''---Inventory---''')
	if gameitem_REDkeycard==('1'):
		print ('Red Keycard: Yes')
	elif gameitem_REDkeycard==('0'):
		print ('Red Keycard: No.')
	

inventory_screen()
