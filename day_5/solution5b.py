
# Trying this the binary way! (https://www.reddit.com/r/adventofcode/comments/k75x7d/day_5_binary_explanation/?utm_source=share&utm_medium=ios_app&utm_name=iossmf)

with open("input5.txt") as raw:
    lines = raw.readlines()

def swap(a):
    if a=="F" or a =="L":
        a="0"
    else:
        a="1"
    return a

seatCheck = []

for line in lines:
    seat = int("".join(map(swap, line.strip())), 2)
    seatCheck.append(seat)

seatCheck.sort()
for x in range(len(seatCheck)-1):
    if (seatCheck[x+1]-seatCheck[x] != 1):
        print(seatCheck[x]+1)