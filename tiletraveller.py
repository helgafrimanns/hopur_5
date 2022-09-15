#leikreglur

"""Leikurinn virkar þannig að ..."""



print("You can travel (N)orth.")
travel = input("Direction: ")

def direction(travel):
    if (travel == "n"):
        return "You can travel (N)orth."
    else:
        return "Not a valid direction!"
        
print(direction(travel))
    
