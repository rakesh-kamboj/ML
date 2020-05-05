# -*- coding: utf-8 -*-
"""
Created on Mon May  4 22:23:10 2020

@author: Vikki
"""
import pandas as pd
from bs4 import BeautifulSoup

from Plot_AQI import avg_data_2013,avg_data_2014,avg_data_2015,avg_data_2016,avg_data_2017,avg_data_2018

def met_data(month, year):
    file_html = open("data/Html_Data/{}/{}.html".format(year, month), 'rb')
    plain_text = file_html.read()
    
    tempD = []
    finalD = []

    soup = BeautifulSoup(plain_text, "lxml")
    for table in soup.find_all('table',{'class':'medias mensuales numspan'}):
        for tbody in table:
            for tr in tbody:
                a = tr.get_text()
                tempD.append(a)
    
    rows = len(tempD) / 15
    
    for times in range(round(rows)):
        newtempD = []
        for i in range(15):
            newtempD.append(tempD[0])
            tempD.pop(0)
            
        finalD.append(newtempD)
            
               
                 
   ## print(soup)

if __name__ == "__main__":
    met_data(1,2013)