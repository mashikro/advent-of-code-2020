# --- Part One ---

# find the two entries that sum to 2020 and then multiply those two numbers 
# together in advent_of_code_expense_report.rtf

def file_to_list(file):
    file_object = open(file) 
    nums = []
    for line in file_object:
        nums.append(int(line.strip()))
    return nums

def calculate(file):
    nums = file_to_list(file)

    for i in range(len(nums)):
        num1 = nums[i]
        for j in range(i, len(nums)):
            num2 = nums[j]
            # print("nums[i]+nums[j]", nums[i]+nums[j])
            if nums[i]+nums[j] == 2020:
                # print((nums[i]*nums[j]))
                return (nums[i]*nums[j])

# calculate("advent_of_code_expense_report.txt")

# --- Part Two ---

# find three numbers in your expense report that add up to 2020. return their product


def calculate2(file):
    nums = file_to_list(file)

    for i in range(len(nums)):
        num1 = nums[i]
        for j in range(i, len(nums)):
            num2 = nums[j]
            for k in range(j, len(nums)):
                num3 = nums[k]
                print("nums[i]+nums[j]+nums[k]", nums[i]+nums[j]+nums[k])
                if nums[i]+nums[j]+nums[k] == 2020:
                    print((nums[i]*nums[j]*nums[k]))
                    return (nums[i]*nums[j]*nums[k])

calculate2("advent_of_code_expense_report.txt")
