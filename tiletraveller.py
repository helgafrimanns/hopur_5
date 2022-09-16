#leikreglur

"""

"""


NORTH = 'n'
SOUTH = 's'
WEST = 'w'
EAST = 'e'


x = 1
y = 1
travel = ''
valid_directions = ('')

def move(travel):
    if (travel == "n") or (travel == "N"):
        return x, y + 1
    elif (travel == "s") or (travel == "S"):
        return x, y - 1
    elif (travel == "w") or (travel == "W"):
        return x -1, y
    elif (travel == "e") or (travel == "E"):
        return x + 1, y


while True:
    if travel in valid_directions:
        if x == 1 and y == 1:
            valid_directions = NORTH 
            print("You can travel: (N)orth.")
        elif x == 1 and y == 2:
            valid_directions = NORTH + EAST + SOUTH
            print("You can travel: (N)orth or (E)ast or (S)outh.")
        elif x == 1 and y == 3:
            valid_directions = SOUTH + EAST
            print("You can travel: (E)ast or (S)outh.")
        elif x == 2 and y == 3:
            valid_directions = EAST + WEST
            print("You can travel: (E)ast or (W)est.")
        elif x == 2 and y == 2:
            valid_directions = WEST + SOUTH
            print("You can travel: (S)outh or (W)est.")
        elif x == 2 and y == 1:
            valid_directions = NORTH
            print("You can travel: (N)orth.")
        elif x == 3 and y == 3:
            valid_directions = WEST + SOUTH
            print("You can travel: (S)outh or (W)est.")
        elif x == 3 and y == 2:
            valid_directions = NORTH + SOUTH
            print("You can travel: (N)orth or (S)outh.")
        elif x == 3 and y == 1:
            valid_directions = NORTH
            print("Victory!")
            exit()

    travel = input("Direction: ").lower()

    if travel in valid_directions:
        x, y = move(travel)
    else:
        print ('Not a valid direction!')
        if valid_directions == "n":
            print("You can travel: (N)orth.")
        elif valid_directions == "nes":
            print("You can travel: (N)orth or (E)ast or (S)outh.")
        elif valid_directions == "se":
            print("You can travel: (E)ast or (S)outh.")
        elif valid_directions == "ew":
            print("You can travel: (E)ast or (W)est.")
        elif valid_directions == "ws":
            print("You can travel: (S)outh or (W)est.")
        elif valid_directions == "ns":
            print("You can travel: (N)orth or (S)outh.")
