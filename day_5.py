with open("./Julekalender/seat.txt", "r") as f:
    seat_IDs = [line.rstrip() for line in f]

seat_list = []
seat_list_mine = [num for num in range(12, 859)]

my_row = 0
my_column = 0

for seat_ID in seat_IDs:
    upper = 127
    lower = 0
    for letter in seat_ID[:7]:
        if letter == "F":
            upper = (upper + lower) // 2
        else:
            lower = (upper + lower) // 2 + 1
        
    if seat_ID[6] == "F":
        my_row = lower
    else:
        my_row = upper
        
    upper = 7
    lower = 0
    for letter in seat_ID[7:]:
        if letter == "L":
            upper = (upper + lower) // 2
        else:
            lower = (upper + lower) // 2 + 1
        
    if seat_ID[-1] == "L":
        my_column = lower
    else:
        my_column = upper
    
    seat = ((my_row * 8) + my_column)

    seat_list_mine.remove(seat)
    seat_list.append(seat)
    seat_list.sort()

print("Task 1:", seat_list[-1])
print("Tast 2:", seat_list_mine[0])

