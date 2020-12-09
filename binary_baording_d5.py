# --- Part One ---

def file_to_list(file):
    file_object = open(file)
    boarding_passes = []
    for line in file_object:
        boarding_passes.append(line.rstrip())

    return boarding_passes

# print(file_to_list("binary_baording_input.txt"))


def find_highest_seat_id(file):
    boarding_passes=file_to_list(file)

    # boarding_passes=file

    seat_ids = []


    for i in range(len(boarding_passes)):
        row = None
        col = None
        row_lower_band = 0
        row_upper_band = 127
        col_lower_band = 0
        col_upper_band = 7

        for j in range(len(boarding_passes[i])):
            current = boarding_passes[i][j]
            
            # print("__________")
            # print("j===", j)
            # print("current=", current)
            # print("row_lower_band=",row_lower_band)
            # print("row_upper_band=", row_upper_band)
            # print("col_lower_band=", col_lower_band)
            # print("col_upper_band=", col_upper_band)
            # print("row=", row)
            # print("col=", col)

            if current == "B":
                row_lower_band = row_lower_band + round((row_upper_band-row_lower_band)/2)
                row_upper_band = row_upper_band
                
                if j == 6:
                    row = row_upper_band


            elif current == "F":

                row_lower_band = row_lower_band
                row_upper_band = row_upper_band - round((row_upper_band-row_lower_band)/2)
                
                if j == 6:
                    row = row_lower_band
                    
            elif current == "R":
                col_lower_band = col_lower_band + round((col_upper_band-col_lower_band)/2)
                col_upper_band = col_upper_band
                if j == 9:
                    col = col_upper_band


            elif current == "L":
                col_lower_band = col_lower_band 
                col_upper_band = col_upper_band - round((col_upper_band-col_lower_band)/2)

                if j == 9:
                    col = col_lower_band


        seat_id = row*8+col
        seat_ids.append(seat_id)
        # print(seat_ids)


    # return max(seat_ids)
    return seat_ids


test = ["BFFFBBFRRR", "FBFBBFFRLR"]
# print(find_highest_seat_id("binary_baording_input.txt")) #965


# --- Part Two ---

def find_my_seat(file):

    seat_ids = find_highest_seat_id(file)
    seat_ids.sort()
    # print(seat_ids)

    possibilites = list(range(seat_ids[0], seat_ids[-1]))

    for i in range(len(possibilites)):
        if possibilites[i] != seat_ids[i]:
                return possibilites[i]



print(find_my_seat("binary_baording_input.txt"))





