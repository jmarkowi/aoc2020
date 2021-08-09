# Solution to the 2nd puzzle

# Open and read input
with open("input.txt") as raw:
    lines = raw.readlines()

data = []
numValid = 0

# Add each line to the list
for line in lines:
    line = line.strip()
    data.append(line)

# Separate the components in the password policy
for line in data:
    line = line.strip().split(":")
    password = line[1].strip()
    policy = line[0]
    policy = policy.split("-")
    pos1 = int(policy.pop(0)) - 1
    policy = policy[0].split()
    pos2 = int(policy[0]) - 1
    required = policy[1]
    # print(f"The letter {required} must be present from {minimum} to {maximum} times in {password}.")

    # Validate the password
    # print(password[pos1])
    # print(password[pos2])
    if (password[pos1] == required) or (password[pos2] == required):
        numValid += 1
    if (password[pos1] == required) and (password[pos2] == required):
        numValid -= 1

print(numValid)