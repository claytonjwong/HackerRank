"""

https://www.hackerrank.com/challenges/staircase

Consider a staircase of size :

   #
  ##
 ###
####
Observe that its base and height are both equal to , and the image is drawn using # symbols and spaces. The last line is not preceded by any spaces.

Write a program that prints a staircase of size .

Input Format

A single integer, , denoting the size of the staircase.

Output Format

Print a staircase of size  using # symbols and spaces.

Note: The last line must have  spaces in it.

Sample Input

6 
Sample Output

     #
    ##
   ###
  ####
 #####
######
Explanation

The staircase is right-aligned, composed of # symbols and spaces, and has a height and width of .

"""

#!/bin/python3

import sys


n = int(input().strip())

# n - 1 spaces followed by 1 #
# n - 2 spaces followed by 2 #s

# n - n spaces followed by n #s

# iterate from [i:n]
for i in range ( 1, n+1 ):
    
    # create a line of n-i spaces followed by i hashes
    spaces = (n-i) * " "
    hashes = i * "#"
    
    print (spaces + hashes + "\n")
    