#!/usr/bin/env python3

import sys
import re

filename = sys.argv[1]

colors = ["red", "green", "blue"]

total = 0
games = {}

with open(filename, "r") as f:
    lines = f.readlines()
    for game, line in enumerate(lines, 1):
        x = re.findall(r'[0-9]+ red', line),
        x_vals = []
        for i in x:
            for group in i:
                x_vals.append(int(group.split()[0]))
        y = re.findall(r'[0-9]+ green', line),
        y_vals = []
        for i in y:
            for group in i:
                y_vals.append(int(group.split()[0]))
        z = re.findall(r'[0-9]+ blue', line),
        z_vals = []
        for i in z:
            for group in i:
                z_vals.append(int(group.split()[0]))
        total += max(z_vals) * max(y_vals) * max(x_vals)

print(total)
