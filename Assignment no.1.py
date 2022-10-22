# Assignment 1:
# Create a program that will print your nickname using only asterisk character (*)

# J
for row in range(8):
    for col in range (10):
        if row == 0 or row == 1:
            print("*")
        if col == 4 or col == 5:
            print("*")
        else: print(" ")