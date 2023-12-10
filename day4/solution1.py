#!/usr/bin/env python3

import sys

filepath = sys.argv[1]

def parse(line: str) -> int:
    card = []
    winning = []
    
    raw = line.split(":")[1].split("|")
    card = raw[0].split()
    winning = raw[1].split()

    score = 0
    for num in card:
        if num in winning:
            if score == 0:
                score += 1
            else:
                score = score << 1

    return score



with open(filepath, 'r') as f:
    score = 0
    for line in f.readlines():
        score += parse(line)

    print(score)
