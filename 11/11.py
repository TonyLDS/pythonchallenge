# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 19:09:55 2016

@author: luzhangqin
"""
#http://www.pythonchallenge.com/pc/return/bull.html
bull = '1'
for bull_i in range(30):
    bull_a = bull[0]
    bull_b = 0
    bull_c = ''
    for bull_a in range(len(bull)):
        if bull_a + 1 >= len(bull):
           bull_c = bull_c + str(bull_a + 1 -bull_b)+bull[bull_a]
        else:
            if bull[bull_a] != bull[bull_a+1]:
                bull_c = bull_c + str(bull_a+1 - bull_b) + bull[bull_a]
                bull_b = bull_a + 1
    bull = bull_c

print len(bull)