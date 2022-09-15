#leikreglur

"""

"""

NORTH = 'n'
SOUTH = 's'
WEST = 'w'
EAST = 'e'

x = 1
y = 1

def move(travel):
    if (travel == "n") or (travel == "N"):
        return x, y + 1
    elif (travel == "s") or (travel == "S"):
        return x, y - 1
    elif (travel == "w") or (travel == "W"):
        return x -1, y
    elif (travel == "e") or (travel == "E"):
        return x + 1, y


def valid_directions(x,y):
    valid_directions = '' 
    if x == 1 and y == 1:
        valid_directions = NORTH
    elif x == 1 and y == 2:
        valid_directions = NORTH + EAST + SOUTH
    elif x == 1 and y == 3: 
        valid_directions = SOUTH + EAST
    elif x == 2 and y == 3:
        valid_directions = EAST + WEST
    elif x == 2 and y == 2:
        valid_directions = WEST + SOUTH
    elif x == 2 and y == 1: 
        valid_directions = NORTH
    elif x == 3 and y == 3:
        valid_directions = WEST + SOUTH
    elif x == 3 and y == 2:
        valid_directions = NORTH + SOUTH
    elif x == 3 and y == 1:
        valid_directions = NORTH
    return valid_directions
    
def main():    
    pick_a_direction = input("Direction: ").lower()
    while pick_a_direction == "n" or pick_a_direction == "s" or pick_a_direction == "e" or pick_a_direction == "w":

        pick_a_direction = input("Direction: ").lower()

print(valid_directions(x,y))

if __name__ == "__main__":
    main()
    
