#!/usr/bin/env python3

import sys

filename = sys.argv[1]

nums = { 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 
        '0','1', '2', '3', '4', '5', '6', '7', '8', '9' }

str_to_num = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
        '1': '1',
        '2': '2',
        '3': '3',
        '4': '4',
        '5': '5',
        '6': '6',
        '7': '7',
        '8': '8',
        '9': '9',
}

sum = 0

with open(filename, "r") as f:
    lines = f.readlines()
    for line in lines:
        highest = (-1, 0)
        lowest = (999, 0)
        for n in nums:
            i = line.find(n)
            if i == -1:
                continue
            if i < lowest[0] or lowest[1] == 0:
                lowest = (i, n)

            j = line.find(n, i+1)
            while j > i:
                i = j
                j = line.find(n, i+1)
            if i > highest[0] or highest[1] == 0:
                highest = (i, n)


        print(line, int(str_to_num[lowest[1]] + str_to_num[highest[1]]))
        sum += int(str_to_num[lowest[1]] + str_to_num[highest[1]])

print(sum)
