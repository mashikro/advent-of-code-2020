def format_to_set(line_people):
    l = line_people[0].split("\n")
    # print("l=", l)
    ret = ""
    for item in l:
        if item != " ":
            ret += item
    # print("ret=", ret)

    return (ret, line_people[1])


def file_to_list(file):

    file_object = open(file)
    answers = []
    p = ""
    people = 0

    for line in file_object:
        line.rstrip()
        # print("line1=", line)
        if not (not line.strip()):
            p+= line 
            people +=1
            # print("p=", p)
            
        else:
            answers.append(format_to_set((p,people)))
            # print("answers=", answers)
            p = ""
            people = 0
      
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


# print(count_answers("custom_customs_input.txt"))
# print(count_answers("test.txt"))


# -- PART TWO --

# You don't need to identify the questions to which anyone answered "yes"; you need to identify the questions to which everyone answered "yes"!
import collections
def count_answers_v2(file):

    answers = file_to_list(file)
    s = 0
    for answer in answers:
        c = collections.Counter(answer[0])
        # print(c)
        # print("answer[1]=",answer[1])
        for v in c:
            if c[v] == answer[1]:
                s+=1
                # print("s=", s)
    return s



print(count_answers_v2("custom_customs_input.txt"))
# print(count_answers_v2("test.txt"))


