
with open("input6.txt") as raw:
    lines = raw.readlines()

sumUnique = 0
unique = []
person = 0
temp = []

# Parse a group
for line in lines:
    temp = []
    if (line != "\n"):
        # You found a person!
        line = line.strip()
        # If it's the first person, add all their letters
        if person == 0:
            for x in line:
                unique.append(x)
        # If it's not the first person, start checking
        else:
            # Check that all the letters in the previous people are in the next person
            for x in unique:
                temp.append(x)
            for x in temp:
                if x not in line:
                    unique.remove(x)
        person += 1

    # End of the group
    else:
        sumUnique += len(unique)
        # Reset values
        unique = []
        person = 0

print(sumUnique)