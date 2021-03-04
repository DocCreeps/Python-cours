# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 11:10:36 2021

@author: doria
"""

#https://psutil.readthedocs.io/en/latest/ 

import psutil 

import datetime 

import time 

temps = 1 

max_temps=5 

count=1 

while count < max_temps: 

    print(datetime.datetime.now().time(), psutil.cpu_times_percent(interval=1)) 

    time.sleep(temps) 

    count += 1 