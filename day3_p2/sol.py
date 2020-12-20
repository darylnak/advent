# https://adventofcode.com/2020/day/3
# probably a terrible solution and definitely not scalable
if __name__ == "__main__":
    slope = []
    with open('./input.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            slope.append(line[:-1])

    x_moves =   [1, 3, 5, 7, 1]
    y_moves =   [1, 1, 1, 1, 2]
    x_posits =  [0 for x in x_moves]
    y_posits =  [0 for x in x_moves]
    num_trees = [0 for x in x_moves]
    done =      [0 for x in x_moves]
    itr = 1
    while True:
        for i in range(len(x_moves)):
            y_posits[i] += y_moves[i]
            if y_posits[i] >= len(slope):
                done[i] = 1
                continue
            x_posits[i] = x_moves[i] * (itr % len(slope[0])) % len(slope[0])
            if slope[y_posits[i]][x_posits[i]] == '#':
                num_trees[i] += 1
        itr += 1

        if sum(done) == len(done):
            break
    
    result = 1
    print(num_trees)
    for n in num_trees:
        result *= n

    print("Number of trees in each slope multiplied with each other: {}".format(result))