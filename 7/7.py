# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 22:28:00 2016

@author: luzhangqin
"""

#http://www.pythonchallenge.com/pc/def/channel.html

import zipfile
import re
channel = zipfile.ZipFile("/home/luzhangqin/桌面/channel.zip", "r")
print channel.read("readme.txt")
channel_after = '90052'
channel_before = ''

try:
    while True:
        zipInfo = channel.getinfo(channel_after + ".txt")
        print zipInfo.comment,
        channel_after = re.findall(r'\d+', channel.read(channel_after + ".txt")) 
        channel_after = channel_after[0]
        if channel_after:
            channel_before =  channel_after
except Exception,ex:
    print Exception,ex
finally:
     print  channel.read(channel_before + ".txt")
