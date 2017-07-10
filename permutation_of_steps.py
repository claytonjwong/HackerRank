"""

Recursion: Davis' Staircase

https://www.hackerrank.com/challenges/ctci-recursive-staircase

 Davis has  staircases in his house and he likes to climb each staircase , , or  steps at a time. Being a very precocious child, he wonders how many ways there are to reach the top of the staircase.

Given the respective heights for each of the  staircases in his house, find and print the number of ways he can climb each staircase on a new line.

Input Format

The first line contains a single integer, , denoting the number of staircases in his house. 
Each line  of the  subsequent lines contains a single integer, , denoting the height of staircase .

Constraints

Subtasks

 for  of the maximum score.
Output Format

For each staircase, print the number of ways Davis can climb it in a new line.

Sample Input

3
1
3
7
Sample Output

1
4
44
Explanation

Let's calculate the number of ways of climbing the first two of the Davis'  staircases:

The first staircase only has  step, so there is only one way for him to climb it (i.e., by jumping  step). Thus, we print  on a new line.
The second staircase has  steps and he can climb it in any of the four following ways: 
Thus, we print  on a new line.


"""


dic = {}

def f(i):
    
    if i < 0:
        return 0
    
    if i == 0:
        dic[0] = 1
        return 1
    
    step1 = f(i-1) if i-1 not in dic else dic[i-1]
    if i-1 not in dic:
        dic[i-1] = step1
    
    step2 = f(i-2) if i-2 not in dic else dic[i-2]
    if i-2 not in dic:
        dic[i-2] = step2
    
    step3 = f(i-3) if i-3 not in dic else dic[i-3]
    if i-3 not in dic:
        dic[i-3] = step3
        
    return step1 + step2 + step3

s = int(input().strip())
for a0 in range(s):
    n = int(input().strip())

    staircase = n
    print(str(  f(staircase)  ))








