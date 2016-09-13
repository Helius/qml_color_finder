#!/usr/bin/python

import random
import math
import colorsys
import struct
import binascii

html_table='<div style="width:100%; display:table; table-layout: fixed;">'
html_row='<div style="display: table-row; height:20px">'
html_color='<div style="width:20%; background-color:{}; display: table-cell"></div>'
html_color_code='<div style="width:5%; padding-left:1%; display: table-cell">{}</div>'
html_color_name='<div style="width:8%; display: table-cell">{}</div>'
html_use_url='<div style="display: table-cell"><a href={}>{}</a></div>'
html_close_div='</div>'

def print_colours(colours):
	print (html_table)
	for i in colours:
		print (html_row)
		c = str(binascii.hexlify(struct.pack('BBB',*i)),'ascii')
		print (html_color.format(c))
		print (html_color_code.format(c))
		print (html_color_name.format("warmGray"))
		#TODO: use urls
		print (html_use_url.format("ProjectQml/Hecateus/bla/bla/someFile.qml#233","Hecateus/bla/bla/someFile.qml#233"))
		print (html_close_div)
	print (html_close_div)

def step (r,g,b, repetitions=1):
	lum = math.sqrt( .241 * r + .691 * g + .068 * b )
	h, s, v = colorsys.rgb_to_hsv(r,g,b)
	h2 = int(h * repetitions)
	lum2 = int(lum * repetitions)
	v2 = int(v * repetitions)
	return (h2, lum, v2)

colours_length = 1000
colours = []
for i in range(1, colours_length):
	colours.append (
		[
			int(random.random()*256),
			int(random.random()*256),
			int(random.random()*256)
		]
	)


colours.sort(key=lambda rgb : step(rgb[0],rgb[1],rgb[2],8))

print_colours(colours)
