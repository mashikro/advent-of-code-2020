# -- PART ONE --

# start by counting all the trees you would encounter for the slope right 3, down 1
# From your starting position at the top-left, check the position that is right 3 and down 1. 
# Then, check the position that is right 3 and down 1 from there, and so on until you go past the bottom of the map.
# Starting at the top-left corner of your map and following a slope of right 3 and down 1, how many trees would you encounter?
import pprint
pp = pprint.PrettyPrinter(indent=4)

def file_to_matrix(file):
    file_object = open(file)

    matrix = []

    for line in file_object:
        matrix.append(list(line.rstrip()))

    return matrix

# print(file_to_matrix("travel_to_airport_input.txt"))


def count_trees(slope, matrix):
    
    trees = 0
    r = 0
    c = 0
    width = len(matrix[0])

    while r < len(matrix):
        
        if matrix[r][c%width] == '#':
            # print("tree")
            trees+=1
        r +=slope[0]
        c +=slope[1]

    return trees

print(count_trees((1,3), file_to_matrix("travel_to_airport_input.txt")))


# -- PART TWO --

# Determine the number of trees you would encounter if, for each of the following slopes, you start at the top-left corner and traverse the map all the way to the bottom:

# Right 1, down 1.
# Right 3, down 1. (This is the slope you already checked.)
# Right 5, down 1.
# Right 7, down 1.
# Right 1, down 2.
# In the above example, these slopes would find 2, 7, 3, 4, and 2 tree(s) respectively; multiplied together, these produce the answer 336.

# What do you get if you multiply together the number of trees encountered on each of the listed slopes?

def find_prod_of_slopes(slopes, file):
    matrix = file_to_matrix(file)
    ret =1
    for slope in slopes:
        trees = count_trees(slope, matrix)
        ret*=trees

    return ret

print(find_prod_of_slopes([(1,1), (1,3), (1,5), (1,7), (2,1)], "travel_to_airport_input.txt"))

