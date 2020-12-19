# https://adventofcode.com/2020/day/1
if __name__ == "__main__":
    nums = {}
    target = 2020
    with open('./input', 'r') as f:
        lines = f.readlines()
        for line in lines:
            nums[int(line)] = int(line)

    for num in nums:
        check = target - num
        if check in nums:
            for num2 in nums:
                check2 = check - num2
                if check2 in nums:
                    print("{} * {} * {}= {}".format(check, check2, num2, num2*check*check2))
                    break