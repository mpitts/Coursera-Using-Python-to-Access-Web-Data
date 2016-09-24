#!/usr/bin/python

# Chapter 2: Extracting Data With Regular Expressions

import re

file = open('regex_sum_201873.txt', 'r')

sum = 0

for line in file:
    numbers = re.findall('[0-9]+', line)
    for number in numbers:
        sum = sum + int(number)

print sum
