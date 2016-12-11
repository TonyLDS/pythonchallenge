# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 18:45:36 2016

@author: luzhangqin
"""

#http://www.pythonchallenge.com/pc/def/ocr.html
#1
ocr = open('ocr.txt','r')
ocr_read = ocr.read()

ocr_result = ''
for i in ocr_read:
    if 'a' <= i <='z':
    #if i.isalpha():
        ocr_result = ocr_result + i

print ocr_result