"""
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc
Note: This problem may be challenging. We encourage you to work smart. If you've spent more than a few hours on this problem, we suggest that you move on to a different part of the course. If you have time, come back to this problem after you've had a break and cleared your head.
"""

s = str(input("Enter a lower-case string: "))
count = 0
maxcount = 0
seq = s[0]
maxseq = seq

for i in range(1, len(s)):
    if s[i] > s[i-1]:
        seq += s[i]
    elif s[i] < s[i-1]:
        maxseq = seq
        seq = s[i]
if len(seq) > len(maxseq):
    print("Longest substring in alphabetical order is: " + str(seq))
else:
    print("Longest substring in alphabetical order is: " + str(maxseq))
