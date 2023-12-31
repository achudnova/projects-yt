# Day 1 - Trebuchet!?

#=================PART 1=================#
document = open("materials/input1.txt").read().splitlines()

total_sum = 0

for line in document:
    digits = [ ]

    for char in line:
        if char.isdigit(): 
            digits.append(char)
    
    value = int(digits[0] + digits[-1])
    total_sum += value

    print(f"Calibration value for line '{line}': {value}")

print("The solution is:", total_sum)


#=================PART 2=================#
document = open("materials/input1.txt")

str_to_num = {
    "one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
    "six": "6", "seven": "7", "eight": "8", "nine": "9",
}

def calc(line: str):
    nums = []

    for i in range(len(line)):
        if line[i].isdigit():
            nums.append(line[i])
        else:
            for num_str in str_to_num:
                if line[i:].startswith(num_str):
                    nums.append(str_to_num[num_str])
    return int(nums[0] + nums[-1])

solution = 0

for row in document:
    solution += calc(row)

print(f"The solution is {solution}")