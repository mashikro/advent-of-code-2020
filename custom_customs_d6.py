def format_to_set(l):
    l = l.split("\n")
    # print("l=", l)
    ret = ""
    for item in l:
        if item != " ":
            ret += item
    # print("ret=", ret)

    return set(ret)


def file_to_list(file):

    file_object = open(file)
    answers = []
    p = ""

    for line in file_object:
        line.rstrip()
        # print("line1=", line)
        if not (not line.strip()):
            p+= line 
            # print("p=", p)
            
        else:
            answers.append(format_to_set(p))
            # print("answers=", answers)
            p = ""
      
    return answers

# print(file_to_list("custom_customs_input.txt"))
# print(file_to_list("test.txt"))


def count_answers(file):

    answers = file_to_list(file)
    s = 0

    for answer in answers:
        s+=len(answer)
        # print("s=",s)

    return s


print(count_answers("custom_customs_input.txt"))
# print(count_answers("test.txt"))

