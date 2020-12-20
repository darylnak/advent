# https://adventofcode.com/2020/day/2
if __name__ == "__main__":
    slope = []
    with open('./input.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            slope.append(line[:-1])

    x_pos = 0
    y_pos = 0
    num_trees = 0
    while y_pos < len(slope) - 1:
        y_pos += 1
        x_pos = 3*(y_pos%len(slope[0])) % len(slope[0])

        if slope[y_pos][x_pos] == '#':
            num_trees += 1

    print("Number of trees on the path: {}".format(num_trees))