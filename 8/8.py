# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 22:31:58 2016

@author: luzhangqin
"""

#http://www.pythonchallenge.com/pc/def/oxygen.html

import Image

oxygen = Image.open("oxygen.png","r")
print oxygen.format,oxygen.size,oxygen.mode

oxygen_w,oxygen_h = oxygen.size
oxygen_list = []
for oxygen_i in range(oxygen_w/7):
    r,g,b,a = oxygen.getpixel((oxygen_i*7,oxygen_h/2))
    if r==g==b:
        oxygen_list.append(r)
print "".join(map(chr,oxygen_list))
print "".join(map(chr,[105, 110, 116, 101, 103, 114, 105, 116, 121]))
