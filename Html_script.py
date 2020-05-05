# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 00:34:53 2020

@author: Vikki
"""

import os
import time
import requests
import sys

def retrieve_html():
    for year in range (2013,2019):
        for month in range (1,13):
            if(month < 10):
                url="https://en.tutiempo.net/climate/0{}-{}/ws-421820.html".format(month, year)
            else:
                url="https://en.tutiempo.net/climate/{}-{}/ws-421820.html".format(month, year)
            
            texts = requests.get(url)
            text_htf=texts.text.encode('utf=8')
            
            if not os.path.exists("data/Html_Data/{}".format(year)):
                os.makedirs("data/Html_Data/{}".format(year))
            with open("data/Html_Data/{}/{}.html".format(year, month), "wb") as output:
                output.write(text_htf)
            
            
        sys.stdout.flush()
            
    
    
retrieve_html()