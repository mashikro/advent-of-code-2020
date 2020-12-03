# -- PART ONE --

# Their password database seems to be a little corrupted: some of the passwords wouldn't 
# have been allowed by the Official Toboggan Corporate Policy that was in effect when they were chosen.

# To try to debug the problem, they have created a list (your puzzle input) of passwords 
# (according to the corrupted database) and the corporate policy when that password was set.

# For example, suppose you have the following list:

# 1-3 a: abcde
# 1-3 b: cdefg
# 2-9 c: ccccccccc
# Each line gives the password policy and then the password. The password policy 
# indicates the lowest and highest number of times a given letter must appear for 
# the password to be valid. For example, 1-3 a means that the password must contain 
# a at least 1 time and at most 3 times.

# In the above example, 2 passwords are valid. The middle password, cdefg, is not; 
# it contains no instances of b, but needs at least 1. The first and third passwords 
# are valid: they contain one a or nine c, both within the limits of their respective policies.

# How many passwords are valid according to their policies?
import pprint
pp = pprint.PrettyPrinter(indent=4)
from random import randrange


def generate_random_num():
    return randrange(100000000)

# generate_random_num()


def file_to_dict(file):
    file_object = open(file) 
    passwords = {}
    # (min, max, letter): password
    l = 0
    for line in file_object:
        clean_line = line.strip()
        l+=1
        # print("clean_line", clean_line)
        listed_line = clean_line.split(" ")
        # print("listed", listed_line)
        nums = listed_line[0].split("-")
        # print("nums", nums)
        min_ = int(nums[0])
        max_ = int(nums[1])
        letter = listed_line[1][:1]
        pw = listed_line[2]
        # print("----- items of dict")
        # print(min_)
        # print(max_)
        # print(letter)
        # print(pw)
        if (min_, max_, letter) not in passwords:
            passwords[(min_, max_, letter)] = pw
        else:
            r =generate_random_num()
            passwords[(min_, max_, letter, r)] = pw

    print(l)
    return passwords
# pp.pprint(file_to_dict("password_philosophy_input.txt"))


def find_valid_pw(file):
    passwords = file_to_dict(file)
    ret = 0

    for pw in passwords:
        count = passwords[pw].count(pw[2])
        if count >= pw[0] and count <= pw[1]:
            ret+=1

    return ret

print(find_valid_pw("password_philosophy_input.txt"))

# -- PART TWO --

# Each policy actually describes two positions in the password, where 1 means the first character, 
# 2 means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept 
#     of "index zero"!) Exactly one of these positions must contain the given letter. 
# Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

# Given the same example list from above:

# 1-3 a: abcde is valid: position 1 contains a and position 3 does not.
# 1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
# 2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
# How many passwords are valid according to the new interpretation of the policies?

def find_valid_pw_p2(file):
    passwords = file_to_dict(file)
    ret = 0

    for pw in passwords:
        # print("pw", pw)
        # print("paswords[pw]", passwords[pw])
        index_1 = pw[0]-1
        index_2 = pw[1]-1
        r = [False, False]
        if (passwords[pw][index_1] == pw[2]):
            r[0] = True
        if (passwords[pw][index_2] == pw[2]):
            r[1] = True
        if r.count(True)==1:
            ret +=1

    return ret

print(find_valid_pw_p2("password_philosophy_input.txt"))


