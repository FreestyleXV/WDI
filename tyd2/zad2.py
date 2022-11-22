def maximum_seating(seats):
    my_seats = seats.copy()
    free_seats = 0
    x = 0
    while x < len(my_seats):
        if my_seats[x] == 0:
            if x < len(my_seats)-3:
                if my_seats[x+1] == 0:
                    if my_seats[x+2] == 0:
                        my_seats[x] = 1
                        free_seats += 1
                        x = x+3
                    else:
                        x = x+2
                else:
                    x = x+1
            else:
                if x == len(my_seats)-2:
                    if my_seats[x+1] == 0:
                        my_seats[x] = 1
                        free_seats += 1
                        x = len(my_seats)
                else:
                    my_seats[x] = 1
                    free_seats += 1
                    x = len(my_seats)
        else:
            while x < len(my_seats)-1 and my_seats[x+1] == 1:
                x = x + 1
            x = x + 3
    print(seats)
    print(my_seats)
    return free_seats


tab = [0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0]
# tab = [0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0]
# tab = [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0]
# tab = [0, 0, 0, 0]
# tab = [0]
print(maximum_seating(tab))