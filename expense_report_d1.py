# PART 1
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

calculate("advent_of_code_expense_report.txt")