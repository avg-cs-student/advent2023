#!/usr/bin/env python3

import sys
from dataclasses import dataclass

@dataclass
class SupportedRange():
    dstart: int
    sstart: int
    length: int

    def includes(self, source: int) -> bool:
        return source in range(self.sstart, self.sstart + self.length)

    def convert(self, source: int) -> int:
        return self.dstart + (source - self.sstart)

@dataclass
class AlmanacMap():
    seedToSoil: list[SupportedRange]
    soilToFertilizer: list[SupportedRange]
    fertilizerToWater: list[SupportedRange]
    waterToLight: list[SupportedRange]
    lightToTemperature: list[SupportedRange]
    temperatureToHumidity: list[SupportedRange]
    humidityToLocation: list[SupportedRange]

    def __init__(self, maps: list[list[SupportedRange]]):
        self.seedToSoil = maps[0]
        self.soilToFertilizer = maps[1]
        self.fertilizerToWater = maps[2]
        self.waterToLight = maps[3]
        self.lightToTemperature = maps[4]
        self.temperatureToHumidity = maps[5]
        self.humidityToLocation = maps[6]

    def get(self, mapList: list[SupportedRange], key: int) -> int:
        val = None
        for m in mapList:
            if m.includes(key):
                val = m.convert(key)
                break
        return val if val else key

    def locate(self, seed: int) -> int:
        soil = self.get(self.seedToSoil, seed)
        fert = self.get(self.soilToFertilizer, soil)
        water = self.get(self.fertilizerToWater, fert)
        light = self.get(self.waterToLight, water)
        temp = self.get(self.lightToTemperature, light)
        humidity = self.get(self.temperatureToHumidity, temp)
        return self.get(self.humidityToLocation, humidity)

filename = sys.argv[1]

with open(filename, "r") as f:
    lines = f.readlines()

# seeds are always on the first line
seeds = [int(s) for s in lines[0].split(":")[1].split()]

maps: list[list[SupportedRange]] = []
curMap: list[SupportedRange] = []
for i in range(1, len(lines)):
    line = lines[i]
    if not line[0].isdigit():
        if curMap:
            maps.append(curMap)
            curMap = []

        continue

    nums = [int(num) for num in line.split()]
    curMap.append(SupportedRange(nums[0], nums[1], nums[2]))

maps.append(curMap)
almanac = AlmanacMap(maps)
for seed in seeds:
    print("seed: ", seed, " location: ", almanac.locate(seed))

print("Optimal location: ", min([l for l in [almanac.locate(s) for s in seeds]]))
