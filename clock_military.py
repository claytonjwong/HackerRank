#!/bin/python3

import sys
import re


def timeConversion(s):
    
    valid_len = len ( "hh:mm:ssXM")
    
    if s is None or len(s) != valid_len:
        return None
    
    regex = re.compile("^([0-9]+):([0-9]+):([0-9]+)(\w+)$")
    
    m = regex.match(s)
    
    if not m:
        return None
    
    hour = m.group(1)
    min = m.group(2)
    sec = m.group(3)
    am_or_pm = m.group(4)
    
    if am_or_pm == "AM":
        
        if hour == "12":
            hour = "00"
            
        return hour + ":" + min + ":" + sec
    
    else: # am_or_pm == "PM"
        
        if int(hour) < 12:
            # ih is int hour, and 12 onto it for converting PMs
            
            ih = int(hour)
            ih += 12
            
            hour = str(ih)
            
        return hour + ":" + min + ":" + sec
        

s = input().strip()
result = timeConversion(s)
print(result)
