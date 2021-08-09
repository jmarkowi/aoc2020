# Required fields:
# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)

# Open and read input
with open("input4.txt") as raw:
    lines = raw.readlines()

valid = 0
passport = " "
# Add info to passport string
for line in lines:
    # Check that you've reached the end of a passport entry by looking for blank line
    if (line == "\n"):
        if (
            (passport.find("byr") != -1) and (passport.find("iyr") != -1) and
            (passport.find("eyr") != -1) and (passport.find("hgt") != -1) and
            (passport.find("hcl") != -1) and (passport.find("hgt") != -1) and
            (passport.find("ecl") != -1) and (passport.find("pid") != -1)
            ):
                valid += 1
        passport = " "
    else:
        passport += line

print(valid)