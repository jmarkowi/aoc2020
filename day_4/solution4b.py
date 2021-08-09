
import string

# Required fields:
# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
    # If cm, the number must be at least 150 and at most 193.
    # If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.

def validate(d):
    birth = int(d["byr"])
    issue = int(d["iyr"])
    expir = int(d["eyr"])
    height = d["hgt"]
    hair = d["hcl"]
    eye = d["ecl"]
    pid = d["pid"]

    if (birth < 1920) or (birth > 2002):
        return False
    if (issue < 2010) or (issue > 2020):
        return False
    if (expir < 2020) or (expir > 2030):
        return False

    num = ""
    unit = ""
    for x in range(len(height)):
        if height[x].isnumeric():
            num += height[x]
        else:
            unit += height[x]
    if (unit == "cm"):
        if (int(num) < 150) or (int(num) > 193):
            return False
    if (unit == "in"):
        if (int(num) < 59) or (int(num) > 76):
            return False
    if (unit != "cm") and (unit != "in"):
        return False

    if (hair[0] != "#"):
        return False
    else:
        hair = hair[1:]
        if (len(hair) != 6):
            return False
        for char in hair:
            if not (char.isdigit()) and not (char == "a" or char == "b" or char == "c" or
                char == "d" or char == "e" or char == "f"):
                    return False

    if not ((eye == "amb") or (eye == "blu") or
       (eye == "brn") or (eye == "gry") or (eye == "grn") or
       (eye == "hzl") or (eye == "oth")):
           return False

    if not ((len(pid) == 9) and (pid.isnumeric())):
        return False

    return True

# Open and read input
with open("input4.txt") as raw:
    lines = raw.readlines()
    last = lines[-1]

valid = 0
passport = " "
check = {}

# Add info to passport string
for line in lines:
    # Check that you've reached the end of a passport entry by looking for blank line
    if (line == "\n") or (line is last):
        if ((passport.find("byr") != -1) and (passport.find("iyr") != -1) and
            (passport.find("eyr") != -1) and (passport.find("hgt") != -1) and
            (passport.find("hcl") != -1) and (passport.find("hgt") != -1) and
            (passport.find("ecl") != -1) and (passport.find("pid") != -1)):

            passport = passport.split()
            # Add key:value pairs to dictionary
            check.clear()
            for item in passport:
                item = item.split(":")
                check[item[0]] = item[1]
            # Validate the passport
            if validate(check):
                valid += 1
        passport = " "
    else:
        passport += line.strip()
        passport += " "

print(valid)