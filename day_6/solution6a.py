
with open("input6.txt") as raw:
    lines = raw.readlines()

group = ""
uniqueValues = 0

# Parse a group
for line in lines:
    unique = []
    if (line != "\n"):
        group += line.strip()
    else:
        # Find num of unique values
        for x in group:
            if x not in unique:
                unique.append(x)
        # Sum unique values
        uniqueValues += len(unique)
        group = ""

print(uniqueValues)