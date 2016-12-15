# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 20:51:23 2016

@author: luzhangqin
"""

#http://www.pythonchallenge.com/pc/def/peak.html
#pickle
#banner.p

import cPickle as pickle
peak = open('banner.p','r')
peak_read = peak.read()
peak_load = pickle.loads(peak_read)
for peak_i in peak_load:
    for peak_j in peak_i:
        print peak_j[0]*peak_j[1],
    print
