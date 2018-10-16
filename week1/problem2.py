"""
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2
"""

s = str(input("Enter a lower-case string:" ))
count = 0
bob = "bob"
for i in range(len(s) - 2):
    if bob in s[i:i+3]:
        count += 1
print("Number of time bob occurs is: " + str(count))
