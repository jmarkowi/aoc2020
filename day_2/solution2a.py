# Solution to the 2nd puzzle

# Open and read input into dictionary
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
    password = line[1]
    policy = line[0]
    policy = policy.split("-")
    minimum = int(policy.pop(0))
    policy = policy[0].split()
    maximum = int(policy[0])
    required = policy[1]
    # print(f"The letter {required} must be present from {minimum} to {maximum} times in {password}.")

    # Validate the password
    count = 0
    for letter in password:
        if (required == letter):
            count += 1

    # Count valid passwords
    if (count >= minimum) & (count <= maximum):
        print(f"{password} contains {required} {count} number of times.")
        numValid += 1

print(numValid)