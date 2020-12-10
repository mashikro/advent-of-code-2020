# -- PART ONE --

# Passport data is validated in batch files (your puzzle input). Each passport is 
# represented as a sequence of key:value pairs separated by spaces or newlines. 
# Passports are separated by blank lines.

# Count the number of valid passports - those that have all required fields. Treat cid as optional. 
# In your batch file, how many passports are valid?
def format_to_list(l):
    l = l.split("\n")
    ret = []
    for item in l:
        if item != "":
            ret.extend(item.split(" "))
    # print("ret=", ret)

    return ret

s = "byr:1937\neyr:2030 pid:154364481\nhgt:158cm iyr:2015 ecl:brn hcl:#c0946f cid:155\n"
# format_to_list(s)


def file_list_of_tuples(file):
    file_object=open(file)

    passports = []
    p = ""

    for line in file_object:
        line.rstrip()
        # print("line=", line)
        if not (not line.strip()):
            p+= line 
            # print("p=", p)
            
        else:
            passports.append(format_to_list(p))
            # print("passports=", passports)
            p = ""
      
    return passports

# print(file_list_of_tuples("test.txt"))
# print(file_list_of_tuples("password_processing_input.txt"))


def is_cid(l):
    for item in l:
        if "cid" in item:
            return True

def find_valid_passports(file):
    valid = 0

    passports = file_list_of_tuples(file)
    print(passports)
    print(len(passports))
    for passport in passports:
        if len(passport) == 8:
            valid+=1
        elif len(passport) == 7 and not is_cid(passport):
            valid +=1
    print("Valid passports ==", valid)
    return valid


find_valid_passports("password_processing_input.txt")


# -- PART TWO --

# The line is moving more quickly now, but you overhear airport security talking about 
# how passports with invalid data are getting through. Better add some data validation, quick!

# You can continue to ignore the cid field, but each other field has strict rules 
# about what values are valid for automatic validation:

# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.

# Your job is to count the passports where all required fields are both present 
# and valid according to the above rules. 

def list_to_dict(l):
    d = {}
    for item in l:
        x = item.split(":")
        d[x[0]] = x[1]
    return d

# print(list_to_dict(['eyr:2024', 'cid:274', 'pid:390115952', 'byr:1934', 'hgt:161cm', 'iyr:2017', 'hcl:#b95b0d']))

def check_byr(b_year):
    if len(b_year) == 4:
        year = int(b_year)
        if year >=1920 and year <=2002:
            return True
    return False

# print(check_byr("1929"))

def check_iyr(issue_year):
    if len(issue_year) == 4:
        year = int(issue_year)
        if year >=2010 and year <=2020:
            return True
    return False

# print(check_iyr("2021"))

def check_eyr(exp_year):
    if len(exp_year) == 4:
        year = int(exp_year)
        if year >=2020 and year <=2030:
            return True
    return False

# print(check_eyr("2020"))

def check_hgt(height):
    if ("cm" in height) and (len(height) == 5):
        h = int(height[:3])
        if h >=150 and h <=193:
            return True

    if ("in" in height) and (len(height) == 4):
        h = int(height[:2])
        if h >=59 and h <=76:
            return True
    
    return False

# print(check_hgt('260in'))

def check_hcl(hair_color):
    if len(hair_color) == 7:
        n ="0123456789"
        l = "abcdef"

        for item in hair_color[1:]:
            # print("item=", item)
            if (item in n):
                continue
            elif (item in l):
                continue
            else:
                return False
        return True
    return False

# print(check_hcl("#b95f0d"))

def check_ecl(eye_color):
    possibilities = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if len(eye_color) == 3 and eye_color in possibilities:
        return True
    return False

# print(check_ecl("blu"))

def check_pid(pass_id):
    if len(pass_id) == 9:
        # if pass_id[0:2] == "00":
        return True
    return False

def validate_data(passport):
    d = list_to_dict(passport)

    for item in d:
        if item == "byr":
            if  check_byr(d[item]) == False:
                return False
        if item == "iyr":
            if  check_iyr(d[item]) == False:
                return False
        if item == "eyr":
            if  check_eyr(d[item]) == False:
                return False
        if item == "hgt":
            if  check_hgt(d[item]) == False:
                return False
        if item == "hcl":
            if  check_hcl(d[item]) == False:
                return False
        if item == "ecl":
            if  check_ecl(d[item]) == False:
                return False
        if item == "pid":
            if  check_pid(d[item]) == False:
                return False

    return True

def find_present_valid_passports(file):
    valid = 0

    passports = file_list_of_tuples(file)
    # print(passports)
    # print(len(passports))
    for passport in passports:
        if len(passport) == 8:
            if validate_data(passport):
                valid+=1
        elif len(passport) == 7 and not is_cid(passport):
            if validate_data(passport):
                valid +=1
    print("Valid passports ==", valid)
    return valid

# find_present_valid_passports("password_processing_input.txt")
