"""
Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:
Number of vowels: 5
"""

s = str(input("enter a lower-case string: "))
vowels = ['a', 'e', 'i', 'o', 'u']
count = 0
for i in range(len(s)):
    a = s[i]
    if a in vowels:
        count += 1
print("Number of vowels: " + str(count))
