# Assignment 1:
# Create a program that will print your nickname using only asterisk character (*)

# J

for row in range(8):
    for col in range (10):
        if (row == 0 or row == 1) and (col == 1 or col == 2 or col == 3 or col == 4 or col == 5 or col == 6 or col == 7 or col == 8):
            print("*", end = "")
        elif (row != 0 or row != 1) and (col == 4 or col == 5):
            print("*", end = "")
        elif (row == 4 or row == 5 or row == 6 or row == 7) and (col == 1 or col == 2):
            print("*", end = "")
        elif (row == 6 or row == 7) and col == 3:
            print("*", end = "")
        else: print(end = " ")
    print()

# I

for row in range(8):
    for col in range (10):
        if  (col == 1 or col == 2 or col == 3 or col == 4 or col == 5 or col == 6 or col == 7 or col == 8) and (row == 0 or row == 1):
            print("*", end = "")
        elif (row != 0 or row != 1) and (col == 4 or col == 5):
            print("*", end = "")
        elif (row == 6 or row == 7) and (col == 1 or col == 2 or col == 3 or col == 4 or col == 5 or col == 6 or col == 7 or col == 8):
            print("*", end = "")
        else: print(end = " ")
    print()

# N

for row in range(8):
    for col in range (10):
        if (col == 1 or col == 2 or col == 7 or col == 8):
            print("*", end = "")
        elif col == 3 and (row == 1 or row == 2 or row == 3):
            print("*", end = "")
        elif col == 4 and (row == 2 or row == 3 or row == 4):
            print("*", end = "")
        elif col == 5 and (row == 3 or row == 4 or row == 5):
            print("*", end = "")
        elif col == 6 and (row == 4 or row == 5 or row == 6):
            print("*", end = "")
        else: print(end = " ")
    print()