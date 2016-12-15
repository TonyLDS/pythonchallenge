# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 20:48:08 2016

@author: luzhangqin
"""

#http://www.pythonchallenge.com/pc/def/linkedlist.php

import urllib
import re

linkedlist = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
linkedlist_after = '27935'
try:
    for i in range(400):
        linkedlist_open = urllib.urlopen(linkedlist+linkedlist_after)
        linkedlist_after = re.findall(r'\d+',linkedlist_open.read())
        linkedlist_after = linkedlist_after[0]
        print linkedlist_after
finally:
        pass
