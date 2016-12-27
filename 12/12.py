# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 11:50:30 2016

@author: luzhangqin
"""

#http://www.pythonchallenge.com/pc/return/5808.html

import Image

odd_even_open = Image.open("cave.jpg","r")

odd_even_open_w, odd_even_open_h = odd_even_open.size
print odd_even_open_w, odd_even_open_h

even_even = Image.new('RGB', (odd_even_open_w/2,odd_even_open_h/2))
even_odd = Image.new('RGB', (odd_even_open_w/2,odd_even_open_h/2))
odd_odd = Image.new('RGB', (odd_even_open_w/2,odd_even_open_h/2))
odd_even = Image.new('RGB', (odd_even_open_w/2,odd_even_open_h/2))

for odd_even_open_x in range(odd_even_open_w):
    for odd_even_open_y in range(odd_even_open_h):
        if odd_even_open_x % 2 == 0 and odd_even_open_y % 2 == 0:
            even_even.putpixel((odd_even_open_x / 2, odd_even_open_y / 2),
                               odd_even_open.getpixel((odd_even_open_x,
                                                     odd_even_open_y)))

for odd_even_open_x in range(odd_even_open_w):
    for odd_even_open_y in range(odd_even_open_h):
       if odd_even_open_x % 2 == 1 and odd_even_open_y % 2 == 1:
            odd_odd.putpixel((odd_even_open_x / 2, odd_even_open_y / 2),
                               odd_even_open.getpixel((odd_even_open_x,
                                                     odd_even_open_y)))

for odd_even_open_x in range(odd_even_open_w):
    for odd_even_open_y in range(odd_even_open_h):
       if odd_even_open_x % 2 == 1 and odd_even_open_y % 2 == 0:
            even_odd.putpixel((odd_even_open_x / 2, odd_even_open_y / 2),
                               odd_even_open.getpixel((odd_even_open_x,
                                                     odd_even_open_y)))

for odd_even_open_x in range(odd_even_open_w):
    for odd_even_open_y in range(odd_even_open_h):
       if odd_even_open_x % 2 == 0 and odd_even_open_y % 2 == 1:
            odd_even.putpixel((odd_even_open_x / 2, odd_even_open_y / 2),
                               odd_even_open.getpixel((odd_even_open_x,
                                                     odd_even_open_y)))
even_even.show()
odd_odd.show()
even_odd.show()
odd_even.show()