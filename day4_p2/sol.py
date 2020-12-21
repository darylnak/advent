# https://adventofcode.com/2020/day/4
import re

if __name__ == "__main__":
    curr = []
    num_valid = 0
    valid = ["ecl","pid","eyr","byr","iyr","hgt","hcl"]
    val_ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    with open('./input.txt', 'r') as f:
        lines = f.read().split("\n\n")

    for line in lines:
        line = re.sub(r'\n', r' ', line)
        t = line.split(" ")

        # check x != '' since the last line in the file is a single '\n'
        elems = {x[:x.index(':')]:x[x.index(':')+1:] for x in t if x != '' and x[:x.index(':')] != "cid"}
        if len(elems) == len(valid):
            if (1920 <= int(elems['byr']) <= 2002 and 2010 <= int(elems['iyr']) <= 2020 and 2020 <= int(elems['eyr']) <= 2030 and \
                re.search(r'^#[0-9a-f]{6}$', elems['hcl']) and elems['ecl'] in val_ecl and re.match('^\d{9}$', elems['pid'])):
                if (elems['hgt'][-2:] == 'cm' and 150 <= int(elems['hgt'][:-2]) <= 193) or (elems['hgt'][-2:] == 'in' and 59 <= int(elems['hgt'][:-2]) <= 76):
                    num_valid += 1
    
    print("Number of valid passports: {}".format(num_valid))
