
# 128 rows, 8 columns
# ROW: F = lower; B = higher
# COLUMN: L = lower; R = higher
import math

with open("input5.txt") as raw:
    lines = raw.readlines()

maxSeat = 0

for line in lines:
    minRow = 0
    maxRow = 127
    minColumn = 0
    maxColumn = 7
    line.strip()
    for x in range(9):
        if line[x] == "F":
            maxRow = math.floor(maxRow - ((maxRow - minRow)/2))
            continue
        if line[x] == "B":
            minRow = math.ceil(minRow + ((maxRow - minRow)/2))
            continue
        if line[x] == "L":
            maxColumn = math.floor(maxColumn - ((maxColumn - minColumn)/2))
            continue
        if line[x] == "R":
            minColumn = math.ceil(minColumn + ((maxColumn - minColumn)/2))
            continue

    seat = int((maxRow * 8) + maxColumn)
    if seat > maxSeat:
        maxSeat = seat
    print(f"Seat is number {seat}, in row {int(maxRow)}, column {int(maxColumn)}.")

print(maxSeat)