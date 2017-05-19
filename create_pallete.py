#!/usr/bin/python

import math
import colorsys
import struct
import binascii

html_table='<div style="width:100%; display:table; table-layout: fixed;">'
html_row='<div style="display: table-row; height:20px">'
html_color='<div style="width:20%; background-color:{}; opacity:{}; display: table-cell"></div>'
html_color_code='<div style="width:8%; padding-left:1%; display: table-cell">{}</div>'
html_color_name='<div style="width:12%; display: table-cell">{}</div>'
html_use_url='<div style="display: table-cell"><a href={}>{}</a></div>'
html_close_div='</div>'

colors = []

class ColorEntry:

    def __init__(self, line):
        self.filename, self.colorCode, self.colorName = line.split(";")
        if len(self.colorCode) > 7: # #33FFCCEE - we have opacity here
            #print ('found opacity', hex_to_rgb(self.color))
            #print('found color with opacity', self.color[1:-4], int(self.color[1:-4])/256.0)
            self.opacity = (hex_to_rgb(self.colorCode))[0]/256.0
            self.color = '#'+self.colorCode[3:]
        else:
            self.color = self.colorCode

    color = "#000000"
    colorCode = "#00000000"
    filename = "filename"
    string = 0
    colorName = "undefined"
    opacity = 1


def read_color_to_list():
    with open(".tmp.colors") as f:
            tmp = f.read().splitlines()
    for i in tmp:
        colors.append(ColorEntry(i))


def print_colors(colors):
	print (html_table)
	for i in colors:
		print (html_row)
		print (html_color.format(i.color, i.opacity))
		print (html_color_code.format(i.colorCode))
		print (html_color_name.format(i.colorName))
		#TODO: use urls
		print (html_use_url.format(i.filename, i.filename))
		print (html_close_div)
	print (html_close_div)

def step (t_rgb, repetitions=1):
	r = t_rgb[0]
	g = t_rgb[1]
	b = t_rgb[2]
	lum = math.sqrt( .241 * r + .691 * g + .068 * b )
	h, s, v = colorsys.rgb_to_hsv(r,g,b)
	h2 = int(h * repetitions)
	lum2 = int(lum * repetitions)
	v2 = int(v * repetitions)
	return (h2, lum, v2)

def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb


read_color_to_list()
colors.sort(key=lambda color_entry : step(hex_to_rgb(color_entry.color),16))
print_colors(colors)
