# https://adventofcode.com/2020/day/4
import re

if __name__ == "__main__":
    curr = []
    num_valid = 0
    valid = ["ecl","pid","eyr","byr","iyr","hgt","hcl"]
    with open('./input.txt', 'r') as f:
        lines = f.read().split("\n\n")

    for line in lines:
        line = re.sub(r'\n', r' ', line)
        t = line.split(" ")

        # check if x != '' since the last line in the file is a single '\n'
        curr = [x[:x.index(':')] for x in t if x != '' and x[:x.index(':')] != "cid"]
        if len(curr) == len(valid):
            num_valid += 1
    
    print("Number of valid passports: {}".format(num_valid))
