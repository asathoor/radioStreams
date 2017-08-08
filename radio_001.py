#!/usr/bin/env python
# -*- coding: utf-8 -*-
# file: test.py
# purpose: simple internet radio player for a pi or similar
# by: per thykjaer jensen

'''
mplayer turns into a zombie on ctrl+z
if it's a problem kill them ...
'''

import subprocess as sub # OS specifikke kommandoer
import signal

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

'''
Print alle kanaler
'''
for x in range (0, len(channels) ):
	print str( x ) + ": "  + channels[x][0] # must be a string, hence str( x )

'''
Input
'''
tune = input("Vælg en kanal\n")
print "Spiller stream " + channels[ tune ][0]
print "For stop tast [alt]+[z]"

'''
Stream initieres
'''
p = sub.Popen( [
    'mplayer',
    '-playlist',
    channels[ tune ][1] ],
               stdout=sub.PIPE,
               stderr=sub.PIPE)
output, errors = p.communicate()
print output
