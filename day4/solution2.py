#!/usr/bin/env python3

import sys

filepath = sys.argv[1]

# map of lines numbers to score for that line
numMap = {}

def parse(line: str) -> int:
    card = []
    winning = []
    
    raw = line.split(":")[1].split("|")
    card = raw[0].split()
    winning = raw[1].split()

    score = 0
    for num in card:
        if num in winning:
            score += 1

    print(line, score)
    return score

with open(filepath, 'r') as f:
    lines = f.readlines()

for index, line in enumerate(lines, 1):
    numMap[index] = parse(line)

# we start with some cards
cards = [1] * len(lines)

# each win gives us more cards
for i, _ in enumerate(cards, 1):
    for k in range(cards[i - 1]):
        for j in range(i + 1, numMap[i] + i + 1):
            cards[j - 1] += 1

print(sum(cards))
