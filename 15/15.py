# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 11:59:52 2016

@author: luzhangqin
"""

#http://www.pythonchallenge.com/pc/return/italy.html

import Image
italy = Image.open("italy.png",'r')
#italy.size
italy_new = Image.new('RGB',(100,100))
italy_list = [[i,i-1,i-1,i-2] for i in xrange(100,1,-2)]
italy_list = reduce(lambda x, y: x+y, italy_list)

italy_x = 0
italy_y = 0
italy_z = 0

for italy_len in range(len(italy_list)):
    if italy_len % 4 == 0:
        for italy_i in range(italy_list[italy_len]):
            italy_new.putpixel((italy_x,italy_y),
                italy.getpixel((italy_z,0)))
            italy_x = italy_x + 1
            italy_z = italy_z + 1
        italy_x = italy_x - 1

    elif italy_len % 4 == 1:
        for italy_i in range(italy_list[italy_len]):
            italy_new.putpixel((italy_x,italy_y),
                italy.getpixel((italy_z,0)))
            italy_y = italy_y + 1
            italy_z = italy_z + 1
        italy_y = italy_y - 1

    elif italy_len % 4 == 2:
        for italy_i in range(italy_list[italy_len]):
            italy_new.putpixel((italy_x,italy_y),
                italy.getpixel((italy_z,0)))
            italy_x = italy_x - 1
            italy_z = italy_z + 1
        italy_x = italy_x + 1

    elif italy_len % 4 == 3:
        for italy_i in range(italy_list[italy_len]):
            italy_new.putpixel((italy_x,italy_y),
                italy.getpixel((italy_z,0)))
            italy_y = italy_y - 1
            italy_z = italy_z + 1
        italy_y = italy_y + 1

italy_new.show()
