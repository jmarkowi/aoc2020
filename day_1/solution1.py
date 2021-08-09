# Find the product of the 3 numbers from a list whose sum is 2020

import csv

# Check the sum of 3 entries in expenses
def checkSum(a, b, c):
    if (a + b + c == 2020):
        return True
    else:
        return False

# Open and read the input file into a list
rawData = csv.reader(open("data.csv"))
data = []
for entry in rawData:
    data.append(int(entry[0]))

# Find the 3 entries that sum to 2020
for i in range(len(data)):
    for j in range(1, len(data)):
        for k in range(2, len(data)):
            if checkSum(data[i], data[j], data[k]):
                # Calculate the product of those 3 entries
                print(data[i])
                print(data[j])
                print(data[k])
                print(data[i] * data[j] * data[k])
                break