# https://adventofcode.com/2020/day/2
if __name__ == "__main__":
    count = 0
    with open('./input', 'r') as f:
        lines = f.readlines()
        for line in lines:
            s = line.split(" ")
            pol = s[0].split("-")
            char = s[1].split(":")[0]
            pswd = s[2][:-1]
            occur = pswd.count(char)

            num = 0
            if pswd[int(pol[0])-1] == char:
                num += 1
            if pswd[int(pol[1])-1] == char:
                num += 1
            
            if num == 1:
                count += 1
    
    print("Number of valid passwords: {}".format(count))