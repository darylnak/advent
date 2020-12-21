# https://adventofcode.com/2020/day/4
import math

if __name__ == "__main__":
    with open('./input.txt', 'r') as f:
        lines = f.readlines()
    
    max_seat = -1
    for line in lines:
        lb = 0
        ub = 127
        ltb = 0
        rtb = 7
        print(line[:-1])
        for s in line[:-1]:
            if s == 'F':
                ub -= math.floor((ub-lb)/2)
            elif s == 'B':
                lb += math.ceil((ub-lb)/2)
            elif s == 'L':
                rtb -= math.floor((rtb-ltb)/2)
            elif s == 'R':
                ltb += math.ceil((rtb-ltb)/2)
        seat = (ub*8) + rtb
        if seat > max_seat:
            max_seat = seat
    
    print("Larget seat ID: {}".format(max_seat))
