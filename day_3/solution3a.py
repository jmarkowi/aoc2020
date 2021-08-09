
# 3 right, 1 down; . = open; # = tree
# use mod function to represent endless rightward repeat of pattern

# Open and read input
with open("input3.txt") as raw:
    lines = raw.readlines()

right = 0
trees = 0
down = 0

# Test spot on each line 3 right, 1 down
for line in lines:
    line = line.strip()
    # Ensure "right" is within the length of the line (minus 1)
    if (down % 2 == 0):
        if (right > len(line) - 1):
            right = right % len(line)
        # Test position for tree
        if (line[right] == "#"):
            trees += 1
        # Increment right
        right += 1
    down += 1

print(trees)

# python solution3a.py