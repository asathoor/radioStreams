#!/usr/bin/env python
# -*- coding: utf-8 -*-
# file: radioAppjar.py
# purpose: simple internet radio player for a pi or similar
# by: per thykjaer jensen

import subprocess as sub # OS specifikke kommandoer
import signal
# import the library
from appJar import gui
# create a GUI variable called app
app = gui()

'''
Radiokanaler
'''
channels = [

    ("SOMA Spacestation","http://somafm.com/spacestation.pls"),
    ("SOMA Suburbs of Goa","http://somafm.com/suburbsofgoa130.pls"),
		("SOMA Secret Agent","http://somafm.com/secretagent130.pls"),
		("SOMA Lush","http://somafm.com/lush130.pls"),
		("SOMA The Silent Channel","http://somafm.com/silent130.pls"),
		("SOMA Indie Pop Rocks","http://somafm.com/indiepop130.pls"),
		("DR P1","http://live-icy.gss.dr.dk/A/A03H.mp3.m3u"),
		("DR Østjylland", "http://live-icy.gss.dr.dk/A/A14H.mp3.m3u"),
		("DR Nyhederne", "http://live-icy.gss.dr.dk/A/A02L.mp3.m3u")

    ]

def press(btn):
	print(btn) # test
	app.stop()
	playing = sub.call(["mplayer", "-playlist", btn])
	# music playing all right.
	# issue: well, how do we kill the stream?

	
'''
Buttons
'''
for x in range (0, len(channels) ):
	app.addLabel( "L" + str(x), channels[x][0], x, 0 ) # labelId, text, row, col
	app.addButton( channels[x][1], press, x, 1 ) # value, function, row, col
	
'''
Loop
'''
app.go()
