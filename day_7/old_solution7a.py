

bagsDict = {}
bagCount = set()

with open("test_input7.txt") as raw:
    lines = raw.readlines()

# Make a list of all the bag dictionaries
for line in lines:
    line = line.strip()

    line = line.split("bags contain")
    # Add each bag into thee dictionary where {outerBag: innerbags}
    bagsDict[line[0]] = line[1]

# Search the bag dictionaries recursively until you:
    # Hit a shiny gold bag
    # Find another bag (then seach(newBag) recursively)
    # Hit "no other"

def search(color):
    for bag in bagsDict:
        contents = bagsDict[bag]
        if color in contents:
            bagCount.add(bag)
        if "no other" in contents:
            return
        else:
            contents = contents.split(",")
            for bag in contents:
                search(bag)

search("shiny gold")
print(bagCount)