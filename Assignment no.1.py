# Assignment 1:
# Create a program that will print your nickname using only asterisk character (*)

# J

list_J = [[" " for i in range(8)] for n in range(8)]
print(len(list_J))

for row in range(8):
    for col in range (8):
        if row == 0 or row == 1:
            list_J[row][col] = "*"
        if col == 3 or col == 4:
            list_J[row][col] = "*"
        if row == 6 and (col == 0 or col == 1 or col == 2):
            list_J[row][col] = "*"
        if row == 7 and (col == 1 or col == 2):
            list_J[row][col] = "*"
        if row == 4 and col == 0:
            list_J[row][col] = "*"
        if row == 5 and (col == 0 or col == 1):
            list_J[row][col] = "*"

# I

list_I = [[" " for i in range(8)] for n in range(8)]

for row in range(8):
    for col in range (8):
        if col == 3 or col == 4:
            list_I[row][col] = "*"
        if (row == 0 or row == 1 or row == 6 or row == 7):
            list_I[row][col] = "*"

# N

list_N = [[" " for i in range(8)] for n in range(8)]

for row in range(8):
    for col in range (8):
        if (col == 0 or col == 1 or col == 6 or col == 7):
            list_N[row][col] = "*"
        if row == 1:
            if col == 2:
                list_N[row][col] = "*"
        if row == 2:
            if col == 2 or col == 3:
                list_N[row][col] = "*"
        if row == 3:
            if col == 2 or col == 3 or col == 4:
                list_N[row][col] = "*"
        if row == 4:
            if col == 3 or col == 4 or col ==5:
                list_N[row][col] = "*"
        if row == 5:
            if col == 4 or col == 5:
                list_N[row][col] = "*"
        if row == 6:
            if col == 5:
                list_N[row][col] = "*"

# PRINT

for s in range(8):
    for k in range(8):
        print(list_J[s][k], end = ' ')
    print(end = " ")
    for k in range(8):
        print(list_I[s][k], end = ' ')
    print(end = " ")
    for k in range(8):
        print(list_N[s][k], end = ' ')
    print(end = " ")
    print()