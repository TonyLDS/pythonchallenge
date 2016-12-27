# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 11:58:02 2016

@author: luzhangqin
"""

#http://www.pythonchallenge.com/pc/return/disproportional.html

import xmlrpclib

url = 'http://www.pythonchallenge.com/pc/phonebook.php'
phonebook = xmlrpclib.Server(url)
print phonebook.phone('Bert')
