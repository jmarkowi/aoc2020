with open("test_input7.txt") as raw:
    lines = raw.readlines()

toRemove = ["bag", "bag," "bags", "bags,", "bag.", "bags.", "contain"]

for line in lines:
    line = line.strip()
    line = line.split(" ")
    line = [ele for ele in line if (ele not in toRemove) and not (ele.isnumeric())]
    print(line)