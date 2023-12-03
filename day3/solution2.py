#!/usr/bin/env python3

import sys
from dataclasses import dataclass

filename = sys.argv[1]

@dataclass
class Num:
    y: int
    x_start: int
    x_end: int
    val: int
    raw: str
    isPart: bool

    def __str__(self):
        return f"val: {self.val} spans: {self.x_start}->{self.x_end} y:{self.y} part? {self.isPart}"

@dataclass
class Sym:
    y: int
    x: int
    raw: str
    adjTo: []

    def __str__(self):
        return f"val: {self.raw} x: {self.x} y: {self.y}"

with open(filename, 'r') as f:
    lines = f.readlines()
    
    numbers = []
    symbols = []
    for col, line in enumerate(lines):
        inNum = False
        num = ""
        x = 0
        y = col 
        for index, char in enumerate(line):
            if char.isdigit():
                if inNum == False:
                    x = index
                inNum = True
                num += char
            else:
                if inNum:
                    numbers.append(
                            Num(y, x, x + len(num), int(num), num, False)
                    )
                    num = ""
                inNum = False
                if char == "*":
                    symbols.append(Sym(col, index, char, []))

result = 0
for n in numbers:
    for s in symbols:
        if s.y not in [n.y-1, n.y, n.y + 1]:
            continue
        if s.x not in range(n.x_start - 1, n.x_end + 1):
            continue
        s.adjTo.append(n.val)

for s in symbols:
    if len(s.adjTo) == 2:
        result += s.adjTo[0] * s.adjTo[1]

print(result)
