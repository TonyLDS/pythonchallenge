# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 16:41:38 2016

@author: luzhangqin
"""

#http://www.pythonchallenge.com/pc/return/good.html

import Image, ImageDraw

good_first = open('good_first.txt','r')
good_first_r = good_first.read()
good_first_list = (good_first_r.strip('\n')).split(',')

good_second = open('good_second.txt','r')
good_second_r = good_second.read()
good_second_list = (good_second_r.strip('\n')).split(',')

good_first_result = []
good_first_list_x = good_first_list[::2]
good_first_list_y = good_first_list[1::2]
for i in range(len(good_first_list_x)):
    good_first_result.append((int(good_first_list_x[i]),int(good_first_list_y[i])))

good_second_result = []
good_second_list_x = good_second_list[::2]
good_second_list_y = good_second_list[1::2]
for i in range(len(good_second_list_x)):
    good_second_result.append((int(good_second_list_x[i]),int(good_second_list_y[i])))

good_first_tuple = ()
good_first_tuple = tuple(good_first_result)

good_second_tuple = ()
good_second_tuple = tuple(good_second_result)

good_img = Image.new('RGB', (640,480))
good_draw = ImageDraw.Draw(good_img)
good_draw.line(good_first_tuple)
good_draw.line(good_second_tuple)
good_img.show()
