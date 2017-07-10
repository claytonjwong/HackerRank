#!/bin/python3

import sys
# import pdb
# pdb.set_trace()

ar = [12,4,5,3,8,7]



i=0
while i < len(ar):
    
    # sort from [0:i)
    sz = i+1
    ar[:sz]=sorted(ar[:sz])
    
    # odd
    if sz % 2 == 1:
        print ( ar[sz//2] * 1.0 )
    else: # even
        print ( (( ar[(sz//2)-1] ) + ( ar[sz//2] )) / 2.0 ) 

    # itr
    i+=1