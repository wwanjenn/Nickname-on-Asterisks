# Assignment 1:
# Create a program that will print your nickname using only asterisk character (*)

# J

for row in range(8):
    for col in range (10):
        if (row == 0 or row == 1) and (col != 0 or col != 9):
            print("*", end = "")
        elif (row != 0 or row != 1) and (col == 4 or col == 5):
            print("*", end = "")
        elif (row == 4 or row == 5 or row == 6 or row == 7) and (col == 1 or col == 2):
            print("*", end = "")
        elif (row == 6 or row == 7) and col == 3:
            print("*", end = "")
        else: print(end = " ")
    print()