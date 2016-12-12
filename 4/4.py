# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 15:57:29 2016

@author: luzhangqin
"""

#http://www.pythonchallenge.com/pc/def/equality.html

import re

equlity = open('equality.txt','r')
ans = ''  
tmp = equlity.read()  
pattern = "[a-z][A-Z][A-Z][A-Z][a-z][A-Z][A-Z][A-Z][a-z]"  
temp = ''  
for match in re.findall(pattern,tmp):  
    temp += match[4]  
print temp  
