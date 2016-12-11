# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 18:41:44 2016

@author: luzhangqin
"""

#http://www.pythonchallenge.com/pc/def/map.html
zf = """
g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.
"""

#1
a = ''

for i in zf:
    if 'a' <= i <= 'x':
        i = chr(ord(i) + 2)
    elif 'y' <= i <= 'z':
        i = chr(ord(i) - 26 + 2)

    a = a + i

print a


#2

import string

a = ''
intab = 'abcdefghijklmnopqrstuvwxyz'
outtab = 'cdefghijklmnopqrstuvwxyzab'

trantab = string.maketrans(intab,outtab)
print zf.translate(trantab)

map = 'map'
print map.translate(trantab)